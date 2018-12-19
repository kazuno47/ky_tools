import os
from glob import glob

BACKUP_DIR_NAME = "/clean_desktop"

def _move_files_from_desktop_to_backup_dir():

    user_dir_path = os.path.expanduser('~')
    user_desktop_path = user_dir_path + '/Desktop/*'

    target_files = glob(user_desktop_path)


def _create_backup_dir_if_none():

    global BACKUP_DIR_NAME
    user_dir_path = os.path.expanduser('~')
    backup_dir_path = user_dir_path + BACKUP_DIR_NAME

    if not os.path.exists(backup_dir_path):
        os.mkdir(backup_dir_path)


def do_logic():
    _create_backup_dir_if_none()
    _move_files_from_desktop_to_backup_dir()


if __name__ == '__main__':
    do_logic()