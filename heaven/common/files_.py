import os
from picture_collection.mongo_ import HormoneSetMongodb


class FilesCommon:

    @classmethod
    def path_list_files(cls, folder_path) -> list:
        """
        :param folder_path:
        :return: []
        返回的结果已经排序了
        """
        dirs = os.listdir(folder_path)
        dirs.sort()
        dirs_ = []
        for file_name in dirs:
            file = os.path.join(folder_path + "/" + file_name)
            dirs_.append({"image_name": file_name, "image_path": file})
        return dirs_

    @classmethod
    def open_files_save_mongodb(cls, dirs_, folder_name) -> bool:
        """
        :param dirs_:
        :param folder_name:
        :return:
        """
        for dirs in dirs_:
            image = open(dirs.pop("image_path"), "rb")
            dirs["image"] = image
            dirs["cartoon_name"] = folder_name
            try:
                HormoneSetMongodb.objects.get_or_create(**dirs)
            except Exception as e:
                print(str(e))
                return False
        return True
