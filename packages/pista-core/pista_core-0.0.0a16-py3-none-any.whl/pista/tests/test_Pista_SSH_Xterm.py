from pista.core.ssh_xtermjs_service import SshXtermService
from pista.tests import *


@class_marker
@m.usefixtures("invoke_web_driver")
class Test_Pista_SSH_Xterm(TestBase):
    logger = Logging.get(__qualname__)

    @m.order(1)
    @m.dependency(name="test_Pista_SSH_Xterm")
    def test_Pista_SSH_Xterm(self):
        """Test pista with SSH xterm code"""
        printit('SSH Xterm')

        # isRunYarn = PISTA_CONFIG.get('ssh', 'is_run_yarn_for_xtermjs')

        xtermCodePath = PISTA_CONFIG.get('ssh', 'xtermjs_code_path')  # Correct the path in pista_config.ini

        # if 'true' in PISTA_CONFIG.get('ssh', 'is_run_yarn_for_xtermjs'):
        SshXtermService._start_node(xterm_code_path=xtermCodePath)

        rfXtermService = SshXtermService(driver=self.driver)

        txt = rfXtermService.readScreen()
        print('txt', txt)

