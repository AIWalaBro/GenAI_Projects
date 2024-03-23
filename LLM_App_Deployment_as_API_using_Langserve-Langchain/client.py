#     # i have to call /essay/ invoke for creating and here expecting the topic
#     # so we are given topic ove here.
#     


import requests

response=requests.post(
    "http://localhost:8000/essay/invoke",
    json={'input':{'topic':"my best friend"}})

print(response.json()['output']['content'])
