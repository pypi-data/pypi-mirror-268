import ipih

from pih import A
from pih.tools import j
from pih.consts import CONST
from pih.collections.service import ServiceDescription

NAME: str = "Polibase"

VERSION: str = "0.15"

HOST = A.CT_H.POLIBASE

PACKAGES: tuple[str, ...] = ("oracledb",)

SD: ServiceDescription = ServiceDescription(
    name=NAME,
    host=HOST.NAME,
    run_from_system_account=True,
    description="Polibase service",
    commands=(
        "get_polibase_person_by_pin",
        "get_polibase_persons_by_pin",
        "get_polibase_persons_by_telephone_number",
        "get_polibase_persons_by_full_name",
        "get_polibase_persons_by_card_registry_folder_name",
        "get_polibase_person_registrator_by_pin",
        "get_polibase_person_pin_list_with_old_format_barcode",
        #
        "get_polibase_persons_pin_by_visit_date",
        #
        "search_polibase_person_visits",
        "get_polibase_person_visits_last_id",
        #
        "set_polibase_person_card_folder_name",
        "set_polibase_person_email",
        "set_barcode_for_polibase_person",
        "check_polibase_person_card_registry_folder_name",
        "set_polibase_person_telephone_number",
        "get_polibase_person_operator_by_pin",
        "get_polibase_person_by_email",
        "update_person_change_date",
    ),
    python_executable_path=CONST.UNKNOWN,
    standalone_name="plb",
    use_standalone=True,
    packages=PACKAGES,
    version=VERSION
)

TEST: bool = False
#
NUMBER: str = "no"
#
NOTE_PREFIX: str = "note_"
PERSON_PREFIX: str = "per_"
VISIT_PREFIX: str = "vis_"
PATIENT_PREFIX: str = "pat_"
USER_PREFIX: str = "use_"
PATIENT_SALDO_PREFIX: str = "psa_"
#
PERSON_TABLE_NAME: str = "persons"
NOTE_EMAILED_TABLE_NAME: str = "notes_emailed"
NOTE_TABLE_NAME: str = "notes"
PERSON_VISIT_TABLE_NAME: str = "visits"
USERS_TABLE_NAME: str = "users"
PATIENT_SALDO_TABLE: str = "patsaldo"
#
ROWID: str = "rowid"
REGISTRATION_DATE: str = "reg_date"
PERSON_BARCODE: str = f"{PERSON_PREFIX}bar"
PERSON_CHANGE_DATE: str = f"{PERSON_PREFIX}change_date"
PERSON_CARD_REGISTRY_FOLDER: str = f"{PERSON_PREFIX}staff_code"
PERSON_FULL_NAME: str = f"{PERSON_PREFIX}full_name"
PERSON_NO: str = f"{PERSON_PREFIX}{NUMBER}"
PERSON_REGISTRATOR_NO: str = f"{PERSON_PREFIX}reg_{NUMBER}"
PERSON_OPERATOR_NO: str = f"{PERSON_PREFIX}ope_{NUMBER}"
PERSON_EMAIL: str = f"{PERSON_PREFIX}{A.CT_FNC.EMAIL}"
PERSON_TELEPHONE_NUMBER: str = f"{PERSON_PREFIX}phone"
PERSON_BIRTH: str = f"{PERSON_PREFIX}birth"
PERSON_NOTES: str = f"{PERSON_PREFIX}notes"
PERSON_REGISTRATION_DATE: str = f"{PERSON_PREFIX}{REGISTRATION_DATE}"
#
NOTE_NO: str = f"{NOTE_PREFIX}{NUMBER}"
NOTE_EMAILED: str = f"{NOTE_PREFIX}{A.CT_FNC.EMAILED}"
#
NAME: str = "name"
VISIT_NO: str = f"{VISIT_PREFIX}{NUMBER}"
VISIT_DATE_PREFFIX: str = f"{VISIT_PREFIX}date_"
VISIT_DATE_PS: str = f"{VISIT_DATE_PREFFIX}ps"
VISIT_DATE_PF: str = f"{VISIT_DATE_PREFFIX}pf"
VISIT_DATE_FS: str = f"{VISIT_DATE_PREFFIX}fs"
VISIT_DATE_FF: str = f"{VISIT_DATE_PREFFIX}ff"
VISIT_PATIENT_NO: str = f"{VISIT_PREFIX}{PATIENT_PREFIX}{NUMBER}"
VISIT_PATIENT_FULL_NAME: str = j((VISIT_PREFIX, PATIENT_PREFIX, NAME))
VISIT_PATIENT_TELEPHONE_NUMBER: str = f"{VISIT_PREFIX}place"
VISIT_PATIENT_REGISTRATION_DATE: str = f"{VISIT_PREFIX}{REGISTRATION_DATE}"
VISIT_PATIENTS_STATUS: str = f"{VISIT_PREFIX}vst_{NUMBER}"
VISIT_CABINET_NO: str = f"{VISIT_PREFIX}cab_{NUMBER}"
VISIT_DOCTOR_NO: str = f"{VISIT_PREFIX}doc_{NUMBER}"
#
BONUS_PLUS: str = "POI_INN"
