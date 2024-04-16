import os
# import sys
import shutil
import threading
import time
from datetime import datetime

import pytest

from pista.root import THREAD_DATA_TEMPLATE_FILE

_START_TIME = ''
_TRIGGERED_CMD = _TRIGGERED_ARGS = _TC_MARK = ''
_PISTA_CORE_VERSION = ''

_IS_A_PROJECT = False
_PROJECT_ROOT_DIR = _OUTPUT_DIR = _SCREENSHOT_DIR = _THREAD_DATA_RUNTIME_FILE = None
_IS_USE_THREAD_DATA_FILE = ''

_ENV = _BROWSER = None
_IS_WEB_BROWSER_INVOKED = False
_ALL_WEB_DRIVERS = ()

# Useful os.environ variables
os.environ['projectRootDirPath'] = ''
os.environ['env'] = ''


pytest_plugins = [
    "pista.plugins.pytest_reporter.plugin",
    "pista.plugins.pytest_reporter_html1.plugin",
    "pista.plugins.pytest_excel.pytest_excel"
]


def pytest_addoption(parser):
    # print('pista: pytest_addoption')

    parser.addoption('--env', action='store', default=_ENV)
    parser.addoption('--browser', action='store', default=_BROWSER)


# def _get_project_root_path(test_path):
#     project_root_path = ''
#     # _is_a_pista_project = True
#     #
#     # parts = str(test_path).split(os.path.sep)
#     # try:
#     #     index = parts.index('tests')
#     #     project_root_path = os.path.sep.join(parts[:index - 1])
#     #     _is_a_pista_project = True
#     # except ValueError:
#     #     project_root_path = ''
#     #     _is_a_pista_project = False
#
#     parts = str(test_path).split(os.path.sep)
#     _IS_A_PROJECT = True if 'pista' not in parts else False
#     if _IS_A_PROJECT:
#         index = parts.index('tests')
#         project_root_path = os.path.sep.join(parts[:index - 1])
#     else:
#         project_root_path = ''
#
#     return project_root_path, _IS_A_PROJECT


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # print('pista: pytest_configure')

    global _TRIGGERED_CMD, _TRIGGERED_ARGS
    global _OUTPUT_DIR, _SCREENSHOT_DIR, _THREAD_DATA_RUNTIME_FILE, _IS_USE_THREAD_DATA_FILE
    global _IS_A_PROJECT, _PROJECT_ROOT_DIR
    global _ENV
    global _PISTA_CORE_VERSION

    _TRIGGERED_CMD = ' '.join(config.invocation_params.args)
    os.environ['triggeredRunCmd'] = _TRIGGERED_CMD
    # print('conftest._TRIGGERED_CMD', _TRIGGERED_CMD)
    if 'addopts' in config.inicfg.keys():
        _TRIGGERED_ARGS = config.inicfg['addopts']
    total_workers = config.option.numprocesses or 1
    print(f"RunCmd: {_TRIGGERED_CMD}\nRunArgs: {_TRIGGERED_ARGS}\nThreads {total_workers}")

    from pista.core.common_service import Commons

    '''Check project_id dir setup'''
    print('PytestIni:', str(config.inipath))
    # _IS_A_PROJECT, _PROJECT_ROOT_DIR = Commons.get_project_dtls_from_arg(test_dir=_invokedDir)
    _IS_A_PROJECT, _PROJECT_ROOT_DIR = Commons.get_project_root_from_ini_path(ini_path=config.inipath)
    # print('conftest._IS_A_PROJECT', _IS_A_PROJECT, _PROJECT_ROOT_DIR)
    os.environ['projectRootDirPath'] = _PROJECT_ROOT_DIR

    '''Setup env'''
    from pista.core._root_manager import PISTA_CONFIG, REQUIREMENT_FILE
    from pista.core import _config_manager
    
    _defaultEnv = PISTA_CONFIG.get('framework', 'default_env')
    os.environ['env'] = _ENV = config.getoption('--env') or _defaultEnv
    _config_manager._set_env(_ENV, _IS_A_PROJECT, _PROJECT_ROOT_DIR)

    _PISTA_CORE_VERSION = Commons.get_line_in_file_startswith(REQUIREMENT_FILE, 'pista-core')
    print('PistaCore:', _PISTA_CORE_VERSION)
    
    if _IS_A_PROJECT:
        _OUTPUT_DIR = os.path.join(_PROJECT_ROOT_DIR, 'output')
        _SCREENSHOT_DIR = os.path.join(_OUTPUT_DIR, 'screenshot')
        _THREAD_DATA_RUNTIME_FILE = os.path.join(_OUTPUT_DIR, 'thread_data.xlsx')

        from pista.core._root_manager import PISTA_CONFIG, PROJECT_ID

        assert PROJECT_ID, "project_id not provided. Provide and rerun"
        assert os.path.exists(os.path.join(_PROJECT_ROOT_DIR, PROJECT_ID, 'apps')) \
               and os.path.exists(os.path.join(_PROJECT_ROOT_DIR, PROJECT_ID, 'resources')) \
               and os.path.exists(os.path.join(_PROJECT_ROOT_DIR, PROJECT_ID, 'tests')), \
            f"Root doesn't have dir {PROJECT_ID} with /apps, /resources or /tests. Resolve and rerun"

        '''Summary file path'''
        exlpath = os.path.join(_OUTPUT_DIR, 'summary.xlsx')
        config.option.excelpath = exlpath

        '''Report file path'''
        reportpath = os.path.join(_OUTPUT_DIR, 'report.html')
        if 'report' in config.option and type(config.option.report) is list:
            config.option.report[0] = reportpath

        '''Junit xml file path'''
        xmlpath = os.path.join(_OUTPUT_DIR, 'jreport.xml')
        config.option.xmlpath = xmlpath

        from pista.core._thread_data_handler import RuntimeXL

        '''Data handling'''
        RuntimeXL._IS_USE_THREAD_DATAFILE = _IS_USE_THREAD_DATA_FILE = PISTA_CONFIG.get('framework', 'is_use_thread_data_file')

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    # print('pista: pytest_sessionstart')

    global _START_TIME, _SCREENSHOT_DIR, _THREAD_DATA_RUNTIME_FILE, _IS_USE_THREAD_DATA_FILE

    if getattr(session.config, 'workerinput', None) is not None:
        # Master process has already executed rest of code
        time.sleep(20.0)
        return
    
    _START_TIME = datetime.today()

    if _IS_A_PROJECT:
        from pista.core.file_service import FileUtil
        from pista.core._root_manager import PISTA_CONFIG
        
        '''Setup output file/dir'''
        FileUtil.archive_outputs(_START_TIME)

        '''Create screenshot dir'''
        if not os.path.exists(_SCREENSHOT_DIR):
            os.makedirs(_SCREENSHOT_DIR)

        '''Copy thread data template file'''
        if 'true' in _IS_USE_THREAD_DATA_FILE:
            shutil.copy(THREAD_DATA_TEMPLATE_FILE, _THREAD_DATA_RUNTIME_FILE)

        '''Invoke yarn for xterm'''
        ssh_serv_provider = str(PISTA_CONFIG.get('ssh', 'ssh_service_provider'))
        is_run_yarn_flag = str(PISTA_CONFIG.get('ssh', 'is_run_yarn_for_xtermjs'))
        if 'xterm' in ssh_serv_provider and 'true' in is_run_yarn_flag:
            from pista.core.ssh_xtermjs_service import SshXtermService
            SshXtermService._start_node()


@pytest.fixture(scope='session', autouse=True)
def pista_session_setup(request, worker_id):
    # print('pista: pista_session_setup')

    global _ENV, _TRIGGERED_CMD, _TRIGGERED_ARGS, _TC_MARK
    global _IS_A_PROJECT, _PROJECT_ROOT_DIR
    global _PISTA_CORE_VERSION

    thread_id = threading.current_thread().native_id
    total_workers = os.environ.get('PYTEST_XDIST_WORKER_COUNT') or 1
    print(f"RunCmd: {_TRIGGERED_CMD}\nRunArgs: {_TRIGGERED_ARGS}\nPistaCore: {_PISTA_CORE_VERSION}"
          f"\nThreadId: {worker_id}/{thread_id} (Threads: {total_workers})")

    from pista.core.common_service import Commons
    # from pista.core._root_manager import PISTA_CONFIG
    # from pista.core import _config_manager
    from pista.core._thread_data_handler import RuntimeXL

    # _invokedDir = str(request.config.invocation_dir)
    # print('2 conftest.inipath', str(request.config.inipath))
    # _IS_A_PROJECT, _PROJECT_ROOT_DIR = Commons.get_project_dtls_from_arg(test_dir=_invokedDir)
    _IS_A_PROJECT, _PROJECT_ROOT_DIR = Commons.get_project_root_from_ini_path(ini_path=request.config.inipath)
    # print('conftest._IS_A_PROJECT', _IS_A_PROJECT, _PROJECT_ROOT_DIR)

    # '''Setup env'''
    # _defaultEnv = PISTA_CONFIG.get('framework', 'default_env')
    # os.environ['env'] = _ENV = request.config.getoption('--env') or _defaultEnv
    # _config_manager._set_env(_ENV, _IS_A_PROJECT, _PROJECT_ROOT_DIR)

    '''Capture test marker'''
    os.environ['tcMark'] = _TC_MARK = request.config.getoption('-m')
    print(f"TcMark: {_TC_MARK}")

    if _IS_A_PROJECT:
        '''Initialize thread data lock file status'''
        RuntimeXL.RUNTIME_FILE_LOCK_STAT[thread_id] = False
    
    yield

    _END_TIME = datetime.today()


@pytest.fixture(scope='module', autouse=True)
def pista_module_setup(request):
    # print('pista: pista_module_setup')

    global _ENV, _TRIGGERED_CMD, _TRIGGERED_ARGS, _TC_MARK
    global _PISTA_CORE_VERSION
    
    from pista.core.file_service import FileUtil
    from pista.core._log_manager import LOG_FILE_PATH
    from pista.core._thread_data_handler import RuntimeXL

    thread_id = threading.current_thread().native_id
    dtls_to_log = (f"\nRunCmd: {_TRIGGERED_CMD}\nRunArgs: {_TRIGGERED_ARGS}\nPistaCore: {_PISTA_CORE_VERSION}"
                   f"\nEnv: {_ENV} (Browser: {_BROWSER})\nTcMark: {_TC_MARK}\n\n")
    FileUtil.append_to_file(LOG_FILE_PATH.format(thread_id), dtls_to_log)

    if _IS_A_PROJECT:
        '''Clear thread data file'''
        if 'true' in RuntimeXL._IS_USE_THREAD_DATAFILE:
                RuntimeXL.createThreadLockFile()
                RuntimeXL.clearAllAttrForThread()
                RuntimeXL.removeThreadLockFile()

    yield 


@pytest.fixture(scope='class')
def invoke_driver(invoke_web_driver):
    pass


@pytest.fixture(scope='class')
def invoke_web_driver(request):
    # print('pista: invoke_web_driver')
    
    global _BROWSER, _IS_WEB_BROWSER_INVOKED, _ALL_WEB_DRIVERS

    from pista.core._root_manager import PISTA_CONFIG
    from pista.core.file_service import FileUtil
    from pista.core._log_manager import LOG_FILE_PATH

    thread_id = threading.current_thread().native_id
    FileUtil.append_to_file(LOG_FILE_PATH.format(thread_id), f"\nClass: {request.node.name}\nMarkers: {request.node.own_markers}\n")

    from pista.core.driver_service import WebBrowser

    '''Setup web browser'''
    _defaultBrowser = PISTA_CONFIG.get('framework', 'default_browser')
    _IS_WEB_BROWSER_INVOKED = True
    WebBrowser.TEST_BROWSER = _BROWSER = request.config.getoption('--browser') or _defaultBrowser

    '''Open web browser'''
    driver = WebBrowser.open_browser(browser_name=_BROWSER)
    request.cls.driver = driver
    _ALL_WEB_DRIVERS = WebBrowser.ALL_DRIVERS

    yield request.cls.driver

    '''Close web browser'''
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # print('pista: pytest_runtest_makereport')

    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)


@pytest.fixture(scope="function", autouse=True)
def pista_func_setup(request, caplog, capsys):
    # print('pista: pista_func_setup')

    global _IS_WEB_BROWSER_INVOKED, _ALL_WEB_DRIVERS

    from pista.core.file_service import FileUtil
    from pista.core._log_manager import LOG_FILE_PATH
    
    thread_id = threading.current_thread().native_id
    FileUtil.append_to_file(LOG_FILE_PATH.format(thread_id), f"\nFunction: {request.node.name}\nMarkers: {request.node.own_markers}\n")

    yield

    from pista.core._root_manager import PISTA_CONFIG
    from pista.core.ui_service import UIService

    '''Capture web driver sreenshot'''
    testnode = request.node
    testfunc = testnode.name
    # testmodule = testnode.path.name
    # testclass = testnode.parent.name
    if testnode.rep_setup.passed and testnode.rep_call.failed:
        FileUtil.append_to_file(LOG_FILE_PATH.format(thread_id), f"Function: {request.node.name} (Status: failed)\n")
        for fixturename in testnode.fixturenames:
            driver = testnode.funcargs[fixturename]
            if _IS_WEB_BROWSER_INVOKED is True:
                if isinstance(driver, _ALL_WEB_DRIVERS):
                    UIService(driver=driver, is_for_screenshot=True).capture_screen(refFileName=testfunc)
                    break
    else:
        FileUtil.append_to_file(LOG_FILE_PATH.format(thread_id), f"Function: {request.node.name} (Status: passed)\n")

    '''Update jira'''
    if 'true' in PISTA_CONFIG.get('jira', 'is_update_jira'):
        _update_jira_for_testfunc(request, testfunc)

def _update_jira_for_testfunc(request, test_name):
    from pista.integration.jira.jira_service import update_results_to_jira

    testnode = request.node
    original_outcome = testnode.rep_call.outcome if 'rep_call' in dir(testnode) \
        else testnode.rep_setup.outcome if 'rep_setup' in dir(testnode) \
        else testnode.rep_teardown.outcome if 'rep_teardown' in dir(testnode) else None

    _issueId_list = []
    jira_marker = testnode.get_closest_marker('jira')
    if jira_marker:
        for marker_arg in jira_marker.args:
            _issueId_list.append(marker_arg)

    outcome_mapping = {"failed": "Fail", "passed": "Pass", "skipped": "Blocked"}
    issue_status = outcome_mapping.get(original_outcome)

    if len(_issueId_list) > 0:
        update_results_to_jira(_issueId_list, issue_status)
    _issueId_list.clear()

@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    # print('pista: pytest_sessionfinish')
    
    '''Close DB connections'''
    from pista.core.db_service import DBService
    if len(DBService.DB_CONNS) > 0:
        for k, v in DBService.DB_CONNS.items():
            try:
                if v is not None:
                    v.close()
            except Exception as e:
                print('Exception while closing DB conn ' + str(e))

    '''Terminate node process'''
    # Commons._close_node_process()  # TODO Handle to avoid close by other threads