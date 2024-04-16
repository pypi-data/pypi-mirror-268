# Call this only after call to _config_manager

import os
import sys
from configparser import ConfigParser

# import pytest

from pista.core.common_service import Commons
from pista.root import PISTA_DIR

# assert 'env' in os.environ.keys(), 'Env is not set yet. Resolve and rerun.'
# ENV = os.environ['env'] if 'env' in os.environ.keys() else ''
# ENV = os.environ['env']

# PROJECT_ROOT_DIR = os.environ['projectRootDirPath']
# _IS_PISTA_A_PROJECT = True if PROJECT_ROOT_DIR else False
_isAProject, PROJECT_ROOT_DIR = Commons.get_project_root_from_sys_args()

# print('_root_manager (project):', _isAProject, PROJECT_ROOT_DIR)

_pistaConfigFilePath = os.path.join(PROJECT_ROOT_DIR, 'pista_config.ini')
if not os.path.exists(_pistaConfigFilePath):
    _pistaConfigFilePath = os.path.join(PISTA_DIR, 'pista_config.ini')

PISTA_CONFIG = ConfigParser()
PISTA_CONFIG.read(_pistaConfigFilePath)

PROJECT_ID = PISTA_CONFIG.get('framework', 'project_id')

OUTPUT_DIR = os.path.join(PROJECT_ROOT_DIR, 'output')
SCREENSHOT_DIR = os.path.join(OUTPUT_DIR, 'screenshot')
THREAD_DATA_RUNTIME_FILE = os.path.join(OUTPUT_DIR, 'thread_data.xlsx')

TEST_DIR = os.path.join(PROJECT_ROOT_DIR, PROJECT_ID, 'tests')
RESOURCE_DIR = os.path.join(PROJECT_ROOT_DIR, PROJECT_ID, 'resources')

REQUIREMENT_FILE = os.path.join(PROJECT_ROOT_DIR, 'requirements.txt')
if not os.path.exists(_pistaConfigFilePath):
    REQUIREMENT_FILE = os.path.join(PISTA_DIR, 'requirements.txt')
