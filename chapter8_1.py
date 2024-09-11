import requests
import json

def fetch_data_from_api(api_url, params=None, headers=None):
    """
    API로부터 데이터를 가져옵니다.

    :param api_url: API 엔드포인트 URL
    :param params: 요청 파라미터 (기본값: None)
    :param headers: 요청 헤더 (기본값: None)
    :return: JSON 형식의 데이터 또는 None
    """
    try:
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # HTTP 오류 발생 시 예외를 발생시킵니다.
        return response.json()  # JSON 형식으로 응답 반환
    except requests.RequestException as e:
        print(f"요청 오류: {e}")
        return None

def save_to_json(data, filename):
    """
    데이터를 JSON 파일로 저장합니다.

    :param data: 저장할 데이터
    :param filename: 저장할 파일 이름
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# API 엔드포인트 URL과 파라미터 설정
api_url = 'api.edamam.com'  # 실제 API URL로 변경
params = {
    'param1': 'value1',
    'param2': 'value2'
}
headers = {
    'Authorization': 'live_YDUKc7X9sIc9bYTfsyFMZXef9JRL1u30kmZ14Oafzv3tfeu5ObQKoOVzY4BMM98r'  # 실제 API 키로 변경
}

# API에서 데이터 수집
data = fetch_data_from_api(api_url, params=params, headers=headers)

if data:
    # 수집한 데이터를 JSON 파일로 저장
    save_to_json(data, 'api.json')
    print("데이터 수집 및 저장 완료.")
else:
    print("데이터 수집 실패.")
