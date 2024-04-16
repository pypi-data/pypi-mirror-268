import ipih

from pih import A
from PolibaseService.const import *

SC = A.CT_SC
ISOLATED: bool = False
DEBUG: bool = False


def start(as_standalone: bool = False) -> None:

    if A.U.for_service(SD, as_standalone=as_standalone):

        from pih.collections import (
            PolibasePersonVisitSearchCritery,
            PolibasePersonVisitDS,
            PolibasePersonVisit,
            PolibasePerson,
        )
        from pih.consts.errors import Error
        from pih.tools import ParameterList, n, ne
        from PolibaseService.api import PolibaseApi as Api

        from datetime import datetime
        from typing import Any

        def service_call_handler(sc: SC, pl: ParameterList, context) -> Any:
            if sc == SC.get_polibase_person_by_pin:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_by_pin(pl.next(), pl.next()),
                )
            if sc == SC.get_polibase_person_by_email:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_by_email(pl.next(), pl.next()),
                )
            if sc == SC.get_polibase_persons_by_pin:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_list_by_pin(pl.next(), pl.next()),
                )
            if sc == SC.get_polibase_persons_by_card_registry_folder_name:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_list_in_card_registry_folder(pl.next(), pl.next()),
                )
            if sc == SC.get_polibase_person_pin_by_login:
                return A.R.pack(
                    A.CT_FCA.VALUE,
                    Api.get_person_pin_by_login(pl.next(), pl.next()),
                )

            if sc == SC.get_polibase_person_user_login_and_worstation_name_pair_list:
                return A.R.pack(
                    A.CT_FCA.VALUE_LIST,
                    Api.get_polibase_person_user_login_and_worstation_name_pair_list(
                        pl.next()
                    ),
                )
            if sc == SC.set_polibase_person_card_folder_name:
                return Api.set_card_folder_name_for_person(
                    pl.next(), pl.next(), pl.next()
                )
            if sc == SC.check_polibase_person_card_registry_folder_name:
                return check_for_person_card_registry_folder_name(pl.next())
            if sc == SC.set_polibase_person_email:
                return Api.set_person_email_by_pin(pl.next(), pl.next(), pl.next())
            if sc == SC.set_polibase_person_telephone_number:
                return Api.set_person_telephone_number_by_pin(
                    pl.next(),
                    pl.next(),
                    pl.next(),
                    pl.next(),
                )
            if sc == SC.get_polibase_person_registrator_by_pin:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_registrator_by_pin(pl.next(), pl.next()),
                )
            if sc == SC.update_person_change_date:
                return Api.update_person_change_date(pl.next(), pl.next())
            if sc == SC.get_polibase_person_operator_by_pin:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_operator_by_pin(pl.next(), pl.next()),
                )
            if sc == SC.get_polibase_persons_by_name:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_list_by_name(pl.next(), pl.next()),
                )
            if sc == SC.get_bonus_list:
                return A.R.pack(
                    A.CT_FCA.VALUE_LIST,
                    Api.get_bonus_list(pl.next(), pl.next()),
                )
            if sc == SC.get_polibase_person_pin_list_with_old_format_barcode:
                return A.R.pack(
                    A.CT_FCA.VALUE_LIST,
                    Api.get_person_pin_list_with_old_format_barcode(pl.next()),
                )
            if sc == SC.set_barcode_for_polibase_person:
                return Api.set_person_barcode_by_pin(pl.next(), pl.next(), pl.next())
            if sc == SC.get_polibase_persons_pin_by_visit_date:
                return A.R.pack(
                    A.CT_FCA.VALUE_LIST,
                    Api.get_person_pin_list_by_visit_date(
                        pl.next(), pl.next(), pl.next()
                    ),
                )
            if sc == SC.search_polibase_person_visits:
                value: PolibasePersonVisitSearchCritery = pl.next(
                    PolibasePersonVisitSearchCritery()
                )
                test: bool = pl.next()
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON_VISIT,
                    person_visit_list_mapper(
                        Api.search_person_visits(value, test), test
                    ),
                )
            if sc == SC.get_polibase_person_visits_last_id:
                return A.R.pack(A.CT_FCA.VALUE, Api.get_person_visit_last_id(pl.next()))
            if sc == SC.get_polibase_persons_by_telephone_number:
                return A.R.pack(
                    A.CT_FCA.POLIBASE_PERSON,
                    Api.get_person_list_by_telephone_number(pl.next()),
                )
            if sc == SC.execute_polibase_query:
                try:
                    return A.R.pack(
                        A.CT_FCA.VALUE,
                        Api.execute_query(pl.next(), pl.next()),
                    )
                except Error as error:
                    import grpc

                    return A.ER.rpc(
                        context, error.details, grpc.StatusCode.INVALID_ARGUMENT
                    )

        def person_visit_list_mapper(
            person_visit_list: list[PolibasePersonVisit], test: bool | None = None
        ) -> list[PolibasePersonVisitDS]:
            result: list[PolibasePersonVisitDS] = []
            if ne(person_visit_list):
                person_cache: dict[int, dict] = {
                    person[A.CT_FNC.PIN]: person
                    for person in Api.get_person_list_by_pin(
                        list(set(list(map(lambda item: item.pin, person_visit_list)))),
                        test,
                    )
                }
                for person_visit_item in person_visit_list:
                    pin: int = person_visit_item.pin  # type: ignore
                    cabinet_id: int = person_visit_item.cabinetID  # type: ignore
                    # default value is Null, None in python, but need convert to 0
                    person_visit_item.status = person_visit_item.status or 0
                    if pin not in [
                        0,
                        A.CT_P.RESERVED_TIME_A_PIN,
                        A.CT_P.RESERVED_TIME_B_PIN,
                        A.CT_P.RESERVED_TIME_C_PIN,
                    ]:
                        if (
                            person_visit_item.status
                            not in A.CT_P.STATUS_EXCLUDE_FROM_VISIT_RESULT
                            and cabinet_id
                            not in A.CT_P.CABINET_NUMBER_EXCLUDED_FROM_VISIT_RESULT
                        ):
                            full_name: str | None = None
                            telephone_number: str | None = None
                            if pin != A.CT_P.PRERECORDING_PIN:
                                person: dict = person_cache[pin]
                                full_name = person[A.CT_FNC.FULL_NAME]
                                telephone_number = person[A.CT_FNC.TELEPHONE_NUMBER]
                            else:
                                full_name = person_visit_item.FullName
                                telephone_number = person_visit_item.telephoneNumber
                            if (
                                cabinet_id
                                in A.CT_P.AppointmentServiceGroupId._value2member_map_
                            ):
                                person_visit_item.serviceGroupID = cabinet_id
                            if not (n(full_name) or n(telephone_number)):
                                full_name = A.D_F.name(full_name, True)
                                telephone_number = A.D_F.telephone_number(
                                    telephone_number
                                )
                                begin_date: datetime = person_visit_item.beginDate
                                complete_date: datetime = person_visit_item.completeDate
                                begin_date2: datetime = person_visit_item.beginDate2
                                complete_date2: datetime = (
                                    person_visit_item.completeDate2
                                )
                                if (
                                    begin_date2 is not None
                                    and begin_date2.year != A.CT_P.DATE_IS_NOT_SET_YEAR
                                ):
                                    begin_date = begin_date2
                                if (
                                    complete_date2 is not None
                                    and complete_date2.year
                                    != A.CT_P.DATE_IS_NOT_SET_YEAR
                                ):
                                    complete_date = complete_date2
                                result.append(
                                    PolibasePersonVisitDS(
                                        person_visit_item.pin,
                                        full_name,
                                        telephone_number,
                                        person_visit_item.id,
                                        A.D.datetime_to_string(
                                            person_visit_item.registrationDate,
                                            A.CT.ISO_DATETIME_FORMAT,
                                        ),
                                        A.D.datetime_to_string(
                                            begin_date, A.CT.ISO_DATETIME_FORMAT
                                        ),
                                        A.D.datetime_to_string(
                                            complete_date, A.CT.ISO_DATETIME_FORMAT
                                        ),
                                        person_visit_item.status,
                                        person_visit_item.cabinetID,
                                        person_visit_item.doctorID,
                                        person_visit_item.doctorFullName,
                                        person_visit_item.serviceGroupID or 0,
                                    )
                                )
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
            return result

        def check_for_person_card_registry_folder_name(value: str | None) -> bool:
            last_is_alpha: bool = value[-1].isalpha() and len(value) > 2
            return ne(value) and (
                value[0].lower() in A.CT_P.CARD_REGISTRY_FOLDER_NAME_CHECK_PATTERN
                and len(value) <= 4
                and (
                    not last_is_alpha
                    and value[1:].isdecimal()
                    or (last_is_alpha and value[1:-1].isdecimal())
                )
            )

        def on_note_emailed_update_handler(id: int, person_pin) -> None:
            A.E.send(
                *A.E_B.mail_to_polibase_person_was_sent(
                    id,
                    person_pin,
                )
            )

        def on_person_creation_or_update_handler(
            person_data: dict[str, Any], update: bool
        ) -> None:
            person: PolibasePerson = A.D.fill_data_from_source(
                PolibasePerson(), person_data
            )
            A.E.send(
                *(
                    (
                        A.E_B.polibase_person_was_updated
                        if update
                        else A.E_B.polibase_person_was_created
                    )(person)
                )
            )

        def on_person_saldo_update_handler(
            person_saldo_data: dict[str, float | int]
        ) -> None:
            print(person_saldo_data)
            id: int = person_saldo_data[A.CT_FNC.ID]  # type: ignore
            doctor_id: int = person_saldo_data[A.CT_FNC.DOCTOR_ID]  # type: ignore
            bonus_minus: int = person_saldo_data["bonus_minus"] or 0  # type: ignore
            bonus_plus: int = person_saldo_data["bonus_plus"] or 0  # type: ignore
            doctor_bonus_pin_list: list[int] = A.S.get(
                A.CT_S.BONUS_DOCTOR_PERSON_PIN_LIST
            )
            if bonus_plus > 0:
                if doctor_id in doctor_bonus_pin_list:
                    A.E.send(
                        A.CT_E.POLIBASE_PERSON_BONUSES_WAS_UPDATED,
                        (person_saldo_data[A.CT_FNC.PERSON_PIN],),
                    )
                else:
                    Api.drop_person_bonus_by_id(id)
            if bonus_minus > 0:
                A.E.send(
                    A.CT_E.POLIBASE_PERSON_BONUSES_WAS_UPDATED,
                    (person_saldo_data[A.CT_FNC.PERSON_PIN],),
                )

        def service_starts_handler() -> None:
            Api.init(DEBUG)
            Api.on_note_emailed_update_handler = on_note_emailed_update_handler
            Api.on_person_creation_or_update_handler = (
                on_person_creation_or_update_handler
            )
            Api.on_person_saldo_update_handler = on_person_saldo_update_handler

        A.SRV_A.serve(
            SD,
            service_call_handler,
            service_starts_handler,
            isolate=ISOLATED,
            as_standalone=as_standalone,
        )


if __name__ == "__main__":
    start()
