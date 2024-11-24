from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
app = Flask(__name__)

# NEIS API URL과 기본 파라미터
NEIS_API_URL = "https://open.neis.go.kr/hub/schoolInfo"
CORS(app)
@app.route('/proxy/schoolInfo', methods=['GET'])
def proxy_meal_service_diet_info():
    # 클라이언트 요청에서 전달받은 파라미터 가져오기
    params = {
        "ATPT_OFCDC_SC_CODE": 'E10',
        "SD_SCHUL_CODE": '7310068',
        "ORG_RDNMA": '인천광역시 연수구 능허대로 437',
        "type":"json"
    }

    try:
        # NEIS API로 요청 보내기
        response = requests.get(NEIS_API_URL, params=params)

        # 응답 반환 (status code와 데이터를 클라이언트로 전달)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        # 에러 발생 시 클라이언트로 에러 메시지 반환
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
