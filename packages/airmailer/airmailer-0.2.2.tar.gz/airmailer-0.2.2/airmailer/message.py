#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Adapted shamelessly from Django 3.2.9.
"""

from typing import Dict, Set, Optional, Union, Tuple, List, Iterable, cast

import mimetypes
from email import (
    charset as Charset, encoders as Encoders, generator, message_from_string,
)
from email.errors import HeaderParseError
from email.header import Header
from email.headerregistry import Address, parser  # type: ignore
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr, formatdate, getaddresses, make_msgid
from io import BytesIO, StringIO
from pathlib import Path
import socket

EmailPayload = Union[List[Message], str, bytes, bytearray]
EmailContent = Union[MIMEBase, str, bytes, bytearray]
EmailAttachment = Union[EmailContent, Tuple[str, bytes, str]]

#: Our ``utf-8`` charset definition.  This differs from the default in that we
#: configure it to not BASE64-encode UTF-8 messages so that we avoid unwanted
#: attention from : some spam filters.
utf8_charset = Charset.Charset('utf-8')
utf8_charset.body_encoding = None  # type: ignore
#: A specific ``utf-8`` charset definition that we use when one or more of the
#: lines in our message headers or body is longer than
#: :py:data:`RFC5322_EMAIL_LINE_LENGTH_LIMIT` : This sets the body encoding to
#: :py:data:`Charset.QP` (quoted-printable) to ensure that the message is still
#: delivered.  Quoted-printable encoding has the side effect of shortening the
#: long lines.
utf8_charset_qp = Charset.Charset('utf-8')
utf8_charset_qp.body_encoding = Charset.QP

#: Default MIME type to use on attachments (if it is not explicitly given
#: and cannot be guessed).
DEFAULT_ATTACHMENT_MIME_TYPE: str = 'application/octet-stream'

#: The maximum number of bytes allowed in a single header line, as per RFC 5322
RFC5322_EMAIL_LINE_LENGTH_LIMIT: int = 998


class BadHeaderError(ValueError):
    pass


#: Header names that contain structured address data (RFC #5322)
ADDRESS_HEADERS: Set[str] = {
    'from',
    'sender',
    'reply-to',
    'to',
    'cc',
    'bcc',
    'resent-from',
    'resent-sender',
    'resent-to',
    'resent-cc',
    'resent-bcc',
}


def force_str(s: Union[str, bytes], encoding: str = 'utf-8', errors: str = 'strict') -> str:
    """
    Given a string-like object, return the string version of it, encoded as
    specified in ``encoding``.

    Args:
        s: the string-like object
        encoding: the encoding to use to decode the bytestring, if s is a bytestring
        errors: how to handle errors in decoding the bytestring

    Returns:
        The decoded string.
    """
    if isinstance(s, bytes):
        s = str(s, encoding, errors)
    else:
        s = str(s)
    return s


def forbid_multi_line_headers(name: str, val: str, encoding: Optional[str]) -> Tuple[str, str]:
    """
    Forbid multi-line headers to prevent header injection.

    If ``name`` is in :data:`ADDRESS_HEADERS`, each address in ``val`` is run
    through :py:func:`sanitize_address`.

    Given a header name and header value, check if there are any newline
    characters in it. If there are, raise a ``BadHeaderError`` exception.

    Args:
        name: the header name
        val: the header value
        encoding: the encoding to use to decode ``val``, if 'ascii' encoding
            fails

    Raises:
        BadHeaderError: if there are any newline characters in the header value

    Returns:
        Sanitized header name and value.
    """
    encoding = encoding or 'utf-8'
    if '\n' in val or '\r' in val:
        raise BadHeaderError("Header values can't contain newlines (got %r for header %r)" % (val, name))
    try:
        val.encode('ascii')
    except UnicodeEncodeError:
        if name.lower() in ADDRESS_HEADERS:
            val = ', '.join(sanitize_address(addr, encoding) for addr in getaddresses((val,)))
        else:
            val = Header(val, encoding).encode()
    else:
        if name.lower() == 'subject':
            val = Header(val).encode()
    return name, val


def sanitize_address(addr: Union[str, Tuple[str, str]], encoding: str) -> str:
    """
    Format a pair of (name, address) or an email address string.

    Args:
        addr: the address to sanitize
        encoding: the encoding to use re-encode the address if 'ascii' is not
            sufficient

    Raises:
        ValueError: if the address is not a valid email address

    Returns:
        A santiized email address.
    """
    address = None
    if not isinstance(addr, tuple):
        addr = force_str(addr)
        try:
            token, rest = parser.get_mailbox(addr)
        except (HeaderParseError, ValueError, IndexError):
            raise ValueError('Invalid address "%s"' % addr)
        else:
            if rest:
                # The entire email address must be parsed.
                raise ValueError(
                    'Invalid address; only %s could be parsed from "%s"'
                    % (token, addr)
                )
            nm = token.display_name or ''
            localpart = token.local_part
            domain = token.domain or ''
    else:
        nm, address = addr
        localpart, domain = address.rsplit('@', 1)

    address_parts = nm + localpart + domain
    if '\n' in address_parts or '\r' in address_parts:
        raise ValueError('Invalid address; address parts cannot contain newlines.')

    # Avoid UTF-8 encode, if it's possible.
    try:
        nm.encode('ascii')
        nm = Header(nm).encode()
    except UnicodeEncodeError:
        nm = Header(nm, encoding).encode()
    try:
        localpart.encode('ascii')
    except UnicodeEncodeError:
        localpart = Header(localpart, encoding).encode()
    domain = domain.encode('idna').decode('ascii')

    parsed_address = Address(username=localpart, domain=domain)
    return formataddr((nm, parsed_address.addr_spec))


class MIMEMixin:
    """
    A mixin for :py:class:`Message` that provides methods for converting the
    message to string or bytes in ways the rest of the code expects.
    """

    def as_string(self, unixfrom: bool = False, linesep: str = '\n') -> str:
        """
        Return the entire formatted message as a string.

        Keyword Args:
            unixfrom: if ``True,`` include the Unix ``From_`` envelope header
            linesep: the line separator to use in the returned string

        Returns:
            The entire formatted message as a string.
        """
        fp = StringIO()
        g = generator.Generator(fp, mangle_from_=False)
        g.flatten(cast(Message, self), unixfrom=unixfrom, linesep=linesep)
        return fp.getvalue()

    def as_bytes(self, unixfrom: bool = False, linesep: str = '\n') -> bytes:
        """
        Return the entire formatted message as bytes.

        Keyword Args:
            unixfrom: if ``True,`` include the Unix ``From_`` envelope header
            linesep: the line separator to use in the returned string

        Returns:
            The entire formatted message as a string.
        """
        fp = BytesIO()
        g = generator.BytesGenerator(fp, mangle_from_=False)
        g.flatten(cast(Message, self), unixfrom=unixfrom, linesep=linesep)
        return fp.getvalue()


class SafeMIMEMessage(MIMEMixin, MIMEMessage):
    """
    A :py:class:`email.message.Message` subclass that sanitizes any headers
    before they are added to the message.
    """

    def __setitem__(self, name: str, val: str) -> None:
        """
        Add a header to the message, sanitizing the header name and value.

        Args:
            name: the header name
            val: the header value
        """
        # message/rfc822 attachments must be ASCII
        name, val = forbid_multi_line_headers(name, val, 'ascii')
        MIMEMessage.__setitem__(self, name, val)


class SafeMIMEText(MIMEMixin, MIMEText):
    """
    A :py:class:`email.mime.text.MIMEText` subclass doe some payload
    sanitization.

    * If the payload contains any lines longer than :py:data:`RFC5322_EMAIL_LINE_LENGTH_LIMIT`,
      use quoted-printable encoding for the body.
    * Sanitize any headers before they are added to the message.
    """

    def __init__(self, _text: str, _subtype='plain', _charset=None):
        self.encoding = _charset
        MIMEText.__init__(self, _text, _subtype=_subtype, _charset=_charset)

    def __setitem__(self, name: str, val: str) -> None:
        """
        Add a header to the message, sanitizing the header name and value.

        Args:
            name: the header name
            val: the header value
        """
        name, val = forbid_multi_line_headers(name, val, self.encoding)
        MIMEText.__setitem__(self, name, val)

    def set_payload(self, payload: str, charset: Union[str, Charset.Charset] = None):
        """
        If the payload contains any lines longer than
        :py:data:`RFC5322_EMAIL_LINE_LENGTH_LIMIT`, the payload will be encoded
        using quoted-printable encoding.

        Args:
            payload: the payload to set
            charset: the charset to use to encode the payload
        """
        if charset == 'utf-8' and not isinstance(charset, Charset.Charset):
            has_long_lines = any(
                len(line.encode()) > RFC5322_EMAIL_LINE_LENGTH_LIMIT
                for line in payload.splitlines()
            )
            # Quoted-Printable encoding has the side effect of shortening long
            # lines, if any (#22561).
            charset = utf8_charset_qp if has_long_lines else utf8_charset
        MIMEText.set_payload(self, payload, charset=charset)


class SafeMIMEMultipart(MIMEMixin, MIMEMultipart):
    """
    A mulitpart MIME message that sanitizes any headers before they are added.
    """

    def __init__(
        self,
        _subtype: str = 'mixed',
        boundary: str = None,
        _subparts=None,
        encoding: str = None,
        **_params
    ):
        self.encoding = encoding
        MIMEMultipart.__init__(self, _subtype, boundary, _subparts, **_params)

    def __setitem__(self, name: str, val: str) -> None:
        name, val = forbid_multi_line_headers(name, val, self.encoding)
        MIMEMultipart.__setitem__(self, name, val)


class EmailMessage:
    """
    A container class for email information.  We use this instead of
    :py:class:`email.message.Message` directly so that we can send the same
    message to multiple recipients and to ease the construction of the
    complicated ``Message`` object.
    """
    #: When constructing the mimetype for the message body, use this subtype of
    #: "text".  Default is "plain", which means that the message body
    #: will be specified as "text/plain".
    content_subtype: str = 'plain'
    mixed_subtype: str = 'mixed'
    #: Use this as the default encoding for our message body.
    encoding: str = 'utf-8'

    def __init__(
        self,
        subject: str = '',
        body: str = '',
        from_email: str = None,
        to: Iterable[str] = None,
        bcc: Iterable[str] = None,
        attachments: List[EmailAttachment] = None,
        headers: Dict[str, str] = None,
        cc: Iterable[str] = None,
        reply_to: Iterable[str] = None
    ):
        """
        Initialize a single email message (which can be sent to multiple
        recipients).
        """
        if to:
            if isinstance(to, str):
                raise TypeError('"to" argument must be a list or tuple')
            self.to = list(to)
        else:
            self.to = []
        if cc:
            if isinstance(cc, str):
                raise TypeError('"cc" argument must be a list or tuple')
            self.cc = list(cc)
        else:
            self.cc = []
        if bcc:
            if isinstance(bcc, str):
                raise TypeError('"bcc" argument must be a list or tuple')
            self.bcc = list(bcc)
        else:
            self.bcc = []
        if reply_to:
            if isinstance(reply_to, str):
                raise TypeError('"reply_to" argument must be a list or tuple')
            self.reply_to = list(reply_to)
        else:
            self.reply_to = []
        self.from_email = from_email
        self.subject = subject
        self.body = body or ''
        self.attachments = []
        if attachments:
            for attachment in attachments:
                if isinstance(attachment, MIMEBase):
                    self.attach(attachment)
                else:
                    self.attach(*attachment)
        self.extra_headers = headers or {}

    def message(self):
        encoding = self.encoding or 'utf-8'
        msg = SafeMIMEText(self.body, self.content_subtype, encoding)
        msg = self._create_message(msg)
        msg['Subject'] = self.subject
        msg['From'] = self.extra_headers.get('From', self.from_email)
        self._set_list_header_if_not_empty(msg, 'To', self.to)
        self._set_list_header_if_not_empty(msg, 'Cc', self.cc)
        self._set_list_header_if_not_empty(msg, 'Reply-To', self.reply_to)

        # Email header names are case-insensitive (RFC 2045), so we have to
        # accommodate that when doing comparisons.
        header_names = [key.lower() for key in self.extra_headers]
        if 'date' not in header_names:
            # formatdate() uses stdlib methods to format the date, which use
            # the stdlib/OS concept of a timezone, however, Django sets the
            # TZ environment variable based on the TIME_ZONE setting which
            # will get picked up by formatdate().
            msg['Date'] = formatdate(localtime=True)
        if 'message-id' not in header_names:
            msg['Message-ID'] = make_msgid(domain=socket.getfqdn())
        for name, value in self.extra_headers.items():
            if name.lower() != 'from':  # From is already handled
                msg[name] = value
        return msg

    def recipients(self):
        """
        Return a list of all recipients of the email (includes direct
        addressees as well as Cc and Bcc entries).
        """
        return [email for email in (self.to + self.cc + self.bcc) if email]

    def attach(
        self,
        filename: Union[Path, str] = None,
        content: EmailContent = None,
        mimetype: str = None
    ):
        """
        Attach a file with the given filename and content. The filename can
        be omitted and the mimetype is guessed, if not provided.

        If the first parameter is a :py:class:`email.mime.base.MIMEBase`
        subclass, insert it directly into the resulting message attachments.

        For a ``text/*`` mimetype (guessed or specified), when a bytes object is
        specified as content, decode it as UTF-8. If that fails, set the
        mimetype to :py:data:`DEFAULT_ATTACHMENT_MIME_TYPE` and don't decode the
        content.
        """
        if isinstance(filename, MIMEBase):
            if content is not None or mimetype is not None:
                raise ValueError(
                    'content and mimetype must not be given when a MIMEBase '
                    'instance is provided.'
                )
            self.attachments.append(filename)
        elif content is None:
            raise ValueError('content must be provided.')
        else:
            mimetype = mimetype or mimetypes.guess_type(filename)[0] or DEFAULT_ATTACHMENT_MIME_TYPE
            basetype, _ = mimetype.split('/', 1)

            if basetype == 'text':
                if isinstance(content, bytes):
                    try:
                        content = content.decode()
                    except UnicodeDecodeError:
                        # If mimetype suggests the file is text but it's
                        # actually binary, read() raises a UnicodeDecodeError.
                        mimetype = DEFAULT_ATTACHMENT_MIME_TYPE

            self.attachments.append((filename, content, mimetype))

    def attach_file(self, path: Union[Path, str], mimetype: str = None):
        """
        Attach a file from the filesystem.

        Set the mimetype to :py:data:`DEFAULT_ATTACHMENT_MIME_TYPE` if it isn't
        specified and cannot be guessed.

        For a ``text/*`` mimetype (guessed or specified), decode the file's
        content as UTF-8. If that fails, set the mimetype to
        :py:data:`DEFAULT_ATTACHMENT_MIME_TYPE` and don't decode the content.
        """
        path = Path(path)
        with path.open('rb') as file:
            content = file.read()
            self.attach(path.name, content, mimetype)

    def _create_message(self, msg: MIMEBase):
        return self._create_attachments(msg)

    def _create_attachments(self, msg: MIMEBase):
        if self.attachments:
            encoding = self.encoding or 'utf-8'
            body_msg = msg
            msg = SafeMIMEMultipart(_subtype=self.mixed_subtype, encoding=encoding)
            if self.body or body_msg.is_multipart():
                msg.attach(body_msg)
            for attachment in self.attachments:
                if isinstance(attachment, MIMEBase):
                    msg.attach(attachment)
                else:
                    msg.attach(self._create_attachment(*attachment))
        return msg

    def _create_mime_attachment(
        self,
        content: "Union[Message, EmailMessage, str]",
        mimetype: str
    ) -> Union[MIMEBase, SafeMIMEText, SafeMIMEMessage]:
        """
        Convert the content, mimetype pair into a MIME attachment object.

        If the mimetype is ``message/rfc822``, content may be an
        :py:class:`email.message.Message` or :py:class:`EmailMessage` object, as
        well as a str.

        Args:
            content: The content of the attachment.
            mimetype: The mimetype of the attachment.

        Returns:
            A MIME attachment object.
        """
        attachment: Union[MIMEBase, SafeMIMEText, SafeMIMEMessage]
        basetype, subtype = mimetype.split('/', 1)
        if basetype == 'text':
            encoding = self.encoding or 'utf-8'
            attachment = SafeMIMEText(cast(str, content), subtype, encoding)
        elif basetype == 'message' and subtype == 'rfc822':
            # Bug #18967: per RFC2046 s5.2.1, message/rfc822 attachments
            # must not be base64 encoded.
            if isinstance(content, EmailMessage):
                # convert content into an email.Message first
                content = content.message()
            elif not isinstance(content, Message):
                # For compatibility with existing code, parse the message
                # into an email.Message object if it is not one already.
                content = message_from_string(force_str(content))

            attachment = SafeMIMEMessage(cast(Message, content), subtype)
        else:
            # Encode non-text attachments with base64.
            attachment = MIMEBase(basetype, subtype)
            attachment.set_payload(content)
            Encoders.encode_base64(attachment)
        return attachment

    def _create_attachment(self, filename: str, content, mimetype: str = None):
        """
        Convert the filename, content, mimetype triple into a MIME attachment
        object.

        Args:
            filename: The filename to attach the content as.
            content: The content to attach.
            mimetype: The mimetype of the content, if not specified, guess
        """
        attachment = self._create_mime_attachment(content, mimetype)
        _filename: Union[str, Tuple[str, str, str]] = filename
        if _filename:
            try:
                cast(str, _filename).encode('ascii')
            except UnicodeEncodeError:
                _filename = ('utf-8', '', filename)
            attachment.add_header('Content-Disposition', 'attachment', filename=_filename)
        return attachment

    def _set_list_header_if_not_empty(self, msg, header, values):
        """
        Set msg's header, either from self.extra_headers, if present, or from
        the values argument.
        """
        if values:
            try:
                value = self.extra_headers[header]
            except KeyError:
                value = ', '.join(str(v) for v in values)
            msg[header] = value


class EmailMultiAlternatives(EmailMessage):
    """
    A version of :py:class:`EmailMessage` that makes it easy to send
    multipart/alternative messages. For example, including text and HTML
    versions of the text is made easier.
    """
    alternative_subtype: str = 'alternative'

    def __init__(
        self,
        subject: str = '',
        body: str = '',
        from_email: str = None,
        to: Iterable[str] = None,
        bcc: Iterable[str] = None,
        attachments: List[EmailAttachment] = None,
        headers: Dict[str, str] = None,
        alternatives=None,
        cc: Iterable[str] = None,
        reply_to: Iterable[str] = None
    ):
        """
        Initialize a single email message (which can be sent to multiple
        recipients).
        """
        super().__init__(
            subject, body, from_email, to, bcc, attachments,
            headers, cc, reply_to,
        )
        self.alternatives = alternatives or []

    def attach_alternative(self, content, mimetype):
        """Attach an alternative content representation."""
        if content is None or mimetype is None:
            raise ValueError('Both content and mimetype must be provided.')
        self.alternatives.append((content, mimetype))

    def _create_message(self, msg):
        return self._create_attachments(self._create_alternatives(msg))

    def _create_alternatives(self, msg):
        encoding = self.encoding or 'utf-8'
        if self.alternatives:
            body_msg = msg
            msg = SafeMIMEMultipart(_subtype=self.alternative_subtype, encoding=encoding)
            if self.body:
                msg.attach(body_msg)
            for alternative in self.alternatives:
                msg.attach(self._create_mime_attachment(*alternative))
        return msg
