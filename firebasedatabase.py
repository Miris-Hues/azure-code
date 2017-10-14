from firebase import firebase

firebase = firebase.FirebaseApplication('https://miris-hues.firebaseio.com/')

result = firebase.get('/fcm', None)

print(result['-KwPxYMV6-t1CvqRuu9V']['key'])