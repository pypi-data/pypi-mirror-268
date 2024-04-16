import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import formataddr
from email import encoders
from typing import Union, List, Tuple


class SmtpEmailNotice:
    """
    邮件通知工具
    """

    def __init__(self,
                 smtp_server: str,
                 smtp_port: int,
                 from_email: str,
                 from_password: str,
                 from_name: str = None,
                 ssl=True):
        """
        :param smtp_server: SMTP 服务器域名, 例如: smtp.feishu.cn
        :param smtp_port: SMTP 服务器端口, 例如: 465
        :param from_email: 发件人邮箱, 例如: xxx@xxx.com
        :param from_password: 发件人密码
        :param from_name: 发件人名称
        :param ssl: 是否使用SMTP_SSL连接服务器
        """
        self._smtp_server = smtp_server
        self._smtp_port = smtp_port
        self._from_email = from_email
        self._from_password = from_password
        self._from_name = from_name if from_name else from_email
        self._ssl = ssl

    def send_email(self,
                   title: str,
                   body: str,
                   to_emails: Union[List[str], Tuple[str], str],
                   to_cc_mails: Union[List[str], Tuple[str], str, None] = None,
                   attachments: Union[List[str], Tuple[str], str, None] = None):
        """
        发送邮件功能, 支持抄送、附件, 目前仅支持 html 渲染的 body 样式
        :param title: 邮件主题
        :param body: 邮件正文
        :param to_emails: 收件人, 支持多个收件人
        :param to_cc_mails: 抄送人, 支持多个抄送人
        :param attachments: 附件, 支持多个附件, 附件的绝对路径或相对路径
        :raise SMTPException: 发送邮件异常
        """
        message = MIMEMultipart()
        # 主题
        message['Subject'] = Header(title, 'utf-8')
        # 发件人
        message['From'] = formataddr(
            (self._from_name, self._from_email), 'utf-8')
        # 抄送人
        if isinstance(to_cc_mails, (tuple, list)):
            to_cc_mails = ','.join(to_cc_mails)
        message['Cc'] = to_cc_mails
        # 邮件正文
        message.attach(MIMEText(body, 'html'))
        # 附件
        if attachments:
            if isinstance(attachments, str):
                attachments = [attachments]
            for attachment in attachments:
                with open(attachment, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                filename = attachment.split(os.sep)[-1]
                part.add_header('Content-Disposition',
                                f'attachment; filename= {filename}')
                message.attach(part)

        # 连接服务器发送邮件
        if self._ssl:
            server = smtplib.SMTP_SSL(self._smtp_server, self._smtp_port)
        else:
            server = smtplib.SMTP(self._smtp_server, self._smtp_port)
        server.login(self._from_email, self._from_password)
        server.send_message(message, self._from_email, to_emails)
