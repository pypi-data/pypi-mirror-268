#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List, Dict, Any
import boto3

import botocore
from botocore.vendored.requests.packages.urllib3.exceptions import ResponseError
from botocore.exceptions import BotoCoreError, ClientError

from ..logging import logger
from ..message import sanitize_address, EmailMessage
from .base import BaseEmailBackend


class SESEmailBackend(BaseEmailBackend):
    """
    Send mails using the AWS SES API.
    """

    def __init__(
        self,
        fail_silently: bool = False,
        aws_access_key_id: str = None,
        aws_secret_access_key: str = None,
        aws_region_name: str = None,
        configuration_set_name: str = None,
        aws_region_endpoint: str = None,
        aws_config=None,
        ses_from_arn: str = None,
        ses_source_arn: str = None,
        ses_return_path_arn: str = None,
        ses_tags: Dict[str, str] = None,
        **kwargs
    ):
        """
        Creates a client for the AWS SES API.

        Keyword Arguments:
            fail_silently: If ``True``, don't raise execeptions on client errors
            aws_access_key_id: the ``AWS_ACCESS_KEY_ID``, defaults to read from environment
            aws_secret_access_key: the ``AWS_SECRET_ACCESS_KEY``, defaults to read from environment
            aws_region_name: the name of the AWS region to use, defaults to read from environment
            configuration_set_name: the name of the SES Configuration Set to use
            aws_region_endpoint: the URL for the SES endpoint for the region
            aws_config: a properly constructed :py:class:`botocore.config.Config` object
            ses_from_arn: the ``FromArn`` when using cross-account identities
            ses_source_arn: the ``SourceArn`` when using cross-account identities
            ses_return_path_arn: the ``ReturnPathArn`` when using cross-account identities
            ses_tags: a dictionary of tags to apply set as ``X-SES-MESSAGE-TAGS`` on each
                message sent
        """
        super().__init__(fail_silently=fail_silently)
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_region_name = aws_region_name
        self.aws_region_endpoint = aws_region_endpoint
        self.aws_config: botocore.client.Config = aws_config
        self.ses_source_arn = ses_source_arn
        self.ses_from_arn = ses_from_arn
        self.ses_return_path_arn = ses_return_path_arn
        self.configuration_set_name = configuration_set_name
        self.ses_tags = ses_tags
        self.connection = None

    def open(self) -> bool:
        """
        Opens a connection to the AWS SES API.

        Returns:
            ``True`` if the connection was opened successfully, ``False`` otherwise.
        """
        if self.connection:
            return False

        try:
            self.connection = boto3.client(
                "ses",
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                region_name=self.aws_region_name,
                endpoint_url=self.aws_region_endpoint,
                config=self.aws_config
            )
        except (ClientError, BotoCoreError):
            if not self.fail_silently:
                raise
            return False
        return True

    def close(self) -> None:
        """
        Close the connection to the AWS SES API.
        """
        self.connection = None

    def send_messages(self, email_messages: List[EmailMessage]) -> int:
        """
        Sends one or more messages returns the number of email messages sent.

        Args:
            email_messages: A list of emails to send

        Raises:
            botocore.exceptions.ClientError: AWS SES had an issue
            botocore.exceptions.BotoCoreError: AWS SES had an issue

        Returns:
            The number of messages sent
        """
        if not email_messages:
            return 0

        new_conn_created = self.open()
        if not self.connection:
            return 0

        sent_message_count = 0

        for email_message in email_messages:
            if self._send(email_message):
                sent_message_count += 1

        if new_conn_created:
            self.close()

        return sent_message_count

    def _send(self, email_message: EmailMessage) -> bool:
        """
        Sends an individual message.

        If the message was submitted successfully to the AWS SES API, set

        * ``email_message.extra_headers['status']`` to 200
        * ``email_message.extra_headers['message_id']`` to the ``MessageId``
        * ``email_message.extra_headers['request_id']`` to the ``RequestId`` of the AWS API call response

        If the message was not submitted successfully to the AWS SES API, set

        * ``email_message.extra_headers['status']`` to HTTP status of the response
        * ``email_message.extra_headers['reason']`` to "Reason" given for the error in the response
        * ``email_message.extra_headers['error_code']`` to error code of the response
        * ``email_message.extra_headers['error_message']`` to error message from the response
        * ``email_message.extra_headers['body']`` to body from the response
        * ``email_message.extra_headers['request_id']`` to the ``RequestId`` of the AWS API call response

        Args:
            email_message: An email to send

        Raises:
            botocore.exceptions.ClientError: AWS SES had an issue
            botocore.exceptions.BotoCoreError: AWS SES had an issue

        Returns:
            ``True`` if the message was sent, ``False`` otherwise
        """
        if not email_message.recipients():
            return False

        encoding = email_message.encoding
        from_email = sanitize_address(email_message.from_email, email_message.encoding)
        recipients = [sanitize_address(addr, encoding) for addr in email_message.recipients()]
        message = email_message.message()

        try:
            kwargs: Dict[str, Any] = {
                "Source": from_email,
                "Destinations": recipients,
                "RawMessage": {"Data": message.as_bytes(linesep="\r\n")},
            }

            if self.configuration_set_name is not None:
                kwargs["ConfigurationSetName"] = self.configuration_set_name
            if self.ses_source_arn:
                kwargs['SourceArn'] = self.ses_source_arn
            if self.ses_from_arn:
                kwargs['FromArn'] = self.ses_from_arn
            if self.ses_return_path_arn:
                kwargs['ReturnPathArn'] = self.ses_return_path_arn
            if self.ses_tags is not None:
                kwargs["Tags"] = [
                    {"Name": key, "Value": value}
                    for key, value in self.ses_tags.items()
                ]
            response = self.connection.send_raw_email(**kwargs)  # type: ignore
        except ResponseError as err:
            # Store failure information so to post process it if required
            error_keys = ['status', 'reason', 'body', 'request_id',
                          'error_code', 'error_message']
            for key in error_keys:
                email_message.extra_headers[key] = getattr(err, key, None)
            if not self.fail_silently:
                raise
            if self.configuration_set_name:
                logger.debug(
                    "airmailer.ses.send.success from='{}' recipients='{}' request_id='{}' "
                    "ses-configuration-set='{}' status='{}' error_code='{}' error_message='{}'".format(
                        email_message.from_email,
                        ", ".join(email_message.recipients()),
                        email_message.extra_headers['request_id'],
                        self.configuration_set_name,
                        email_message.extra_headers['status'],
                        email_message.extra_headers['error_code'],
                        email_message.extra_headers['error_message'],
                    )
                )
            return False
        email_message.extra_headers['status'] = 200
        email_message.extra_headers['message_id'] = response['MessageId']
        email_message.extra_headers['request_id'] = response['ResponseMetadata']['RequestId']
        logger.debug(
            "airmailer.ses.send.success from='{}' recipients='{}' message_id='{}' request_id='{}' "
            "ses-configuration-set='{}'".format(
                email_message.from_email,
                ", ".join(email_message.recipients()),
                email_message.extra_headers['message_id'],
                email_message.extra_headers['request_id'],
                self.configuration_set_name
            )
        )
        return True
