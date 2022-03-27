"""
测试发帖的异常场景
"""
import pytest
import requests
from business.file_utils import parse_json_file

test_data = parse_json_file('data/topics.json')

@pytest.mark.parametrize('topic_data,code,msg',test_data)
def test_create_topic(topic_data, code, msg):
    print(topic_data, code, msg)
    res = requests.post('http://47.100.175.62:3000/api/v1/topics', topic_data)
    print('返回数据：', res.json())
    assert res.status_code == code
    assert res.json()['error_msg'] == msg


