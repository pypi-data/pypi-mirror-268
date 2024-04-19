import ipih

from pih import A
from AnswerAutomationService.const import SD

SC = A.CT_SC

ISOLATED: bool = False


class ANSWER_TYPE:

    VISIT = 0
    TAX_CERTIFICATE = 1
    VISIT_MODIFICATION = 2


def start(as_standalone: bool = False) -> None:

    from pih.collections import (
        Message,
        PolibasePerson,
        WhatsAppMessage,
        PolibasePersonVisitDS as PPVDS,
        PolibasePersonNotificationConfirmation as PPNC,
    )

    from pih import serve, subscribe_on
    from pih.tools import ParameterList, ne, nn, lw, one, nnt

    SENDER: str = A.D.get(A.CT_ME_WH_W.Profiles.CALL_CENTRE)

    def polibase_person_name_format(value: str, polibase_person: PolibasePerson) -> str:
        return value.format(name=A.D.to_given_name(polibase_person))

    def server_call_handler(sc: SC, pl: ParameterList) -> bool | None:
        if sc == SC.send_event:
            event: A.CT_E = A.D_Ex_E.get(pl)
            if event == A.CT_E.WHATSAPP_MESSAGE_RECEIVED:
                whatsapp_message: WhatsAppMessage | None = A.D_Ex_E.whatsapp_message(pl)
                if ne(whatsapp_message):
                    sender: str = nnt(nnt(whatsapp_message).profile_id)
                    if sender == SENDER:
                        telephone_number: str = A.D_F.telephone_number_international(
                            nnt(nnt(whatsapp_message).sender)
                        )
                        notification_confirmation: PPNC | None = A.R_P_N_C.by(
                            telephone_number, sender
                        ).data
                        if (
                            ne(notification_confirmation)
                            and nnt(notification_confirmation).status == 2
                        ):
                            visit_ds: PPVDS | None = one(
                                A.R_P_V_DS.search(
                                    PPVDS(
                                        telephoneNumber=A.D_F.telephone_number(
                                            telephone_number
                                        )
                                    )
                                )
                            )
                            if nn(visit_ds):
                                pin: int = nnt(nnt(visit_ds).pin)
                                person: PolibasePerson = (
                                    PolibasePerson(
                                        pin,
                                        nnt(visit_ds).FullName,
                                        nnt(visit_ds).telephoneNumber,
                                    )
                                    if pin == A.CT_P.PRERECORDING_PIN
                                    else A.D_P.person_by_pin(pin)
                                )
                                if A.A_P_N_C.update(telephone_number, sender, 1):

                                    answer_type: int | None = None

                                    message: str = nnt(nnt(whatsapp_message).message)
                                    mesasge_word_list: list[str] = lw(
                                        A.D.not_empty_items(
                                            nnt(A.D.space_format(message)).split(" ")
                                        )
                                    )  # type: ignore
                                    tax_certificate_variant_list: list[str] = A.S.get(
                                        A.CT_S.POLIBASE_ANSWER_PERSON_TAX_CERTIFICATE_VARIANTS
                                    )
                                    visit_modification_variant_list: list[str] = (
                                        A.S.get(
                                            A.CT_S.POLIBASE_PERSON_ANSWER_VISIT_MODIFICATION_VARIANTS
                                        )
                                    )
                                    for word in mesasge_word_list:
                                        if nn(answer_type):
                                            break
                                        for (
                                            tax_certificate_word
                                        ) in tax_certificate_variant_list:
                                            if word.startswith(tax_certificate_word):
                                                answer_type = (
                                                    ANSWER_TYPE.TAX_CERTIFICATE
                                                )
                                                break

                                        for (
                                            visit_modification_word
                                        ) in visit_modification_variant_list:
                                            if word.startswith(visit_modification_word):
                                                answer_type = (
                                                    ANSWER_TYPE.VISIT_MODIFICATION
                                                )
                                                break
                                    answer_type = answer_type or ANSWER_TYPE.VISIT

                                    A.ME_WH_W_Q.add_message(
                                        Message(
                                            [
                                                A.S_P_V.offer_telegram_bot_url_text(
                                                    person
                                                ),
                                                polibase_person_name_format(
                                                    A.S.get(
                                                        A.CT_S.POLIBASE_PERSON_ANSWER_TAX_CERTIFICATE_TEXT
                                                    ),
                                                    person,
                                                ),
                                                polibase_person_name_format(
                                                    A.S.get(
                                                        A.CT_S.POLIBASE_PERSON_ANSWER_VISIT_MODIFICATION_TEXT
                                                    ),
                                                    person,
                                                ),
                                            ][answer_type],
                                            telephone_number,
                                            sender,
                                        )
                                    )
                                    if answer_type in (
                                        ANSWER_TYPE.VISIT,
                                        ANSWER_TYPE.TAX_CERTIFICATE,
                                    ):
                                        A.ME_WH_W_Q.add_message(
                                            Message(
                                                [
                                                    A.CT_P.TELEGRAM_BOT_URL,
                                                    A.CT_P.TAX_CERTIFICATE_URL,
                                                ][answer_type],
                                                telephone_number,
                                                sender,
                                            )
                                        )

                                    A.E.polibase_person_answered(person, message)
        return None

    def service_starts_handler() -> None:
        subscribe_on(SC.send_event)

    serve(
        SD,
        server_call_handler,
        service_starts_handler,
        isolate=ISOLATED,
        as_standalone=as_standalone,
    )


if __name__ == "__main__":
    start()
