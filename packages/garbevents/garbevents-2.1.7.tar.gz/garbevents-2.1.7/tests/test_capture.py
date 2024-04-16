#!/usr/bin/python
"""
@Author  :  Lijiawei
@Date    :  2022/3/25 5:03 下午
@Desc    :  test_capture line.
"""
from garbevents.capture import GetData
from garbevents.settings import Settings as ST

"gb -p 8888 --ssl-insecure -s test_capture.py"

ST.url = "https://test.com"

ST.db_path = "proxy"

addons = [GetData()]
