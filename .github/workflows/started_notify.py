"""started notify"""

import json
import os
import smtplib
import sys
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from http.client import HTTPSConnection
from urllib import request
import traceback

if __name__ == "__main__":
    token = sys.argv[1]
    user, repo = os.getenv("GITHUB_REPOSITORY").split("/")

    conn = HTTPSConnection("api.github.com")
    conn.request(
        "POST",
        "/graphql",
        json.dumps(
            {
                "query": '{ repository(name: "'
                + repo
                + '", owner: "'
                + user
                + '") { stargazerCount stargazers(last: 1) { edges { node { name url avatarUrl email } } } } }'
            }
        ),
        {
            "User-Agent": "Python3",
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
        },
    )

    data = conn.getresponse().read().decode("utf8")
    data = json.loads(data)["data"]

    sender = "started_notify@163.com"
    receiver = sys.argv[2]

    msg_root = MIMEMultipart()
    msg_root["From"] = formataddr(("started notify", sender))
    msg_root["To"] = formataddr((receiver, receiver))
    msg_root["Subject"] = f"[{user}/{repo}] started"

    try:
        last_user = data["repository"]["stargazers"]["edges"][0]["node"]
        content = f"""
<div style="text-align: center;">
    <h1>{data['repository']['stargazerCount']} 💕</h1>
    <img style="max-width: 100%; border-radius: 50%" src="cid:avatar">
    <div style="margin: 10px; font-size: x-large">{last_user['name']} {last_user['email']}</div>
    <a href="{last_user['url']}" style="display: block; font-size: large">{last_user['url']}</a>
</div>
"""

        msg_image = MIMEImage(request.urlopen(last_user["avatarUrl"]).read(), "png")
        msg_image.add_header("Content-ID", "<avatar>")

        msg_root.attach(msg_image)

        msg_root.attach(MIMEText(content, "html"))

        smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
        smtp.login(sender, "QDCONGQTZIIZKBBI")
        for i in range(1, 4):
            try:
                result = smtp.sendmail(sender, [receiver], msg_root.as_bytes())
                break
            except smtplib.SMTPServerDisconnected as e:
                traceback.print_exception(e)
                time.sleep(i * 3)
    except Exception as e:
        traceback.print_exception(e)
