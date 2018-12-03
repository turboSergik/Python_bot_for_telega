import requests
import json
import time


#//////////////////////////////////////////////////////////////////////////////////////////////////

#auth_token = '233e7ef7888d82e098b3d63ca2a888d0e32a0eea'
#heads = {'Authorization': 'Token {}'.format(auth_token)}

#print(resp)
#print()

#//////////////////////////////////////////////////////////////////////////////////////////////////


url_test = 'https://test.bop.rest/api/feed/'

token = "752741562:AAHi0Zjl4hKp1ib3kMyrMP-ljH32HRTF5gU"
url = "https://api.telegram.org/bot752741562:AAHi0Zjl4hKp1ib3kMyrMP-ljH32HRTF5gU/".format(token)


method_getUpd = 'getUpdates'
param_getUpd = {'limit' : 1, 'offset' : -1}

method_sendMess = 'sendMessage'
param_sendMess = {'chat_id' : 0, 'text' : ''}


last_data = -1

#//////////////////////////////////////////////////////////////////////////////////////////////////

while 1:

	print("I still workong")
	s = ''

	res = requests.get(url + method_getUpd, param_getUpd).json()

	param_sendMess['chat_id'] = res['result'][0]['message']['from']['id']

	last = ''
	
	#print(res)

	for i in res['result']:
		last = i['message']['text']
		data = i['message']['date']

	#print(last)
	#print('last_data = ' + str(last_data) + ' data = ' + str(data))

	if (last == '/feed' and data != last_data and last_data != -1):

		param_sendMess['text'] = 'Last 10 updates: '
		requests.get(url + method_sendMess, param_sendMess)

		#//////////////////////////////////////////////////////////////////////////////////////////////////
		
		auth = {'Authorization' : 'Token 233e7ef7888d82e098b3d63ca2a888d0e32a0eea'}
		resp = requests.get(url_test, headers = auth).json()

		count_2 = 0
		for i in resp: count_2 += 1

		for i in resp:
			#print('Match name: ' + i['name'])

			count_2 -= 1
			if count_2 >= 10:
				continue

			s = s + 'Match name: ' + i['name'] + '\n'

			s_2 = i['time']
			posT = 0
			posZ = 0
			count = 0

			for j in s_2:
				if j == 'T': posT = count
				if j == 'Z': posZ = count
				count += 1

			#print(str(posT) + ' ' + str(posZ))

			#print ('	Match date: ' + i['time'][0:posT])
			s = s + '			Match date: ' + i['time'][0:posT] + '\n'

			#print('	Match time: ' + i['time'][posT + 1:posZ])
			s = s + '			Match time: ' + i['time'][posT + 1:posZ] + '\n'

			#print()
			s = s + '\n'

		#//////////////////////////////////////////////////////////////////////////////////////////////////

		#s = s + str(count_2) + '\n'

		#print(s)
		#print(count_2)

		param_sendMess['text'] = s
		requests.get(url + method_sendMess, param_sendMess)

	for i in res['result']:
		last_data = i['message']['date']


	time.sleep(4)







	




