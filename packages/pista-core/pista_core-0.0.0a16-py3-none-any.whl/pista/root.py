import os

'''FOR PISTA_CORE - DO NOT CHANGE'''
PISTA_DIR = os.path.dirname(os.path.abspath(__file__))
PISTA_CORE_DIR = os.path.dirname(PISTA_DIR)
PISTA_TEST_DIR = os.path.join(PISTA_DIR, 'tests')
PISTA_RESOURCE_DIR = os.path.join(PISTA_DIR, 'resources')
THREAD_DATA_TEMPLATE_FILE = os.path.join(PISTA_RESOURCE_DIR, 'templates', 'thread_data.xlsx')
