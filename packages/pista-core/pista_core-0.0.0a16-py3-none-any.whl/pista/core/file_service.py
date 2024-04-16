import os

from pista.core._root_manager import OUTPUT_DIR, SCREENSHOT_DIR
from pista.core.common_service import Commons


class FileUtil:

    @staticmethod
    def create_file(filepath: str):
        try:
            with open(filepath, mode='w') as f:
                pass
        except Exception:
            assert False, 'Exception found during file creation: ' + filepath

    @staticmethod
    def read_from_file(filepath: str) -> str:
        try:
            with open(filepath, mode='r') as f:
                contents = f.read()
        except FileNotFoundError:
            assert False, 'File not found: ' + filepath
        except Exception:
            assert False, 'Exception found during file reading: ' + filepath
        return contents

    @staticmethod
    def append_to_file(filepath: str, content):
        try:
            with open(filepath, mode='a', encoding='utf-8') as f:
                contents = f.write(content)
        except FileNotFoundError:
            assert False, 'File not found: ' + filepath
        except UnicodeEncodeError as e:
            assert False, 'UnicodeEncodeError found during file appending: ' + filepath
        except Exception:
            assert False, 'Exception found during file appending: ' + filepath

    @staticmethod
    def write_to_file(filepath: str, content):
        try:
            with open(filepath, mode='w') as f:
                contents = f.write(content)
        except FileNotFoundError:
            assert False, 'File not found: ' + filepath
        except UnicodeEncodeError as e:
            assert False, 'UnicodeEncodeError found during file writing: ' + filepath
        except Exception:
            assert False, 'Exception found during file writing: ' + filepath

    @staticmethod
    def replace_in_file(filepath: str, old_val: str, new_val: str):
        pass

    @staticmethod
    def archive_outputs(file_dttm):
        output_file = 'archive_{}'
        file_dttm = Commons.build_date_for_filename()
        arch_path = os.path.join(OUTPUT_DIR, output_file.format(file_dttm))

        '''Move output reports to archive dir'''
        oldfiles = [f for f in os.listdir(OUTPUT_DIR) if f.lower().endswith(('.html', '.xls', '.xlsx', '.log', '.xml'))]
        screenshots = ''
        if os.path.exists(SCREENSHOT_DIR):
            screenshots = [f for f in os.listdir(SCREENSHOT_DIR) if f.lower().endswith('.png')]
        if len(oldfiles) > 0 or len(screenshots) > 0:
            try:
                if not os.path.exists(arch_path):
                    os.mkdir(arch_path)
            except Exception as e:
                print('Exception while creating archive dir', str(e))

            for oldfile in oldfiles:
                try:
                    os.rename(OUTPUT_DIR + '/' + oldfile, arch_path + '/' + oldfile)
                except (PermissionError, FileNotFoundError):
                    pass
            for screenshot in screenshots:
                try:
                    os.rename(SCREENSHOT_DIR + '/' + screenshot, arch_path + '/' + screenshot)
                except (PermissionError, FileNotFoundError):
                    pass

        '''Delete thread_data file if exists'''
        thread_data_lock_path = os.path.join(OUTPUT_DIR, 'thread_data.xlsx.lock')
        if os.path.exists(thread_data_lock_path):
            os.rmdir(thread_data_lock_path)
