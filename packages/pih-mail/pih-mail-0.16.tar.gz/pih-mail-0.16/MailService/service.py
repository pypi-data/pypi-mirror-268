import ipih

from pih import A
from MailService.const import *
from pih.collections import MailboxInfo, NewMailMessage
from pih.tools import ne, j, n, e, nn, lw, one, nnd, nns, nna
from pih.consts import EmailVerificationMethods, CHARSETS

import smtplib
import dns.resolver
from time import sleep
from typing import Any

SC = A.CT_SC
EVM = A.CT_EVM

ISOLATED: bool = False


class DH:

    EMAIL_IT_USER_PASSWORD: str | None = None
    EMAIL_RECEPTION_USER_PASSWORD: str | None = None
    EMAIL_CALL_CENTER_USER_PASSWORD: str | None = None
    EXTERNAL_EMAIL_USER_PASSWORD: str | None = None
    EMAIL_ADD_EMAIL_USER_PASSWORD: str | None = None
    ABSTRACT_API_KEY: str | None = None


def start(as_standalone: bool = False) -> None:

    if A.U.for_service(SD, as_standalone=as_standalone):

        from pih.tools import ParameterList

        from imap_tools.mailbox import MailMessage
        from imap_tools import MailBox, AND
        from requests import Response
        from smtplib import SMTP
        import requests
        import ssl

        def service_call_handler(sc: SC, pl: ParameterList) -> Any | None:
            if sc == SC.heart_beat:
                for mailbox_item in [
                    (
                        A.CT_ADDR.EMAIL_SERVER_ADDRESS,
                        A.CT_EML.IT,
                        DH.EMAIL_IT_USER_PASSWORD,
                    ),
                    (
                        A.CT_ADDR.EMAIL_SERVER_ADDRESS,
                        A.CT_EML.RECEPTION,
                        DH.EMAIL_RECEPTION_USER_PASSWORD,
                    ),
                    (
                        A.CT_ADDR.EMAIL_SERVER_ADDRESS,
                        A.CT_EML.CALL_CENTRE,
                        DH.EMAIL_CALL_CENTER_USER_PASSWORD,
                    ),
                    (
                        A.CT_ADDR.EMAIL_SERVER_ADDRESS,
                        A.CT_EML.ADD_EMAIL,
                        DH.EMAIL_ADD_EMAIL_USER_PASSWORD,
                    ),
                    (
                        A.CT_EML.EXTERNAL_SERVER,
                        A.CT_EML.EXTERNAL,
                        DH.EXTERNAL_EMAIL_USER_PASSWORD,
                    ),
                ]:
                    try:
                        mailbox_server: str = mailbox_item[0]
                        mailbox_address: str = mailbox_item[1]
                        mailbox_password: str = nns(mailbox_item[2])
                        mail_message: MailMessage | None = None
                        with MailBox(mailbox_server).login(
                            mailbox_address, mailbox_password
                        ) as mailbox:
                            mail_message_list: list[MailMessage] = []
                            mailbox_info: MailboxInfo | None = A.R.get_first_item(
                                A.R_DS.value(
                                    mailbox_address, A.D_Ex.mailbox_info, SECTION
                                )
                            )
                            last_uid: str | None = None
                            if ne(mailbox_info):
                                last_uid = nna(mailbox_info).last_uid
                            for mail_message in mailbox.fetch(
                                AND(date=A.D.today()),
                                mark_seen=False,
                                headers_only=True,
                                bulk=True,
                            ):
                                if e(last_uid) or (
                                    ne(mail_message.uid)
                                    and int(nns(last_uid)) < int(nns(mail_message.uid))
                                ):
                                    mail_message_list.append(mail_message)
                            if ne(mail_message_list):
                                new_mail_messages: list[NewMailMessage] = []
                                for mail_message in mailbox.fetch(
                                    AND(
                                        uid=A.D.map(
                                            lambda item: item.uid, mail_message_list
                                        )
                                    ),
                                    mark_seen=False,
                                ):
                                    new_mail_message: NewMailMessage = NewMailMessage(
                                        mailbox_address,
                                        mail_message.subject,
                                        mail_message.text,
                                        mail_message.from_,
                                    )
                                    new_mail_messages.append(new_mail_message)
                                    A.E.new_mail_message_was_received(new_mail_message)
                                mail_message = mail_message_list[-1]
                                A.A_DS.value(
                                    MailboxInfo(
                                        mail_message.date, int(mail_message.uid)
                                    ),
                                    mailbox_address,
                                    SECTION,
                                )
                    except Exception as _:
                        pass
                return True
            check_email_accessibility: bool = sc == SC.check_email_accessibility
            if check_email_accessibility or sc == SC.get_email_information:
                email_address: str = lw(pl.next())
                method: str = pl.next()
                cached: bool = pl.next()
                result: bool | None = (
                    one(A.R_DS.value(email_address, None, SECTION_DELIVERITY))
                    if cached
                    else None
                )
                if nn(result):
                    return result
                domain: str = email_address.split(A.CT.EMAIL_SPLITTER)[1]
                if check_email_accessibility and method == A.D.get(
                    EmailVerificationMethods.NORMAL
                ):
                    server = smtplib.SMTP()
                    server.set_debuglevel(0)
                    server.connect(str(dns.resolver.resolve(domain, "MX")[0].exchange))
                    server.helo(server.local_hostname)
                    server.mail(A.CT_EML.IT)
                    code, _ = server.rcpt(email_address)
                    server.quit()
                    result = code == 250
                    A.A_DS.value(result, email_address, SECTION_DELIVERITY)
                    return result
                content: dict[str, Any] | None = None
                count: int = TRY_AGAIN_COUNT
                email_deliverability_status: str | None = None
                while True:
                    try:
                        response: Response = requests.get(
                            j(
                                (
                                    "https://emailvalidation.abstractapi.com/v1/?api_key=",
                                    DH.ABSTRACT_API_KEY,
                                    "&email=",
                                    email_address,
                                )
                            ),
                            timeout=TIMEOUT,
                        )
                        if response.status_code == 200:
                            content = A.D.rpc_decode(
                                response.content.decode(CHARSETS.UTF8)
                            )
                            email_deliverability_status = nnd(content)[
                                EMAIL_STATUS_FIELD
                            ]
                        else:
                            sleep(TRY_AGAIN_SLEEP_TIME)
                            if count == 0:
                                break
                            count -= 1
                    except Exception as _:
                        sleep(TRY_AGAIN_SLEEP_TIME)
                        if count == 0:
                            break
                        count -= 1
                    if nn(email_deliverability_status):
                        if (
                            email_deliverability_status
                            == EMAIL_DELIVERABILITY_STATUS.UNKNOWN
                        ):
                            sleep(TRY_AGAIN_SLEEP_TIME)
                            if count == 0:
                                break
                            count -= 1
                            continue
                        else:
                            break
                if check_email_accessibility:
                    if n(content):
                        return None
                    result = (
                        email_deliverability_status == EMAIL_DELIVERABILITY_STATUS.YES
                    )
                    A.A_DS.value(result, email_address, SECTION_DELIVERITY)
                    return result
                return A.R.pack(A.CT_FC.VALUE, content)

            if sc == SC.send_email:
                context = ssl.create_default_context()
                server: SMTP = SMTP(A.CT_ADDR.EMAIL_SERVER_ADDRESS, A.CT_PORT.SMTP)
                try:
                    server.ehlo()
                    server.starttls(context=context)
                    server.ehlo()
                    server.login(A.CT_EML.IT, nns(DH.EMAIL_IT_USER_PASSWORD))
                    server.sendmail(
                        A.CT_EML.IT,
                        pl.next(),
                        pl.next().encode(CHARSETS.UTF8),
                    )
                except Exception as _:
                    pass
                finally:
                    server.quit()

            return False

        def service_starts_handler() -> None:
            DH.EMAIL_IT_USER_PASSWORD = A.D_V_E.value("EMAIL_IT_USER_PASSWORD")
            DH.EMAIL_RECEPTION_USER_PASSWORD = A.D_V_E.value(
                "EMAIL_RECEPTION_USER_PASSWORD"
            )
            DH.EMAIL_CALL_CENTER_USER_PASSWORD = A.D_V_E.value(
                "EMAIL_CALL_CENTER_USER_PASSWORD"
            )
            DH.EXTERNAL_EMAIL_USER_PASSWORD = A.D_V_E.value(
                "EXTERNAL_EMAIL_USER_PASSWORD"
            )
            DH.EMAIL_ADD_EMAIL_USER_PASSWORD = A.D_V_E.value(
                "EMAIL_ADD_EMAIL_USER_PASSWORD"
            )
            DH.ABSTRACT_API_KEY = A.D_V_E.value("ABSTRACT_API_KEY")
            A.SRV_A.subscribe_on(SC.heart_beat)

        A.SRV_A.serve(
            SD,
            service_call_handler,
            service_starts_handler,
            isolate=ISOLATED,
            as_standalone=as_standalone,
            max_workers=1,
        )


if __name__ == "__main__":
    start()
