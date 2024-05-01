import requests
import json
import csv
import pandas as pd

# 기존 코드에서 가져온 부분
UID = "u-s4t2ud-74766556a4e743fc75b26498d8f22e2c6444da37b87ddf898ea7fe883a3ddfd3"
SECRET = "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"
BASE_URL = "https://api.intra.42.fr"

auth = (UID, SECRET)
response = requests.post(f"{BASE_URL}/oauth/token", auth=auth, data={
    'grant_type': 'client_credentials',
    'client_id': UID,
    'client_secret': SECRET
})
response.raise_for_status()
token_data = response.json()
access_token = token_data["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

params = {
    "page[size]": "100",
    "page[number]": "1"

}

def get_as_corrector(user_id, page_number):
    params["page[number]"] = str(page_number)
    endpoint = f"/v2/users/{user_id}/scale_teams/as_corrector"
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_as_corrected(user_id, page_number):
    params["page[number]"] = str(page_number)
    endpoint = f"/v2/users/{user_id}/scale_teams/as_corrected"
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def count_word_occurrences(json_data, word):
    return json_data.lower().count(word)

def process_user(user_id):
    # "/v2/users/{user_id}/scale_teams/as_corrector" 엔드포인트에 대한 요청
    response_corrector1 = get_as_corrector(user_id, 1)
    # "/v2/users/{user_id}/scale_teams/as_corrected" 엔드포인트에 대한 요청
    response_corrected1 = get_as_corrected(user_id, 1)
    # JSON 응답을 가져와서 단어 개수 세기
    corrector_count = count_word_occurrences(json.dumps(response_corrector1), "corrector")
    corrected_count = count_word_occurrences(json.dumps(response_corrected1), "correcteds")

    response_corrector2 = get_as_corrector(user_id, 2)
    response_corrected2 = get_as_corrected(user_id, 2)
    corrector_count += count_word_occurrences(json.dumps(response_corrector2), "corrector")
    corrected_count += count_word_occurrences(json.dumps(response_corrected2), "corrected")

    return {
        "id": user_id,
        "corrector": corrector_count,
        "corrected": corrected_count
   }

# CSV 파일 작성 함수
def append_to_csv(data, filename):
    with open(filename, "a", newline="") as csvfile:
        fieldnames = ["id", "corrector", "corrected"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # 각 사용자에 대한 처리
        # CSV 파일에 데이터 작성
        writer.writerow(data)
        print(f"{data['id']} is appended")

# 유저 리스트 받아오기
def read_user_ids_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    # 첫 번째 열의 데이터를 읽어옴 (헤더 제외)
    user_ids = df.iloc[:, 0].tolist()
    return user_ids

user_ids = read_user_ids_from_csv("/Users/kimkangmin/user_data_campus_29_for_feedback.csv")

for user_id in user_ids:
    result_correct = process_user(user_id)
    append_to_csv(result_correct, "/Users/kimkangmin/Newuser_feedback_data.csv")

