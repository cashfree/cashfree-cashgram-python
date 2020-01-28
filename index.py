'''
Below is an integration flow on how to use Cashfree's cashgram feature.
Please go through the payout docs here: https://docs.cashfree.com/docs/payout/guide/

The following script contains the following functionalities :
    1.getToken() -> to get auth token to be used in all following calls.
    2.createCashgram() -> to create cashgram.
    3.cashgramGetStatus() -> to get the cashgrams status


All the data used by the script can be found in the config.ini file. This includes the clientId, clientSecret, cashgram section.
You can change keep changing the values in the config file and running the script.
Please enter your clientId and clientSecret, along with the appropriate enviornment and bank details
'''


#warning the following code is written for python2 and tested using python2.7
#warning the following code has a dependency on the request, configparser library
import configparser
import requests
import json

#read the config file
config = configparser.ConfigParser()
config.optionxform = str
if config.read('config.ini') == []:
    print 'unable to read config'
    exit()

#default
default = config._sections['default']
clientId, clientSecret, env = default['clientId'], default['clientSecret'], default['env']
baseurl = config._sections['baseUrl'][env]
url = config._sections['url']

#get auth token
def getToken():
    try:
        finalUrl = baseurl + url['auth']
        r =  requests.post(finalUrl, headers={ "X-Client-Id":clientId, "X-Client-Secret":clientSecret})

        if (not r):
            raise Exception("response err: response is null")

        content = json.loads(r.content)


        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        return content["data"]["token"]
    except Exception as err:
        print 'err in getting token'
        raise Exception(err)

#create cashgram
def createCashgram(token):
    try:
        finalUrl = baseurl + url['createCashgram']
        cashgram = config._sections['cashgramDetails']
        r = requests.post(finalUrl, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret, 'Content-Type': 'application/json','Authorization': 'Bearer ' + token}, json=cashgram)
        content = json.loads(r.content)

        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        print content
        print 'cashgram created successfully'
    except Exception as err:
        print 'err in creating cashgram'
        raise Exception(err)

#check status of cashgram
def cashgramGetStatus(token):
    try:
        cashgramId = config._sections['cashgramDetails']['cashgramId']
        queryString = "?cashgramId="+cashgramId
        finalUrl = baseurl + url['getCashgramStatus'] + queryString
        r = requests.get(finalUrl, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret, 'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        content = json.loads(r.content)

        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        print content
    except Exception as err:
        print 'err in getting cashgram status'
        raise Exception(err)

'''
The flow executed below is:
1. fetching the auth token
2. creating a cashgram
3. getting the status of the cashgram
'''

#main function
if __name__ == '__main__':
    token = getToken()
    createCashgram(token)
    cashgramGetStatus(token)

