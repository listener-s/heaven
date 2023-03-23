import random

import requests

from setHelp.ReptileHelp import ReptileHelps


class Reptile:
    @classmethod
    def headers(cls) -> dict:
        headers = dict()
        headers['User-Agent'] = random.choice(ReptileHelps.USER_AGENT_LIST)
        return headers

    @classmethod
    def content_image(cls, url) -> bytes:
        img_response = requests.get(url, headers=cls.headers())
        return img_response.content
