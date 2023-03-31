class DataCommon:

    @classmethod
    def dict_key_and_value_list(cls, dict_data: dict) -> tuple[list, list]:
        """
        获取字典中的 key_list 和 value_list
        :param dict_data:
        :return:
        """
        key_list = [key for key, value in dict_data.items()]
        value_list = [value for key, value in dict_data.items()]
        return key_list, value_list

    @classmethod
    def lists_dict(cls, list_data1: list, list_data2: list) -> dict:
        """
        将二个列表合并成一个字典，如果两个列表的元素个数不相同，那么以元素个数最短的列表为准
        :param list_data1:
        :param list_data2:
        :return:
        """
        return dict(zip(list_data1, list_data2))
