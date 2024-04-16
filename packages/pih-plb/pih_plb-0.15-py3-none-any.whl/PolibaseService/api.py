from contextlib import contextmanager

import oracledb
from oracledb import SessionPool, DatabaseError, Cursor

oracledb.init_oracle_client()
# lib_dir="C:\\oracle"
import ipih
from pih import A, PIHThread
from pih.consts.errors import Error
from PolibaseService.const import *
from pih.collections import (
    PolibasePersonVisit,
    PolibasePersonVisitSearchCritery,
)
from pih.tools import (
    j,
    e,
    n,
    js,
    nn,
    ne,
    nl,
    one,
    esc,
    escs,
    BitMask as BM,
    while_not_do,
)

from typing import Any, Callable
import re


def get_host(test: bool) -> str:
    return (A.CT_H.POLIBASE_TEST if test else A.CT_H.POLIBASE1).NAME


def get_dsn(test: bool) -> str:
    return j(
        (
            get_host(test),
            A.D_V_E.value("ORACLE_INSTANCE"),
        ),
        "/",
    )


class PolibaseApi:
    pool_map: dict[bool, SessionPool] = {}
    # handlers
    on_note_emailed_update_handler: Callable[[int, int], None]
    on_person_creation_or_update_handler: Callable[[dict[str, Any], bool], None]
    on_person_saldo_update_handler: Callable[[dict[str, float | int]], None]

    @staticmethod
    def init(debug: bool) -> None:
        if not debug:
            PIHThread(PolibaseApi.create_cqn_for_person_update)
            PIHThread(PolibaseApi.create_cqn_for_note_emailed_update)
            PIHThread(PolibaseApi.create_cqn_for_person_saldo_insert)

    @staticmethod
    def cqn_callback_for_person_update(message):
        for query in message.queries:
            for table in query.tables:
                for row in table.rows:
                    PolibaseApi.on_person_creation_or_update_handler(
                        PolibaseApi.get_person_by_rowid(row.rowid),
                        BM.has(row.operation, oracledb.OPCODE_UPDATE),
                    )

    @staticmethod
    def cqn_callback_for_person_saldo_insert(message):
        for query in message.queries:
            for table in query.tables:
                for row in table.rows:
                    PolibaseApi.on_person_saldo_update_handler(
                        PolibaseApi.get_person_saldo_by_rowid(row.rowid)
                    )

    @staticmethod
    def cqn_callback_for_note_emailed_update(message):
        for query in message.queries:
            for table in query.tables:
                for row in table.rows:
                    note_emailed_data: dict[str, int] | None = (
                        PolibaseApi.get_note_emailed_by_rowid(row.rowid)
                    )
                    if ne(note_emailed_data):
                        if BM.has(row.operation, oracledb.OPCODE_INSERT):
                            PolibaseApi.on_note_emailed_update_handler(
                                note_emailed_data[A.CT_FNC.ID],
                                note_emailed_data[A.CT_FNC.PERSON_PIN],
                            )

    @staticmethod
    def create_cqn_for_person_update() -> None:
        with PolibaseApi.get_connection(False, False, True) as connection:
            subscribtion = connection.subscribe(
                callback=PolibaseApi.cqn_callback_for_person_update,
                operations=oracledb.OPCODE_INSERT | oracledb.OPCODE_UPDATE,
                qos=oracledb.SUBSCR_QOS_QUERY | oracledb.SUBSCR_QOS_ROWIDS,
            )
            subscribtion.registerquery(
                PolibaseApi.get_person_query(
                    [
                        PolibaseApi.get_person_barcode_field(),
                        PolibaseApi.get_person_email_field(),
                        PolibaseApi.get_person_chart_folder_field(),
                    ]
                    + PolibaseApi.get_person_telephone_numbers_field_list()
                )
            )
            while_not_do(sleep_time=1)

    @staticmethod
    def create_cqn_for_person_saldo_insert() -> None:
        with PolibaseApi.get_connection(False, False, True) as connection:
            subscribtion = connection.subscribe(
                callback=PolibaseApi.cqn_callback_for_person_saldo_insert,
                operations=oracledb.OPCODE_INSERT,
                qos=oracledb.SUBSCR_QOS_QUERY | oracledb.SUBSCR_QOS_ROWIDS,
            )
            subscribtion.registerquery(
                PolibaseApi.get_person_saldo_query_with_condition(True)
            )
            while_not_do(sleep_time=1)

    @staticmethod
    def create_cqn_for_note_emailed_update() -> None:
        with PolibaseApi.get_connection(False, False, True) as connection:
            subscribtion = connection.subscribe(
                callback=PolibaseApi.cqn_callback_for_note_emailed_update,
                operations=oracledb.OPCODE_INSERT,
                qos=oracledb.SUBSCR_QOS_QUERY | oracledb.SUBSCR_QOS_ROWIDS,
            )
            subscribtion.registerquery(PolibaseApi.get_note_emailed_query())
            while_not_do(sleep_time=1)

    @staticmethod
    def get_pool(test: bool = TEST) -> SessionPool:
        pool: SessionPool | None = None
        if test not in PolibaseApi.pool_map:
            pool = SessionPool(
                user=A.D_V_E.value("POLIBASE_USER_LOGIN"),
                password=A.D_V_E.value("POLIBASE_USER_PASSWORD"),
                dsn=get_dsn(test),
                min=5,
                max=5,
                increment=0,
            )
            PolibaseApi.pool_map[test] = pool
        else:
            pool = PolibaseApi.pool_map[test]
        return pool

    @staticmethod
    @contextmanager
    def get_connection(
        test: bool | None = TEST,
        poolled: bool = True,
        use_events: bool = False,
        catch_exception: bool = False,
    ):
        connection: Any = None
        test = test or TEST
        if poolled:
            try:
                pool: SessionPool = PolibaseApi.get_pool(test)
                try:
                    connection = pool.acquire()
                    yield connection
                except DatabaseError as exception:
                    A.ER.global_except_hook(exception)
                    if catch_exception:
                        raise exception
                finally:
                    if nn(connection):
                        pool.release(connection)
            except DatabaseError as exception:
                A.ER.global_except_hook(exception, get_host(test), A.D.map(lambda item: item.message, exception.args))  # type: ignore
                if catch_exception:
                    raise Error(exception.args[0].message)
        else:
            yield oracledb.connect(
                user=A.D_V_E.value("POLIBASE_USER_LOGIN"),
                password=A.D_V_E.value("POLIBASE_USER_PASSWORD"),
                dsn=get_dsn(False),
                events=use_events,
            )

    @staticmethod
    @contextmanager
    def get_connection_and_cursor(test: bool | None = TEST):
        test = A.D.triple_bool(test, test, test, TEST)
        with PolibaseApi.get_connection(test) as connection:
            with connection.cursor() as cursor:
                yield (connection, cursor)

    @staticmethod
    @contextmanager
    def get_cursor(
        test: bool | None = TEST,
        catch_exception: bool = False,
        autocommit: bool = False,
    ):
        with PolibaseApi.get_connection(
            test, catch_exception=catch_exception
        ) as connection:
            if autocommit:
                connection.autocommit = True
            with connection.cursor() as cursor:
                yield cursor

    @staticmethod
    def get_full_name_field(use_alias: bool = True) -> str:
        return js(
            (
                j(PolibaseApi.get_full_name_field_list(), " || ' ' || "),
                esc(A.CT_FNC.FULL_NAME) if use_alias else "",
            )
        )

    @staticmethod
    def get_full_name_field_list() -> list[str]:
        return A.D.map(
            lambda item: j((PERSON_PREFIX, item, "_", NAME)), ["las", "fir", "sec"]
        )  # type: ignore

    @staticmethod
    def get_person_extended_field_list() -> list[str]:
        return PolibaseApi.get_person_field_list() + [
            js((PERSON_BIRTH, esc(A.CT_FNC.BIRTH))),
            js((PERSON_REGISTRATION_DATE, esc(A.CT_FNC.REGISTRATION_DATE))),
        ]

    @staticmethod
    def get_person_field_list(use_full_name_alias: bool = True) -> list[str]:
        return [
            PolibaseApi.get_person_pin_field(),
            PolibaseApi.get_full_name_field(use_full_name_alias),
            js((PERSON_NOTES, esc(A.CT_FNC.COMMENT))),
            PolibaseApi.get_person_chart_folder_field(),
            PolibaseApi.get_person_email_field(),
            PolibaseApi.get_person_barcode_field(),
        ] + PolibaseApi.get_person_telephone_numbers_field_list()

    @staticmethod
    def get_note_emailed_field_list() -> list[str]:
        return [
            js((NOTE_NO, esc(A.CT_FNC.ID))),
            js(
                (
                    j((NOTE_PREFIX, PERSON_NO)),
                    esc(A.CT_FNC.PERSON_PIN),
                )
            ),
        ]

    @staticmethod
    def get_note_field_list() -> list[str]:
        return [js((j((NOTE_PREFIX, NUMBER)), esc(A.CT_FNC.ID)))]

    @staticmethod
    def get_person_barcode_field() -> str:
        return js((PERSON_BARCODE, esc(A.CT_FNC.BARCODE)))

    @staticmethod
    def get_person_email_field() -> str:
        return js((PERSON_EMAIL, esc(A.CT_FNC.EMAIL)))

    @staticmethod
    def get_person_pin_field() -> str:
        return js((PERSON_NO, esc(A.CT_FNC.PIN)))

    @staticmethod
    def get_note_emailed_field() -> str:
        return js((NOTE_EMAILED, esc(A.CT_FNC.EMAILED)))

    @staticmethod
    def get_person_chart_folder_field() -> str:
        return js(
            (
                PERSON_CARD_REGISTRY_FOLDER,
                esc(A.CT_FNC.CARD_REGISTRY_FOLDER),
            )
        )

    @staticmethod
    def get_person_telephone_numbers_field_list() -> list[str]:
        return [
            js(
                (
                    j((PERSON_TELEPHONE_NUMBER, index + 1)),
                    esc(j((A.CT_FNC.TELEPHONE_NUMBER, index + 1 if index > 0 else ""))),
                )
            )
            for index in range(4)
        ]

    @staticmethod
    def get_person_by_pin(value: int, test: bool | None = None) -> dict[str, Any]:
        return one(PolibaseApi.get_person_list_by_pin([value], test))  # type: ignore

    @staticmethod
    def get_person_by_email(value: str, test: bool | None = None) -> dict[str, Any]:
        return one(PolibaseApi.get_person_by_email(value, test))  # type: ignore

    @staticmethod
    def get_person_by_rowid(value: str, test: bool | None = None) -> dict[str, Any]:
        return one(PolibaseApi.get_person_list_by_rowid([value], test))  # type: ignore

    @staticmethod
    def get_note_emailed_by_rowid(
        value: str, test: bool | None = None
    ) -> dict[str, Any]:
        return one(PolibaseApi.get_note_emailed_list_by_rowid([value], test))  # type: ignore

    @staticmethod
    def get_person_saldo_by_rowid(
        value: str, test: bool | None = None
    ) -> dict[str, Any]:
        return one(PolibaseApi.get_person_saldo_list_by_rowid([value], test))  # type: ignore

    @staticmethod
    def search_person_visits(
        value: PolibasePersonVisitSearchCritery, test: bool | None = None
    ) -> list[PolibasePersonVisit]:
        return PolibaseApi.query_person_visits_with_condition(
            PolibaseApi.get_condition_string(value), test
        )

    @staticmethod
    def get_bonus_list(
        person_pin: int, test: bool | None = None
    ) -> list[dict[str, float]]:
        result_data: list[dict[str, int | float]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            result_data = PolibaseApi.fill_data(
                cursor.execute(
                    PolibaseApi.get_person_saldo_query_with_condition(
                        for_cqn=False,
                        value=js(
                            (
                                j((PATIENT_SALDO_PREFIX, PERSON_NO)),
                                "=",
                                person_pin,
                            )
                        ),
                    )
                ),
                cursor.description,  # type: ignore
            )  # type: ignore
            return result_data

    @staticmethod
    def get_condition_string(search_critery: Any = None) -> str:
        result: str = ""
        if search_critery is not None:
            condition_part_list: list[str] = []
            field_value: Any = None
            field_value_string: str | None = None
            compare_sign: str | None = None
            for field_name in search_critery.__dataclass_fields__:
                field_value = search_critery.__getattribute__(field_name)
                if field_value is not None:
                    if isinstance(field_value, list):
                        field_value_string = A.D.list_to_string(
                            field_value, separator=", ", start="(", end=")"
                        )
                        compare_sign = "in"
                    else:
                        compare_sign = "="
                        field_value_string = str(field_value)
                        if field_name.lower().find(A.CT_FNC.DATE.lower()) != -1:
                            if field_value_string == "":
                                compare_sign = "is"
                                field_value_string = "NULL"
                            else:
                                if field_value_string.find(" ") == -1:
                                    field_name = j(("TO_DATE({", field_name, ")"))
                                field_value_string = j(
                                    (
                                        "TO_DATE(",
                                        escs(field_value_string),
                                        "'DD.MM.YYYY')",
                                    )
                                )

                        else:
                            if isinstance(field_value, str):
                                for sign in ["!=", "<>", ">=", "<=", ">", "<"]:
                                    if field_value.startswith(sign):
                                        compare_sign = sign
                                        field_value = field_value[len(sign) :]
                                        break
                                field_value_string = escs(field_value)
                    condition_part_list.append(
                        js((field_name, compare_sign, field_value_string))
                    )
            if len(condition_part_list) > 0:
                result = js(("where", j(condition_part_list, " and ")))
        return result

    @staticmethod
    def escape_ansi(line):
        ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
        return ansi_escape.sub("", line)

    @staticmethod
    def query_person_visits_with_condition(
        value: str, test: bool | None = None
    ) -> list[PolibasePersonVisit]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            query_string: str = (
                f"select {VISIT_NO} {esc(A.CT_FNC.ID)}, {VISIT_PATIENT_NO} {esc(A.CT_FNC.PIN)}, {VISIT_PATIENT_FULL_NAME} {esc(A.CT_FNC.FULL_NAME)}, DOC.{PERSON_FULL_NAME} {esc(A.CT_FNC.DOCTOR_FULL_NAME)}, {VISIT_PATIENT_TELEPHONE_NUMBER} {esc(A.CT_FNC.TELEPHONE_NUMBER)}, {VISIT_PATIENT_REGISTRATION_DATE} {esc(A.CT_FNC.REGISTRATION_DATE)}, {VISIT_DATE_PS} {esc(A.CT_FNC.BEGIN_DATE)}, {VISIT_DATE_PF} {esc(A.CT_FNC.COMPLETE_DATE)}, {VISIT_DATE_FS} {esc(j((A.CT_FNC.BEGIN_DATE, '2')))}, {VISIT_DATE_FF} {esc(j((A.CT_FNC.COMPLETE_DATE, '2')))}, {VISIT_PATIENTS_STATUS} {esc(A.CT_FNC.STATUS)}, {VISIT_CABINET_NO} {esc(A.CT_FNC.CABINET_ID)}, {VISIT_DOCTOR_NO} {esc(A.CT_FNC.DOCTOR_ID)}, DOC.{PERSON_FULL_NAME} {esc(A.CT_FNC.DOCTOR_FULL_NAME)} from {PERSON_VISIT_TABLE_NAME} inner join {PERSON_TABLE_NAME} DOC on {VISIT_DOCTOR_NO} = DOC.{PERSON_NO} {value}"
            )
            result = PolibaseApi.fill_data(
                cursor.execute(query_string), cursor.description
            )  # type: ignore
        return A.D.fill_data_from_list_source(PolibasePersonVisit, result)

    @staticmethod
    def execute_query(value: str, test: bool | None = None) -> list[dict]:
        result: list[dict] = []
        with PolibaseApi.get_cursor(
            test, catch_exception=True, autocommit=True
        ) as cursor:
            if value.lower().find(A.CT_P.DBMS_OUTPUT) != -1:
                dbms_result: str = ""
                cursor.callproc(j((A.CT_P.DBMS_OUTPUT, "enable"), "."))
                cursor.execute(value)
                chunk: int = 100
                mLine = cursor.arrayvar(str, chunk)
                mNumLines = cursor.var(int)
                mNumLines.setvalue(0, chunk)
                while True:
                    cursor.callproc(
                        j((A.CT_P.DBMS_OUTPUT, "get_lines"), "."), (mLine, mNumLines)
                    )
                    num_lines = int(mNumLines.getvalue())
                    lines = mLine.getvalue()[:num_lines]
                    for line in lines:
                        dbms_result = nl(js((dbms_result, line)))
                    if num_lines < chunk:
                        break
                return [{A.CT_P.DBMS_OUTPUT: dbms_result}]
            result = (
                PolibaseApi.fill_data(cursor.execute(value), cursor.description) or []
            )
        return result

    @staticmethod
    def get_person_visit_last_id(test: bool | None = None) -> int:
        result: int = 0
        with PolibaseApi.get_cursor(test) as cursor:
            cursor.execute(
                j(("select max(", VISIT_NO, "from", PERSON_VISIT_TABLE_NAME))
            )
            result = one(cursor.fetchone())  # type: ignore
        return result

    @staticmethod
    def get_person_pin_by_login(value: str, test: bool | None = None) -> int | None:
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                js(
                    (
                        "select * from",
                        USERS_TABLE_NAME,
                        "where",
                        j((USER_PREFIX, A.CT_UP.NAME)),
                        "=",
                        escs(value),
                    )
                )
            )
            result: dict = one(PolibaseApi.fill_data(fetch_result, cursor.description))
            if n(result):
                return None
            return result[j((USER_PREFIX, PERSON_NO)).upper()]

    @staticmethod
    def get_polibase_person_user_login_and_worstation_name_pair_list(
        test: bool | None = None,
    ) -> list[tuple[str, str]]:
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                js(
                    (
                        "select distinct s.osuser",
                        esc(A.CT_FNC.LOGIN),
                        ",",
                        "s.terminal",
                        esc(A.CT_FNC.WORKSTATION_NAME),
                        "from",
                        "v$session s WHERE s.terminal not in ('unknown', 'FMVPOLIBASE1')",
                    )
                )
            )
            result_data: list[dict[str, str]] = PolibaseApi.fill_data(
                fetch_result, cursor.description
            )
            result: list[tuple[str, str]] = []
            for item in result_data:
                pair = A.D.to_list(item)
                result.append((pair[0], pair[1]))
            return result

    @staticmethod
    def get_person_list_by_name(
        value: str, test: bool | None = None
    ) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_person_query_with_condition(
                    j(
                        (
                            "lower(",
                            PERSON_FULL_NAME,
                            ") like ",
                            escs(j((value.lower(), "%"))),
                        )
                    )
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_person_list_by_pin(
        value: list[int], test: bool | None = None
    ) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_person_query_with_condition(
                    js(
                        (
                            PERSON_NO,
                            "in",
                            A.D.list_to_string(value, start="(", end=")"),
                        )
                    )
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_person_list_by_rowid(
        value: list[str], test: bool | None = None
    ) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_person_query_with_condition(
                    js(
                        (
                            ROWID,
                            "in",
                            A.D.list_to_string(value, True, start="(", end=")"),
                        )
                    )
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_note_emailed_list_by_rowid(
        value: list[str], test: bool | None = None
    ) -> list[dict[str, int]]:
        result: list[dict] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_note_emailed_query_with_condition(
                    js(
                        (
                            ROWID,
                            "in",
                            A.D.list_to_string(value, True, start="(", end=")"),
                        )
                    )
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_person_saldo_list_by_rowid(
        value: list[str], test: bool | None = None
    ) -> list[dict[str, int]]:
        result: list[dict] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_person_saldo_query_with_condition(
                    for_cqn=True,
                    value=js(
                        (
                            ROWID,
                            "in",
                            A.D.list_to_string(value, True, start="(", end=")"),
                        )
                    ),
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_person_list_by_telephone_number(
        value: str, index: int = 1, test: bool | None = None
    ) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_person_query_with_condition(
                    j((PERSON_TELEPHONE_NUMBER, index, " = ", escs(value)))
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_person_by_email(
        value: str, test: bool | None = None
    ) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_person_query_with_condition(
                    j((PERSON_EMAIL, "=", escs(value)))
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_person_list_in_card_registry_folder(
        name: str, test: bool | None = None
    ) -> list[dict[str, Any]]:
        name = name.lower()
        name = A.D.translit(name, "ru")
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                PolibaseApi.get_person_query_with_condition(
                    (
                        f"lower({PERSON_CARD_REGISTRY_FOLDER}) = {escs(name)} order by {PERSON_FULL_NAME}"
                    )
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def set_person_barcode_by_pin(
        value: str, pin: int, test: bool | None = None
    ) -> bool:
        return PolibaseApi.set_person_parameter_by_pin(PERSON_BARCODE, value, pin, test)

    @staticmethod
    def set_person_email_by_pin(value: str, pin: int, test: bool | None = None) -> bool:
        return PolibaseApi.set_person_parameter_by_pin(PERSON_EMAIL, value, pin, test)

    @staticmethod
    def set_person_telephone_number_by_pin(
        index: int, value: str, pin: int, test: bool | None = None
    ) -> bool:
        return PolibaseApi.set_person_parameter_by_pin(
            j((PERSON_TELEPHONE_NUMBER, index + 1)), value, pin, test
        )

    @staticmethod
    def set_person_parameter_by_pin(
        name: str, value: str, pin: int, test: bool | None = None
    ) -> bool:
        return PolibaseApi.execute_update_query(
            js(
                (
                    PERSON_TABLE_NAME,
                    "set",
                    name,
                    "=",
                    escs(value),
                    "where",
                    PERSON_NO,
                    "=",
                    pin,
                )
            ),
            test,
        )

    @staticmethod
    def set_new_format_barcode_for_all_person(test: bool | None = None) -> bool:
        def get_barcode_field_value() -> str:
            return js(
                (
                    escs(A.CT_P.BARCODE.NEW_PREFIX),
                    "||",
                    PERSON_NO,
                    "||",
                    escs(j((".", A.CT_P.BARCODE.PERSON.IMAGE_FORMAT))),
                )
            )

        return PolibaseApi.execute_update_query(
            js(
                (
                    PERSON_TABLE_NAME,
                    "set",
                    PERSON_BARCODE,
                    "=",
                    get_barcode_field_value(),
                )
            ),
            test,
        )

    @staticmethod
    def fill_data(
        data: Cursor, description: list | None
    ) -> list[dict[str, Any]] | None:
        if n(description):
            return None
        result: list[dict[str, Any]] = []
        field_list: list = []
        for description_iten in description:
            field_list.append(description_iten[0])
        for data_item in data:
            result_item: dict = {}
            for index, row_item in enumerate(data_item):
                result_item[field_list[index]] = row_item
            result.append(result_item)
        return result

    @staticmethod
    def get_barcode_by_pin(pin: int, test: bool | None = None) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                f"select {PolibaseApi.get_person_pin_field()}, {PolibaseApi.get_person_barcode_field()} from {PERSON_TABLE_NAME} where {PERSON_NO}=: pin",
                pin=pin,
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def get_person_pin_list_with_old_format_barcode(
        test: bool | None = None,
    ) -> list[int]:
        result: list[int] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                f"select {PERSON_NO} from {PERSON_TABLE_NAME} where {PERSON_BARCODE} not like '{A.CT_P.BARCODE.NEW_PREFIX}%' or {PERSON_BARCODE} is NULL"
            )
            for item in fetch_result:
                result.append(item[0])
        return result

    @staticmethod
    def get_all_barcodes(test: bool | None = None) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result: Any = cursor.execute(
                js(
                    (
                        "select",
                        PolibaseApi.get_person_pin_field(),
                        PolibaseApi.get_person_barcode_field(),
                        "from",
                        PERSON_TABLE_NAME,
                    )
                )
            )
            result = PolibaseApi.fill_data(fetch_result, cursor.description)
        return result

    @staticmethod
    def set_card_folder_name_for_person(
        chart_folder: str, pin: int, test: bool | None = None
    ) -> bool:
        return PolibaseApi.execute_update_query(
            js(
                (
                    PERSON_TABLE_NAME,
                    "set",
                    PERSON_CARD_REGISTRY_FOLDER,
                    "=",
                    escs(chart_folder),
                    "where",
                    PERSON_NO,
                    "=",
                    pin,
                )
            ),
            test,
        )

    @staticmethod
    def execute_update_query(value: str, test: bool | None = None) -> bool:
        with PolibaseApi.get_connection_and_cursor(test) as (connection, cursor):
            cursor.execute(js(("update", value)))
            connection.commit()
            return cursor.rowcount > 0

    @staticmethod
    def get_person_query_with_condition(
        value: str | None = None, fields: list[str] | None = None
    ) -> str:
        if e(value):
            value = ""
        else:
            value = js(("where", value))
        return js(
            (
                "select",
                j(fields or PolibaseApi.get_person_extended_field_list(), ", "),
                "from",
                PERSON_TABLE_NAME,
                value,
            )
        )

    @staticmethod
    def get_note_emailed_query_with_condition(
        value: str | None = None, fields: list[str] | None = None
    ) -> str:
        if e(value):
            value = ""
        else:
            value = js(("where", value))
        return js(
            (
                "select",
                j(fields or PolibaseApi.get_note_emailed_field_list(), ", "),
                "from",
                NOTE_EMAILED_TABLE_NAME,
                value,
            )
        )

    @staticmethod
    def get_note_query_with_condition(
        value: str | None = None, fields: list[str] | None = None
    ) -> str:
        if e(value):
            value = ""
        else:
            value = js(("where", value))
        return js(
            (
                "select",
                j(fields or PolibaseApi.get_note_field_list(), ", "),
                "from",
                NOTE_TABLE_NAME,
                value,
            )
        )

    @staticmethod
    def get_person_query(fields: list[str] | None = None) -> str:
        return PolibaseApi.get_person_query_with_condition(None, fields)

    @staticmethod
    def drop_person_bonus_by_id(value: int) -> bool:
        return PolibaseApi.execute_update_query(
            js(
                (
                    PATIENT_SALDO_TABLE,
                    "set",
                    j((PATIENT_SALDO_PREFIX, BONUS_PLUS)),
                    "=",
                    0,
                    "where",
                    j((PATIENT_SALDO_PREFIX, NUMBER)),
                    "=",
                    value,
                )
            ),
        )

    @staticmethod
    def get_person_saldo_query_with_condition(
        for_cqn: bool,
        value: str | None = None,
    ) -> str:
        if e(value):
            value = ""
        else:
            value = js(("where", value))
        return js(
            (
                "select",
                j(
                    A.D.map(
                        lambda item: j((PATIENT_SALDO_PREFIX, item)),
                        [
                            js((NUMBER, esc(A.CT_FNC.ID))),
                            js((PERSON_NO, esc(A.CT_FNC.PERSON_PIN))),
                            js(("POI_OUT", esc("bonus_minus"))),
                            js((BONUS_PLUS, esc("bonus_plus"))),
                            js(("SUM_SAL", esc("money"))),
                            js(("DOC_NO", esc(A.CT_FNC.DOCTOR_ID))),
                        ],
                    ),  # type: ignore
                    ", ",
                ),
                None if for_cqn else js((",", j((PATIENT_SALDO_TABLE, ".*")))),
                "from",
                PATIENT_SALDO_TABLE,
                value,
                None if for_cqn else "order by psa_date desc",
            )
        )

    @staticmethod
    def get_note_emailed_query(fields: list[str] | None = None) -> str:
        return PolibaseApi.get_note_emailed_query_with_condition(None, fields)

    @staticmethod
    def get_person_registrator_by_pin(
        value: int, test: bool | None = None
    ) -> dict[str, Any]:
        result: list[dict] = []
        with PolibaseApi.get_cursor(test) as cursor:
            query_string: str = PolibaseApi.get_person_query_with_condition(
                f"{PERSON_NO} = (select {PERSON_REGISTRATOR_NO} from {PERSON_TABLE_NAME} where {PERSON_NO} = {value})"
            )
            result = PolibaseApi.fill_data(
                cursor.execute(query_string), cursor.description
            )  # type: ignore
        return one(result, {})  # type: ignore

    @staticmethod
    def get_person_operator_by_pin(
        value: int, test: bool | None = None
    ) -> dict[str, Any]:
        result: list[dict] = []
        with PolibaseApi.get_cursor(test) as cursor:
            query_string: str = PolibaseApi.get_person_query_with_condition(
                f"{PERSON_NO} = (select {PERSON_OPERATOR_NO} from {PERSON_TABLE_NAME} where {PERSON_NO} = {value})"
            )
            result = PolibaseApi.fill_data(
                cursor.execute(query_string), cursor.description
            )  # type: ignore
        return one(result, {})  # type: ignore

    @staticmethod
    def get_person_pin_list_by_visit_date(
        date: str, only_operation_department: bool = False, test: bool | None = None
    ) -> list[int]:
        complete_list_part: str = """
                            OJBS_COMPLETE_LIST as (
                            select
                            DIV_NAME,
                            DIV_NOTES DEPARTMENT,
                            JOB_NO,
                            JOB_NAME,
                            ORD_PAT_NO,
                            PATIENT.PER_FULL_NAME,
                            PATIENT.PER_NO,
                            OJB_DOC_NO as DOC_NO,
                            DOCTOR.PER_FULL_NAME as DOCTOR,
                            OJB_MED_NO as MED_NO,
                            DOCTOR.PER_PLI_NO as DOC_PLI_NO,
                            OJB_NO,
                            OJB_ORD_NO ORDER_NO,
                            ORD_STRT CREATE_AT,
                            ORD_PAID PAID_AT,
                            ORD_TOTAL_PRICE TOTAL_PRICE,
                            OJB_JOB_PRC,
                            OJB_JOB_QNT,
                            OJB_JOB_KO,
                            OJB_DOC_PRC DOC_RATE,
                            OJB_MED_PRC MED_RATE,
                            JSL_COST_DOC,
                            JSL_NO,
                            JSL_TRF_NO
                            from DIVS_ALL
                            left outer join JOBLISTS on JLI_DIV_NO=DIV_NO
                            left outer join JOBLIS on JIL_JLI_NO=JLI_NO
                            left outer join JOBS on JIL_JOB_NO=JOB_NO
                            left outer join OJBS on OJB_JOB_NO=JOB_NO
                            left outer join PERSONS DOCTOR on OJB_DOC_NO=DOCTOR.PER_NO
                            left outer join PERSONS PATIENT on OJB_PAT_NO=PATIENT.PER_NO
                            left outer join JOBSALS ON JSL_JOB_NO=OJB_JOB_NO and DOCTOR.PER_PLI_NO=JSL_PLI_NO
                        )
                        """

        pin_list: list[int] = A.S.get(
            A.CT_S.POLIBASE_PERSON_REVIEW_NOTIFICATION_DOCTOR_PERSON_PIN_LIST
        )
        query: str = js(
            (
                (
                    j(
                        (
                            """with DIVS_ALL as (
                            select DIV_NO, DIV_NAME, DIV_NOTES from DIVISIONS where DIV_NOTES is not NULL
                            start with DIV_NO=(select DIV_NO from DIVISIONS where DIV_NAME like '%Операционный блок%')
                            connect by prior DIV_NO=DIV_DIV_NO
                        ),
                        OJBS as (
                            select * from ORDJOB
                            inner join ORDERS on OJB_ORD_NO=ORD_NO
                            where OJB_ORD_NO not in (
                                select ORD_NO from ORDERS
                                inner join DIVISIONS on ORD_DIV_NO=DIV_NO
                                where DIV_NAME like 'Скорая помощь ПИКВ'
                            ) and OJB_NO is not NULL
                        ),""",
                            complete_list_part,
                            """select distinct
                        PER_NO
                        from OJBS_COMPLETE_LIST
                        where
                        (DEPARTMENT not like '%---%---%' or DEPARTMENT is NULL)""",
                        )
                    )
                    if only_operation_department
                    else j(
                        (
                            """with DIVS_POLY as (
                            select DIV_NO, DIV_NAME, DIV_NOTES from DIVISIONS where DIV_NOTES is not NULL
                            start with DIV_NO=(select DIV_NO from DIVISIONS where DIV_NAME like 'ПОЛИКЛИНИКА')
                            connect by prior DIV_NO=DIV_DIV_NO
                            union all
                            select DIV_NO, DIV_NAME, DIV_NOTES from DIVISIONS where DIV_NAME like 'АНАЛИЗЫ ФАЛЬК'
                            ),
                            DIVS_IVF as (
                                select DIV_NO, DIV_NAME, DIV_NOTES from DIVISIONS where DIV_NOTES is not NULL
                                start with DIV_NO=(select DIV_NO from DIVISIONS where DIV_NAME like 'ВРТ')
                                connect by prior DIV_NO=DIV_DIV_NO
                            ),
                            DIVS_DIAG as (
                                select DIV_NO, DIV_NAME, DIV_NOTES from DIVISIONS where DIV_NOTES is not NULL
                                start with DIV_NO=(select DIV_NO from DIVISIONS where DIV_NAME like 'Диагностическое Отделение%')
                                connect by prior DIV_NO=DIV_DIV_NO
                            ),
                            DIVS_INPAT as (
                                select DIV_NO, DIV_NAME, DIV_NOTES from DIVISIONS where DIV_NOTES is not NULL
                                start with DIV_NO=(select DIV_NO from DIVISIONS where DIV_NAME like 'Стационар%')
                                connect by prior DIV_NO=DIV_DIV_NO
                            ),
                            DIVS_AnE as (
                                select DIV_NO, DIV_NAME, DIV_NOTES from DIVISIONS where DIV_NOTES is not NULL
                                start with DIV_NO=(select DIV_NO from DIVISIONS where DIV_NAME like 'Отделение Неотложной помощи%')
                                connect by prior DIV_NO=DIV_DIV_NO
                            ),
                            DIVS_ALL as (
                                select * from DIVS_POLY
                                union all
                                select * from DIVS_IVF
                                union all
                                select * from DIVS_DIAG
                                union all
                                select * from DIVS_INPAT
                                union all
                                select * from DIVS_AnE
                            ),
                            OJBS as (
                                select * from ORDJOB
                                inner join ORDERS on OJB_ORD_NO=ORD_NO
                                where OJB_ORD_NO not in (
                                    select ORD_NO from ORDERS
                                    inner join DIVISIONS on ORD_DIV_NO=DIV_NO
                                    where DIV_NAME like 'Скорая помощь ПИКВ'
                                ) and OJB_NO is not NULL
                            ),
                        """,
                            complete_list_part,
                            "select distinct PER_NO from OJBS_COMPLETE_LIST where (DEPARTMENT not like '%---%---%' or DEPARTMENT is NULL)",
                        )
                    )
                ),
                (
                    None
                    if only_operation_department or e(pin_list)
                    else j(
                        (
                            "and DOC_NO IN(",
                            A.D.list_to_string(A.D.map(str, pin_list)),
                            ")",
                        )
                    )
                ),
                " and CREATE_AT like TO_DATE(",
                escs(date),
                ", 'DD.MM.YY')",
            )
        )
        result: list[int] = []
        with PolibaseApi.get_cursor(test) as cursor:
            fetch_result = cursor.execute(query)
            for item in fetch_result:
                result.append(item[0])
        return result

    @staticmethod
    def update_person_change_date(person_pin: int, person_registrator_pin: int) -> bool:
        return PolibaseApi.execute_update_query(
            js(
                (
                    PERSON_TABLE_NAME,
                    "set per_ope_no =",
                    person_registrator_pin,
                    ", per_change_date=to_date(",
                    escs(A.D.now_to_string(A.CT.DATETIME_FORMAT)),
                    ",",
                    escs(A.CT_P.DATETIME_FORMAT),
                    ") where per_no =",
                    person_pin,
                )
            )
        )
