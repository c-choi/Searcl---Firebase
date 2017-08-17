# import pyrebase
#
# # UID = main.UID
# # USERNAME = main.USERNAME
# # PICTURE = main.PICTURE
# # TITLE = main.TITLE
# # BODY = main.BODY
# # URL = main.URL
#
# config = {
#   "apiKey": "AIzaSyAkaWESNGQro0lAO9WX2o3rFoJHZ4toHhk",
#   "authDomain": "searcl-ce85f.firebaseapp.com",
#   "databaseURL": "https://searcl-ce85f.firebaseio.com",
#   "storageBucket": "searcl-ce85f.appspot.com"
# }
#
# firebase = pyrebase.initialize_app(config)
#
# # Get a reference to the auth service
# auth = firebase.auth()
#
# # Get a reference to the database service
# db = firebase.database()
#
#
# def writeNewPost(uid, username, picture, title, body):
#     postData = {
#     'author' : username,
#     'uid' : uid,
#     'body': body,
#     'title': title,
#     'starCount': 0,
#     'authorPic': picture
#   }
#
#     post = db.child('posts').push(postData)
#     print(post)
#
#     key = post['name']
#
#     user_post = db.child('user-posts/' + UID + '/' + key).update(postData)
#     print(user_post)
#
# # writeNewPost(UID, USERNAME, PICTURE, TITLE, BODY)
