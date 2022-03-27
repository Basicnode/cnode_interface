import requests

def create_topic(topicdata):
    url = 'http://47.100.175.62:3000/api/v1/topics'
    r = requests.post(url=url, json=topicdata)
    return r


def topic_detail(id):
    url = 'http://47.100.175.62:3000/api/v1/topic/' + id
    return requests.get(url)


def get_token():
    return "f290306e-2fa3-429b-b516-8f967bc8ce93"



