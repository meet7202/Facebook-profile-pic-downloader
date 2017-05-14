import urllib.request
import json

def image_download(friend):
	size = '/picture?width=250&height=250'
	url = 'https://graph.facebook.com/'+ friend['id'] + size
	image = urllib.request.urlopen(url).read()
	f = open(friend['name'] + '.jpg', 'wb')
	f.write(image)
	f.close()
	print (friend['name'] + '.jpg Downloaded')
print("Hi...!!  Welcome to Facebook Auto Image Downloader by Meet Shah")
print("please generate your token\n from https://developers.facebook.com/tools/explorer with user_friends option marked and enter that token here...!!")
print("please Enter your Token : ",end='')
token = input()
#get the token https://developers.facebook.com/tools/explorer
url = ('https://graph.facebook.com/me/friends?access_token='+token)
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

for friend in data['data']:
  image_download(friend)
print("\n\nThank you for using my Auto Image Downloader")