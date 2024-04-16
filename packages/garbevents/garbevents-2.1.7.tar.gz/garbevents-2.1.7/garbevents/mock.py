#!/usr/bin/python
"""
@Author  :  Lijiawei
@Date    :  2020/11/20 09:48 上午
@Desc    :  mock line.
"""
import json
import traceback

import mitmproxy
from loguru import logger

from garbevents.settings import Settings as ST


class GetData:
    """
    A garbevents HTTP mock class.
    """

    def __init__(self):
        try:
            self.content = ST.mock["content"]
            self.api = ST.mock["api"]
        except (TypeError, KeyError):
            logger.error(traceback.format_exc())
            self.content = {}
            self.api = ""

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
        mock modifies the response interface
        :param flow:
        :return:
        """
        if ST.url in flow.request.url:
            if self.api in flow.request.url:
                response = json.loads(flow.response.get_text())
                logger.info(f"original response content: {response}")
                response_content = json.dumps(self.content)
                logger.info(f"mock response content: {self.content}")
                flow.response.set_text(response_content)
                logger.info(f"{self.api} modify success!")
