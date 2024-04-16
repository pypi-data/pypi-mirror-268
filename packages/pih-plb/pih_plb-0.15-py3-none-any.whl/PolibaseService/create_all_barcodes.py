import os
from api import PolibaseApi
from pih.const import CONST, FIELD_NAME_COLLECTION, PATHS
from pih.pih import PIH

log: bool = False
test: bool = False
PolibaseApi.TEST = test
update_polibase_db: bool = True
if not update_polibase_db or PolibaseApi.set_new_format_barcode_for_all_person():
    barcode_list: list = PolibaseApi.get_all_barcodes()
    length: int = len(barcode_list)
    for index, barcode_item in enumerate(barcode_list):
        pin: int = barcode_item[FIELD_NAME_COLLECTION.PIN]
        barcode: str = barcode_item[FIELD_NAME_COLLECTION.BARCODE]
        person_folder: str = PATHS.POLIBASE.person_folder(pin, test) 
        person_folder_is_exists: bool = os.path.isdir(person_folder)
        if person_folder_is_exists:
            if os.path.exists(os.path.join(person_folder, POLIBASE.BARCODE.get_file_name(pin, True))):
                if log:
                    print("Person already has new barcode image")
            else:
                PIH.ACTION.POLIBASE.create_barcode_for_person(pin, test)
        else:
            if log:
                print("Person folder is not exists")
        print(f"{index} / {length}")
