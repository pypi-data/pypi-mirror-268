# import time

import cx_Oracle

from pista.core._config_manager import PISTA_CONFIG
from pista.core._data_manager import DataHandler
from pista.core._log_manager import Logging, printit
from pista.core.db_service import DBService


class OraService(DBService):
    """ To connect to databases """
    logger = Logging.get(__qualname__)

    DB_CONNS = {}  # Dict of schemas name and db connection

    @classmethod
    def connect_db(cls, schema, user, pwd_en, host, service, port=15):
        ORA_CLIENT_DIRPATH = PISTA_CONFIG.get('db', 'oracle_instaclient_dirpath')
        OR_HOST = host
        OR_PORT = port
        OR_SERVICE = service
        OR_USER = user
        OR_PWD_EN = pwd_en
        _OR_PWD = DataHandler.decrypt_it(OR_PWD_EN)

        if schema not in cls.DB_CONNS.keys() or cls.DB_CONNS[schema] is None:
            printit('Connecting DB: ' + schema)

            try:
                cx_Oracle.init_oracle_client(lib_dir=ORA_CLIENT_DIRPATH)
                conn = cx_Oracle.connect(OR_USER + '/' + _OR_PWD + '@' + OR_HOST + ':' + OR_PORT + '/' + OR_SERVICE)
                conn.callTimeout = 1000 * 200  # DPI-1067: call timeout of 1000 ms exceeded with ORA-3156
                cls.DB_CONNS[schema] = conn
                DBService.store_connection(schema, conn)
            except cx_Oracle.DatabaseError as e:
                assert False, 'Exception during DB connection: ' + str(e)
            except Exception as e:
                assert False, 'Exception during DB connection: ' + str(e)

        return cls.DB_CONNS[schema]
