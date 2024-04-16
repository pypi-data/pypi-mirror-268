import os
import sys
from configparser import ConfigParser

from pista.core._root_manager import PROJECT_ROOT_DIR, PISTA_CONFIG, PROJECT_ID
from pista.core.common_service import Commons
from pista.root import PISTA_RESOURCE_DIR

# _triggeredTestPath = os.path.abspath(sys.argv[1])
# parts = str(_triggeredTestPath).split(os.path.sep)
# _IS_PISTA_A_PROJECT = True if 'pista' not in parts else False

_isAProject, _projectRootDir = Commons.get_project_root_from_sys_args()

# print('_config_manager (project):', _isAProject, _projectRootDir)

# _IS_PISTA_A_PROJECT = True if os.environ['projectRootDirPath'] else False
if _isAProject:
    _envConstFilePath = os.path.join(_projectRootDir, PROJECT_ID, 'resources', 'env_constants.ini')
else:
    _envConstFilePath = os.path.join(PISTA_RESOURCE_DIR, 'env_constants.ini')

# print('_config_manager (envConst):', _envConstFilePath)

ENV_CONST = ConfigParser()
ENV_CONST.read(_envConstFilePath)

ENV = ''

ENV_CONFIG = ConfigParser()


def _set_env(env, _isAProject:bool=False, _projectRootDir=''):
    global ENV, ENV_CONFIG

    assert env, 'Env name not provided. Provide and rerun.'

    ENV = env
    
    envConfigFile = f"env_config_{env}.ini"

    # _isAProject, _projectRootDir = Commons.get_project_dtls_from_arg()

    # _IS_PISTA_A_PROJECT = True if os.environ['projectRootDirPath'] else False
    if _isAProject:
        envConfigFilePath = os.path.join(_projectRootDir, PROJECT_ID, 'resources', envConfigFile)
    else:
        envConfigFilePath = os.path.join(PISTA_RESOURCE_DIR, envConfigFile)

    isAProject = _isAProject
    projectRootDir = _projectRootDir

    # print('_config_manager (_set_env.project):', _isAProject, _projectRootDir)
    # print('_config_manager (_set_env.envConfig):', env, envConfigFilePath)

    if os.path.exists(envConfigFilePath):
        ENV_CONFIG.read(envConfigFilePath)
    else:
        assert False, f"env_confg_ file not found {envConfigFilePath}"
