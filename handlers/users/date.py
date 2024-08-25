import requests

def userget():
    #url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    url = 'http://127.0.0.1:8000/api/telegramuser/'
    respons = requests.get(url)
    return respons.json()



def usercreate(first_name,username,user_id):
    #url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    url = 'http://127.0.0.1:8000/api/telegramuser/'
    re = requests.post(url,data={'first_name':first_name,'last_name':username,'user_id':user_id})
    return re.status_code


def user(user_id):
    #url = 'https://temur01.pythonanywhere.com/api/user/'+ user_id + '/'
    url = 'http://127.0.0.1:8000/api/user/'+ user_id + '/'
    respons = requests.get(url)
    return respons.json()


def create_channel(name,channel_id):
    url = 'http://127.0.0.1:8000/api/channel/'
    respons = requests.post(url,data={'name':name,'channel_id':channel_id})
    return respons.status_code



def delete_channel(channel_id):
    url = 'http://127.0.0.1:8000/api/channel/delete/' + channel_id + '/'
    respons = requests.delete(url)
    return respons.status_code



def channelget():
    url = 'http://127.0.0.1:8000/api/channel/'
    respons = requests.get(url)
    date = respons.json()
    channels = []

    for i in date:
        channels.append(i["channel_id"])

    return channels

def channelal():
    url = 'http://127.0.0.1:8000/api/channel/'
    respons = requests.get(url)
    return respons.json()



def userpersonalinfo(user_id,name,job,tel,username,email,addres):
    url = 'http://127.0.0.1:8000/api/personalcreate/'
    re = requests.post(url,data={'user_id':user_id,'name':name,'job':job,"tel":tel,"username":username,"email":email,"addres":addres   })
    return re.status_code


def userperinfo(user_id):
    #url = 'https://temur01.pythonanywhere.com/api/user/'+ user_id + '/'
    url = 'http://127.0.0.1:8000/api/personalinfo/'+ user_id + '/'
    respons = requests.get(url)
    return respons.json()


def edit_userinfo(user_id,name,job,tel,username,email,addres):
    url = 'http://127.0.0.1:8000/api/personalinfo/'+ user_id + '/'
    data = {
    'name': name,
    'job': job,
    'tel': tel,
    'username': username,
    'email': email,
    'addres': addres
}

    respons = requests.put(url, json=data)

    return respons.json()



