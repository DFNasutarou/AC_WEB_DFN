import requests
import json
import time
from collections import defaultdict

FOLDER_DATA = "data\\"
FOLDER_CRAWL_DATA = FOLDER_DATA + "crawl_data\\"
FOLDER_USER_DATA = FOLDER_DATA + "user_data\\"
FOLDER_VRC_DATA = FOLDER_DATA + "vrc_data\\"
FILE_CRAWL_SETTING = FOLDER_CRAWL_DATA + "crawl_setting.json"
FILE_CONTEST_INFO = FOLDER_CRAWL_DATA + "contest_info.json"
FILE_MONITOR_USER = FOLDER_VRC_DATA + "monitor_user.json"

KEY_USER_LIST = "user_list"
KEY_ROOM_MAP = "room_map"

# その時点での提出物 後ろにUNIX_TIMEが必要
URL_ALL_RESULT = "https://kenkoooo.com/atcoder/atcoder-api/v3/from/"
# 最新コンテスト情報
URL_CONTEST_INFO = "https://kenkoooo.com/atcoder/resources/contests.json"
# AtCoder上のcontests情報
URL_AC_CONTESTS = "https://atcoder.jp/contests/"

class ParseJson:
	@staticmethod
	def load_data(file_path):
		with open(file_path, "r", encoding="utf-8") as f:
			data_list = json.load(f)
		return data_list
	
	@staticmethod
	def save_data(file_path, data_list):
		with open(file_path, "w", encoding="utf-8") as f:
			json.dump(data_list, f, indent=2, ensure_ascii=False)

class UnixTime:
	@staticmethod
	def getNow():
		return time.time()
	
class AtcoderData:
	KEY_ID = "id"
	KEY_CONTEST_ID = "contest_id"
	KEY_PROBLEM_ID = "problem_id"
	KEY_USER_ID = "user_id"
	KEY_RESULT = "result"
	KEY_TIME = "epoch_second"
	KEY_START_TIME = "start_epoch_second"
	KEY_DURATION_SECOND = "duration_second"
	@staticmethod
	def get_contest_data(tm):
		"""
		指定したUNIX時間のコンテストデータを取得
		"""
		contest_url: str = URL_ALL_RESULT + str(tm)
		contest_data = requests.get(contest_url).json()
		return contest_data
	
	@staticmethod
	def get_user_data(tm, user_list):
		"""
		指定したUNIX時間の
		指定したユーザーのデータを取得
		"""
		contest_data = AtcoderData.get_contest_data(tm)
		result = defaultdict(list)
		for data in contest_data:
			user = data[AtcoderData.KEY_USER_ID]
			if user in user_list:
				d = {}
				d[AtcoderData.KEY_TIME] = data[AtcoderData.KEY_TIME]
				d[AtcoderData.KEY_PROBLEM_ID] = data[AtcoderData.KEY_PROBLEM_ID]
				d[AtcoderData.KEY_RESULT] = data[AtcoderData.KEY_RESULT]				
				result[user].append(d)
		print(result)

	@staticmethod
	def get_contest_info():
		"""
		コンテスト情報取得
		"""
		url = URL_CONTEST_INFO
		ifo = requests.get(url).json()
		ParseJson.save_data(FILE_CONTEST_INFO, ifo)
		return ifo

# ut = 1739016000
# monitor_user = ParseJson.load_data(FILE_MONITOR_USER)
# user_list = monitor_user[KEY_USER_LIST]
# print(user_list)
# AtcoderData.get_user_data(ut, user_list)

# ifo = AtcoderData.get_contest_info()
# ifo = ParseJson.load_data(FILE_CONTEST_INFO)
# tm = time.time()
# for data in ifo:
# 	print(tm, data)
# 	break
# 	if int(data[AtcoderData.KEY_START_TIME]) >= tm:
# 		print(data)

try:
	response = requests.get(URL_AC_CONTESTS)
	response.raise_for_status()
except requests.RequestException as e:
	print("ng")

print(response.text)