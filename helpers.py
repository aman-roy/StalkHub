# This file has all the functions which will 
# be used in retriving data from GitHub API.

import urllib2
import json

# Basic retrival of data from 
# https://api.github.com/users/user_name
def basic_retrive(user_name):

	# concatenate user name to create link
	link = "https://api.github.com/users/" + user_name
	# empty list for collecting things I need
	box = []

	# Try to open link and if failed return None
	try:
		response = urllib2.urlopen(link)
		data = json.load(response)
		if not data:
			return None
	except:
		return None

	# Check if the link opened is user type
	if not data['type'] == "User":
		return None

	# Empty dict
	box_feed = {}

	# Collect everything in box and return box 
	try:
		box_feed['login'] = data['login']
		box_feed['avatar_url'] = data['avatar_url']
		box_feed['html_url'] = data['html_url']
		box_feed['name'] = data['name']
		box_feed['company'] = data['company']
		box_feed['blog'] = data['blog']
		box_feed['location'] = data['location']
		box_feed['bio'] = data['bio']
		box_feed['public_repos'] = data['public_repos']
		box_feed['public_gists'] = data['public_gists']
		box_feed['followers'] = data['followers']
		box_feed['following'] = data['following']
		box.append(box_feed)
		return box
	except:
		return None

def watch_list(user_name):
	# concatenate user name to create link
	link = "https://api.github.com/users/" + user_name + "/subscriptions"
	
	# empty list for collecting things I need
	box = []

	# Try to open link and if failed return None
	try:
		response = urllib2.urlopen(link)
		data = json.load(response)
		if not data:
			return None
	except:
		return None

	# pack the box with info we need
	for i in range(len(data)):
		box_feed = {}
		box_feed["full_name"] = data[i]["full_name"]
		box_feed["html_url"] = data[i]["html_url"]
		box.append(box_feed)

	return box
