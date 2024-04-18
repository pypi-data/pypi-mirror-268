import os
import shutil
from datetime import datetime
from pathlib import Path


class FileUtil:
    @staticmethod
    def is_exist(path):
        return os.path.exists(path)

    @staticmethod
    def is_it_file(path):
        return os.path.isfile(path)

    @staticmethod
    def is_it_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def get_file_extension(filename):
        if '.' in filename:
            return filename.rsplit('.', 1)[1].lower()

    @staticmethod
    def filename_only(name_with_extension):
        return Path(name_with_extension).stem

    @staticmethod
    def get_filename(path_with_filename):
        path_with_filename = path_with_filename.rstrip(os.sep)
        filename = os.path.basename(path_with_filename)
        return filename

    @staticmethod
    def delete(path):
        if FileUtil.is_exist(path):
            if FileUtil.is_it_file(path):
                os.remove(path)
            elif FileUtil.is_it_dir(path):
                shutil.rmtree(path, ignore_errors=True)
            else:
                return False
        return True

    @staticmethod
    def create_directories(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def rename(source, destination):
        os.rename(source, destination)

    @staticmethod
    def copy(source, destination, ignore=None):
        if os.path.isdir(source):
            return shutil.copytree(source, destination, ignore)
        else:
            return shutil.copy(source, destination)

    @staticmethod
    def join_path(*args):
        return os.path.join(*args)

    @staticmethod
    def getcwd():
        return os.getcwd()

    @staticmethod
    def file_size_into_byte(path):
        if FileUtil.is_exist(path):
            return os.stat(path).st_size
        return None

    @staticmethod
    def get_created_modified_datetime(path):
        if not FileUtil.is_exist(path):
            return None, None
        load_file_path = Path(path)
        create_timestamp = load_file_path.stat().st_ctime
        modify_timestamp = load_file_path.stat().st_mtime
        return datetime.fromtimestamp(create_timestamp), datetime.fromtimestamp(modify_timestamp)

    @staticmethod
    def create_empty_file(path):
        try:
            with open(path, "x") as empty:
                empty.close()
                return True
        except FileExistsError:
            return False

    @staticmethod
    def human_readable_file_size(size):
        B = float(size)
        KB = float(1024)
        MB = float(KB ** 2)
        GB = float(KB ** 3)
        TB = float(KB ** 4)

        if B < KB:
            return '{0} {1}'.format(B, 'B' if 0 == B > 1 else 'B')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B / KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B / MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B / GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B / TB)

    """
        Task: Use the method for check any service started withing the time difference in second.

        Usages: It used when production mode has multiple worker, run service multiple time, so it can help to prevent 
        multi start of a service more than once
    """

    @staticmethod
    def is_started(check_file_path_name: str, time_diff_in_sec) -> bool:
        current_time = datetime.now()
        if FileUtil.is_exist(check_file_path_name):
            created, modified = FileUtil.get_created_modified_datetime(check_file_path_name)
            diff = current_time - created
            if diff.seconds > time_diff_in_sec:
                FileUtil.delete(path=check_file_path_name)
            else:
                return True
        FileUtil.create_empty_file(path=check_file_path_name)
        return False
