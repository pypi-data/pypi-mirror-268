import ipih

from pih import A, serve, subscribe_on
from BonusProgramService.const import SD

SC = A.CT_SC

ISOLATED: bool = False


def start(as_standalone: bool = False) -> None:

    from BonusProgramService.api import BonusApi as Api
    from pih.tools import ParameterList, js, nn, one, nnt
    from pih.collections import BonusInformation, PolibasePerson, Message, EventDS

    from datetime import datetime

    api: Api = Api()

    class DH:
        timestamp: dict[int, datetime] = {}

    SENDER: str = A.D.get(A.CT_ME_WH_W.Profiles.CALL_CENTRE)

    def server_call_handler(sc: SC, pl: ParameterList) -> bool | None:
        if sc == SC.send_event:
            event: A.CT_E = A.D_Ex_E.get(pl)
            if event == A.CT_E.POLIBASE_PERSON_BONUSES_WAS_UPDATED:
                polibase_person_pin: int = A.D_Ex_E.parameters(pl)[0]
                bonus_information: BonusInformation | None = one(
                    A.R_P.bonus_information(polibase_person_pin)
                )
                if nn(bonus_information):
                    A.L.polibase(
                        js(
                            (
                                "Для клиента:",
                                polibase_person_pin,
                                "обновлены бонусы:",
                                nnt(bonus_information).bonus_last,
                                "из",
                                nnt(bonus_information).bonus_active,
                            )
                        )
                    )
                    if A.S.get(
                        A.CT_S.BONUS_PROGRAM_IS_ON
                    ) or polibase_person_pin == A.S.get(
                        A.CT_S.BONUS_PROGRAM_TEST_POLIBASE_PERSON_PIN
                    ):
                        polibase_person: PolibasePerson = A.D_P.person_by_pin(
                            polibase_person_pin
                        )
                        bonus_information: BonusInformation | None = one(
                            A.R_P.bonus_information(polibase_person)
                        )
                        if nn(bonus_information):
                            if nnt(bonus_information).bonus_active >= A.S.get(
                                A.CT_S.BONUS_PROGRAM_BONUS_MINIMUM
                            ):
                                link: str | None = None
                                if api.exists_bonus_card(polibase_person):
                                    if not api.exists_bonus_card(polibase_person, True):
                                        event_ds: EventDS | None = one(
                                            A.R_E.get_last(
                                                A.CT_E.POLIBASE_PERSONS_BONUS_CARD_WAS_CREATED,
                                                (polibase_person_pin,),
                                            )
                                        )
                                        link = A.D_Ex_E.value(
                                            event_ds,
                                            "url",
                                        )
                                        last_timestamp: datetime | None = A.D.if_is_in(
                                            DH.timestamp,
                                            polibase_person_pin,
                                            None,
                                        )
                                        if (
                                            nn(last_timestamp)
                                            and (
                                                A.D.now() - nnt(last_timestamp)
                                            ).total_seconds()
                                            < 5 * 60
                                        ):
                                            link = None

                                        DH.timestamp[polibase_person_pin] = A.D.now()
                                    else:
                                        api.update_bonuses(polibase_person)
                                else:
                                    link = api.create_bonus_card(polibase_person)
                                    if nn(link):
                                        A.E.send(
                                            A.CT_E.POLIBASE_PERSONS_BONUS_CARD_WAS_CREATED,
                                            (
                                                polibase_person_pin,
                                                link,
                                            ),
                                        )
                                        DH.timestamp[polibase_person_pin] = A.D.now()
                                if nn(link):
                                    A.ME_WH_W_Q.add_message(
                                        Message(
                                            js(("Перейдите по ссылке:", link)),
                                            polibase_person.telephoneNumber,
                                            A.D.get(SENDER),
                                        )
                                    )
                                else:
                                    pass
                        else:
                            pass
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
