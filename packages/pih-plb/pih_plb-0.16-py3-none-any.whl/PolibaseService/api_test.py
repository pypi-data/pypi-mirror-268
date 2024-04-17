import cx_Oracle
import re
import importlib.util
import sys

pih_is_exists = importlib.util.find_spec("pih") is not None
if not pih_is_exists:
    sys.path.append("//pih/facade")
from pih import A
from pih.tools import DateTimeTool
from pih.consts import FIELD_NAME_COLLECTION, CONST
from pih.collections import PolibasePersonVisitDS, PolibasePersonVisit, PolibasePersonVisitSearchCritery, User

from api import PolibaseApi as Api

print(Api.get_note_emailed_by_rowid("AAMzMUAAEAAAGmDAAA"))

'''connection = cx_Oracle.connect(user=A.CT_P.USER, password=A.CT_P.PASSWORD,
                  dsn=Api.get_dns(False),
                  events=True)


 def cqn_callback(message):
    print("Notification:")
    for query in message.queries:
        for tab in query.tables:
            print("Table:", tab.name)
            print("Operation:", tab.operation)
            for row in tab.rows:
                if row.operation & cx_Oracle.OPCODE_INSERT:
                    print("INSERT of rowid:", row.rowid)
                if row.operation & cx_Oracle.OPCODE_UPDATE:
                        person: dict = Api.get_person_by_rowid(row.rowid)
                        print("UPDATE of rowid:", row.rowid, person)


subscr = connection.subscribe(callback=cqn_callback,
                              operations=cx_Oracle.OPCODE_INSERT | cx_Oracle.OPCODE_UPDATE,
                              qos=cx_Oracle.SUBSCR_QOS_QUERY | cx_Oracle.SUBSCR_QOS_ROWIDS)

subscr.registerquery(Api.get_person_query_statement(Api.get_base_person_field_list(False)))
input("Hit enter to stop CQN demo\n") '''





