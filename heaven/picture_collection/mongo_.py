import mongoengine


class CommonImagesMongodb(mongoengine.Document):
    name = mongoengine.StringField()  # 名称
    url = mongoengine.StringField()  # 图片 URL
    img = mongoengine.ImageField()  # 图片


class HormoneSetMongodb(mongoengine.Document):
    cartoon_name = mongoengine.StringField()  # 漫画名称
    image_name = mongoengine.StringField()  # 图片名称
    image_page = mongoengine.StringField()  # 图片页数
    image = mongoengine.ImageField()  # 图片
