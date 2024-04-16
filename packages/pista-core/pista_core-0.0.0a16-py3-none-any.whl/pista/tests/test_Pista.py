from pista.tests import *


@class_marker
class Test_Pista(TestBase):
    logger = Logging.get(__qualname__)

    @m.order(1)
    @m.dependency(name="test_Pista")
    def test_Pista(self):
        """Test pista framewok"""
        self.logger.info(f'Project root dir {PROJECT_ROOT_DIR}')

        printit('Jira user name', PISTA_CONFIG.get('jira', 'jira_username'))
        printit('Google url', ENV_CONST.get('app', 'google_home_url'))
        printit('API url', ENV_CONFIG.get('api', 'module1_base_url'))
