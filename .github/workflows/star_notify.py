"""started notify"""
import os
import sys

import requests
import yagmail

if __name__ == '__main__':
    token = sys.argv[1]
    user, repo = os.getenv('GITHUB_REPOSITORY').split('/')
    data = requests.post(
        'https://api.github.com/graphql',
        json={
            'query': '{ repository(name: "' + repo + '", owner: "' + user + '") { stargazerCount stargazers(last: 1) { edges { node { name url avatarUrl email } } } } }'},
        headers={
            'Authorization': 'Bearer ' + token,
        }
    ).json()['data']

    try:
        last_user = data['repository']['stargazers']['edges'][0]['node']
        content = f"""
<div style="text-align: center;">
    <h1>{data['repository']['stargazerCount']} 💕</h1>
    <img src="{last_user['avatarUrl']}" alt="avatar" style="width:200px; border-radius: 100px">
    <div style="margin: 10px; font-size: x-large">{last_user['name']} {last_user['email']}</div>
    <a href="{last_user['url']}" style="display: block; font-size: large">{last_user['url']}</a>
</div>
"""
    except:
        content = f"""
<div style="text-align: center;">
    <h5>刚刚有个吊毛，给你标星，又取消了 💕</h5>
    <h3>不知道是谁 😂</h3>
    <h4>是不是你自己呀 🤣</h4>
</div>
"""
    yag = yagmail.SMTP({'started_notify@163.com': 'started notify'}, 'QDCONGQTZIIZKBBI', 'smtp.163.com', 465)
    notify_email = sys.argv[2]
    yag.send(notify_email, f'[{user}/{repo}] Started', content)
