from pytest import mark as m

from pista.root import PISTA_DIR
from pista.core._root_manager import PISTA_CONFIG, PROJECT_ROOT_DIR, OUTPUT_DIR, SCREENSHOT_DIR
from pista.core._config_manager import ENV_CONFIG, ENV_CONST

from pista.core._log_manager import Logging, printit
from pista.core._test_enhancer import *
from pista.conftest import *


class TestBase:
    pass


# def logger_init(name):
#     logger = Logging.get(name)
#     return logger
