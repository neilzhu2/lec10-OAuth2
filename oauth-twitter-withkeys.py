
from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

# protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
# print (r.text)


results = r.json()
# fw = open('tweet.json', 'w')
# json_to_write = json.dumps(results, sort_keys = True, indent = 2)
# fw.write(json_to_write)
# fw.close()

for eachStatus in results["statuses"]:
    print('----------')
    print(eachStatus["user"]["name"], end = ":\n")
    print(eachStatus["text"])
print('----------')
