import pytest
import requests
import json
from business.file_utils import parse_excel_file

test_data = parse_excel_file('data/data.xlsx', 'topics')

@pytest.mark.parametrize('url,method,topic_data,code,msg', test_data)
def test_create_topic(url, method, topic_data, code, msg):
    if method =='post':
        res = requests.post(url, data=json.loads(topic_data))
        # print(res.json())
        assert res.status_code == code
        assert res.json() == json.loads(msg)

    elif method == 'get':
        res = requests.get(url, data=json.loads(topic_data))
        assert res.status_code == code
        assert res.json()['data']['loginname'] == json.loads(msg)['data']['loginname']







