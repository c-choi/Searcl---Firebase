from apscheduler.schedulers.blocking import BlockingScheduler
import time
import pyrebase
from urllib.request import urlopen
from bs4 import BeautifulSoup

title = time.strftime("%Y-%m-%d %H:%M", time.localtime())
category = {'economy': '경제', 'society': '사회', 'culture': '문화', 'diplomacy': '외교'}

for c in category.keys():
    url = 'http://www.korea.kr/policy/' + c + 'List.do'
    response = urlopen(url)
    plain_text = response.read()
    soup = BeautifulSoup(plain_text, 'html.parser')
    lists = soup.select('dl')
    body_data = ""
    i = 1

    for list in range(len(lists)-1):
        try:
            body_data += str(i) + ". " + lists[list].find('a').text.strip() + "\n\n"
            i += 1
        except:
            pass

    print(body_data)

    UID = '5rCTVQtsUvW0Yti7mwijlmZnKRv1'
    USERNAME = 'news_bot'
    PICTURE = ''
    TITLE = category[c] + ' ' + title
    BODY = body_data
    URL = 'https://searcl-ce85f.firebaseio.com/'


    config = {
      "apiKey": "AIzaSyAkaWESNGQro0lAO9WX2o3rFoJHZ4toHhk",
      "authDomain": "searcl-ce85f.firebaseapp.com",
      "databaseURL": "https://searcl-ce85f.firebaseio.com",
      "storageBucket": "searcl-ce85f.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Get a reference to the database service
    db = firebase.database()


    def writeNewPost(uid, username, picture, title, body):
        postData = {
        'author' : username,
        'uid' : uid,
        'body': body,
        'title': title,
        'starCount': 0,
        'authorPic': picture
      }

        post = db.child('posts').push(postData)
        key = post['name']
        user_post = db.child('user-posts/' + UID + '/' + key).update(postData)
        print(post)
        print(user_post)

    scheduler = BlockingScheduler()
    scheduler.add_job(writeNewPost(UID, USERNAME, PICTURE, TITLE, BODY), 'interval', hours=1)
    scheduler.start()
