import requests
import json

# AtCoderProblems API からデータ取得
contest_url = "https://kenkoooo.com/atcoder/resources/contests.json"
user_url = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=your_username"

contest_data = requests.get(contest_url).json()
user_data = requests.get(user_url).json()

# JSONファイルとして保存
with open("data/contests.json", "w", encoding="utf-8") as f:
    json.dump(contest_data, f, indent=4, ensure_ascii=False)

with open("data/user_results.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f, indent=4, ensure_ascii=False)
