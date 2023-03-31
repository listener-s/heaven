from common.files_ import FilesCommon
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    将 图片集合 存储到 mongodb ,启动命令为：
    python manage.py set_images --folder_name 文艺 --folder_path ./文艺
    folder_name: 文件名称
    folder_path: 文件路径
    """
    def add_arguments(self, parser):
        parser.add_argument("--folder_name")
        parser.add_argument("--folder_path")

    def handle(self, *args, **options):
        folder_name = options['folder_name']
        folder_path = options['folder_path']
        dirs = FilesCommon.path_list_files(folder_path=folder_path)
        save_status = FilesCommon.open_files_save_mongodb(dirs, folder_name)
        if save_status is True:
            print("OK!")
        else:
            print("Error !")
