#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Iterable

from ..message import EmailMultiAlternatives


class BaseEmailBackend:
    """
    Base class for email backend implementations.

    Subclasses must at least overwrite :py:meth:`send_messages`

    :py:meth:`open` and :py:meth:`close` can be called indirectly by using a
    backend object as a context manager:

    .. code-block:: python

       with backend as connection:
           # do something with connection
           pass
    """
    def __init__(self, fail_silently=False, **kwargs):
        self.fail_silently = fail_silently

    def open(self):
        """
        Open a network connection.

        This method can be overwritten by backend implementations to
        open a network connection.

        It's up to the backend implementation to track the status of
        a network connection if it's needed by the backend.

        This method can be called by applications to force a single network
        connection to be used when sending mails. See the
        :py:meth:`airmailer.backend.smtp.SMTPEmailBackend.send_messages` method
        of the SMTP backend for a reference implementation.

        The default implementation does nothing.
        """
        pass

    def close(self):
        """Close a network connection."""
        pass

    def __enter__(self):
        try:
            self.open()
        except Exception:
            self.close()
            raise
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def send_messages(self, email_messages):
        """
        Send one or more :py:class:`airmailer.message.EmailMessage` objects and
        return the number of email messages sent.
        """
        raise NotImplementedError('subclasses of BaseEmailBackend must override send_messages() method')

    def send_mail(
        self,
        subject: str,
        message,
        from_email: str,
        recipient_list: Iterable[str],
        html_message: str = None,
        bcc: Iterable[str] = None,
        cc: Iterable[str] = None,
        reply_to: Iterable[str] = None,
    ):
        """
        Easy wrapper for sending a single message to a recipient list. All members
        of the recipient list will see the other recipients in the 'To' field.
        """
        mail = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
            bcc=bcc,
            cc=cc,
            reply_to=reply_to,
        )
        if html_message:
            mail.attach_alternative(html_message, 'text/html')

        with self as conn:
            num_sent = conn.send_messages([mail])

        return num_sent
