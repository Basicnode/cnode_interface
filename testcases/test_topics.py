
import requests
import business.common as common

base_url = 'http://47.100.175.62:3000/api/v1'

def test_topic_index_page():
    query_parmas = {
        "page":1,
        "tab":'share',
        "limit":3,
        "mdrender": 'false'
    }
    r = requests.get(base_url + '/topics',params=query_parmas)
    print(r.status_code)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['success'] == True
    data = r.json()['data']
    assert len(data) == query_parmas['limit']

    for topic in data:
        assert topic['tab'] == query_parmas['tab']


def test_create_topic():
    topic_data = {
        "accesstoken": "f290306e-2fa3-429b-b516-8f967bc8ce93",
        "title": 'bbccdd1',
        "tab": 'ask',
        "content": 'ddddd1'
    }
    r = common.create_topic(topic_data)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['success'] == True

    r2 = common.create_topic(topic_data)
    assert r.json()['topic_id'] != r2.json()['topic_id']


def test_topic_update():
    topic_data = {
        "accesstoken":common.get_token(),
        "title": 'bbccdd',
        "tab": 'ask',
        "content": 'ddddd'
    }

    r = common.create_topic(topic_data)
    id = r.json()['topic_id']

    update_topic_data = {
        "accesstoken": common.get_token(),
        "title": "bbccdd",
        "topic_id":id,
        "tab": "ask",
        "content": "ddddd"
    }
    r =requests.post(base_url + '/topics/update',update_topic_data)
    print(r.json())

    assert r.json()['topic_id'] == id
    r_detail = common.topic_detail(id)
    print(r_detail.json())
    jsondata = r_detail.json()
    assert jsondata['data']['id'] == id
    assert jsondata['data']['tab'] == update_topic_data['tab']
    assert jsondata['data']['title'] == update_topic_data['title']
    assert update_topic_data["content"] in jsondata['data']['content']  
