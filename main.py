import requests
from send_email import send_email

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=techcrunch&'
       'apiKey=b85242105a53484cbbec775f35e243f1')

request = requests.get(url)
content = request.json()

message = """\
Subject: News

From:Myself

"""
for article in content['articles']:
    title = article['title']
    description = article['description']
    url = article['url']

    # message = message + f"b{title}\n{description}\n{url}\n\n"
    if title is not  None:
        message = message + title + '\n' + description + '\n' + url + '\n' + '\n'

# print(message.__contains__('\u2026'))
message = message.encode('utf-8')
send_email(message)