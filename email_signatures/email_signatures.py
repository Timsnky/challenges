# @Author: Phillis Kiragu <PKiragu>
# @Date:   2016-10-02T22:57:02+03:00
# @Email:  pkiragu@cytonn.com
# @Last modified by:   PKiragu
# @Last modified time: 2016-10-04T15:40:42+03:00

# SQL Query to run
# INSERT INTO oauth_clients(id, secret, name, created_at, updated_at) VALUES ('3', 'retRDTFYGrt545354fsdgfh', 'HRSystem', NOW(), NOW());

import urllib2
import csv
import json
import requests
from time import sleep

# Url to fetch the token
url = "https://hr.cytonn.com/oauth/token"
#url = "https://hr.cytonn.com/oauth/token"

# Enter the correct client credentials
CLIENT_ID = "3"
CLIENT_SECRET = "retRDTFYGrt545354fsdgfh"


try:
# Pass the client credentials above to the payload
    payload = "grant_type=client_credentials&client_id="+str(CLIENT_ID)+"&client_secret="+str(CLIENT_SECRET)
    print payload
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }

    # send a post request to the url to fetch the access token
    response = requests.post(url, data = payload, headers = headers)

    data = response.json()

    # get the access token from the json response
    access_token_key = data['access_token']
except:
     print ("An error occurred. Check that you have the correct client credentials")
     exit()

print "Access key obtained, downloading csv..."

# API url
# csv_url = "https://hr.cytonn.com/api/signature/export?access_token={0}".format(access_token_key)
# csv_url = "https://hr.app/api/signature/export?access_token={0}".format(access_token_key)

try:
    # API url
    # csv_url = "https://hr.cytonn.com/api/signature/export?access_token={0}".format(access_token_key)
    #csv_url = "https://hr.app/api/signature/export?access_token={0}".format(access_token_key)
    csv_url = 'https://hr.cytonn.com/api/signature/export'

    headers2 = {
        'Authorization': 'Bearer ' + access_token_key
    }

    request = urllib2.Request(csv_url, headers=headers2)

    # open the api url
    data = urllib2.urlopen(request)
    # data = urllib2.urlopen(str(csv_url))

    file = data.read()

    # write the results in a csv file
    with open('signatures_all.csv', 'wb') as f:
        f.write(file)

        print ("File Saved Successfully")
except:
     print ("Could Not Print The File")


