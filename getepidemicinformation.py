import pandas as pd
import requests

headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'}

url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?'
res = requests.get(url,headers=headers)
res.text

print(type(res.text))
print(len(res.text))

# load by JSON, beautify format
import json
data_json = json.loads(res.text)
data_json

data=data_json['data']
data.keys()

#find area data, use China's data as an example
data_province=data['areaTree'][2]['children']
data_province

data_province[0].keys()

pd.DataFrame(data_province).head()


free_data=pd.DataFrame(data_province)[['id','lastUpdateTime','name']]
today_data=pd.DataFrame([province['today'] for province in data_province])
today_data.head()

free_data=pd.DataFrame(data_province)[['id','lastUpdateTime','name']]
total_data=pd.DataFrame([province['total'] for province in data_province])
total_data.head()

today_data.columns=('today_'+i for i in today_data.columns)
total_data.columns=('total_'+i for i in total_data.columns)

# id	lastUpdateTime	name	today_confirm	today_suspect	today_heal	today_dead	today_severe	today_storeConfirm	today_input	total_confirm	total_suspect	total_heal	total_dead	total_severe	total_input
# 0	420000	2020-05-24 08:25:38	湖北	NaN	NaN	NaN	NaN	NaN	NaN	NaN	68135	0	63616	4512	0	0
# 1	440000	2020-05-24 08:46:17	广东	NaN	NaN	NaN	NaN	NaN	NaN	NaN	1592	0	1580	8	0	0
# 2	410000	2020-05-24 09:18:06	河南	NaN	NaN	NaN	NaN	NaN	NaN	NaN	1276	0	1254	22	0	0
# 3	330000	2020-05-24 09:05:10	浙江	NaN	NaN	NaN	NaN	NaN	NaN	NaN	1268	0	1267	1	0	0

China_data=pd.concat([free_data,today_data,total_data],axis=1)
China_data

import time
file_name = 'China epidemic information'+'_'+time.strftime('%Y_%m_%d', time.localtime(time.time()))+'.csv'
China_data.to_csv(file_name, index=None, encoding='utf_8_sig')
print("success")


#American epidemic information get process
data_state=data['areaTree'][9]['children']
data_state

print(type(res.text))
print(len(res.text))

data_state[0].keys()
pd.DataFrame(data_state).head()

# today	total	extData	name	id	lastUpdateTime	children
# 0	{'confirm': None, 'suspect': None, 'heal': Non...	{'confirm': 369656, 'suspect': 0, 'heal': 2888...	{}	纽约	C2020040122094639	2020-05-24 15:07:20	[]
# 1	{'confirm': None, 'suspect': None, 'heal': Non...	{'confirm': 154713, 'suspect': 0, 'heal': 7405...	{}	新泽西	C2020040122094621	2020-05-24 15:12:43	[]
# 2	{'confirm': None, 'suspect': None, 'heal': Non...	{'confirm': 107796, 'suspect': 0, 'heal': 606,...	{}	伊利诺伊	C2020040122094642	2020-05-24 15:13:09	[]

free_data=pd.DataFrame(data_state)[['id','lastUpdateTime','name']]
total_data=pd.DataFrame([state['total'] for state in data_state])
total_data.head()

# 	confirm	suspect	heal	dead	severe
# 0	369656	0	28884	29112	0
# 1	154713	0	7405	11083	0
# 2	107796	0	606	4790	0
# 3	92535	0	2740	3759	0
# 4	91662	0	1299	6304	0

USA_data=pd.concat([free_data,total_data],axis=1)
USA_data

# id	lastUpdateTime	name	confirm	suspect	heal	dead	severe
# 0	C2020040122094639	2020-05-24 15:07:20	纽约	369656	0	28884	29112	0
# 1	C2020040122094621	2020-05-24 15:12:43	新泽西	154713	0	7405	11083	0
# 2	C2020040122094642	2020-05-24 15:13:09	伊利诺伊	107796	0	606	4790	0
# 3	C2020040122094651	2020-05-24 15:13:31	加利福尼亚	92535	0	2740	3759	0


import time
file_name = 'USA epidemic information'+'_'+time.strftime('%Y_%m_%d', time.localtime(time.time()))+'.csv'
USA_data.to_csv(file_name, index=None, encoding='utf_8_sig')
print("success")

# success