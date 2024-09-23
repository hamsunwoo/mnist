import jigeum.seoul
import requests
import os

def run():
    """image_processing 테이블을 읽어서 가장 오래된 요청 하나씩을 처리"""
  
    # STEP 1
    # image_processing 테이블의 prediction_result IS NULL 인 ROW 1 개 조회 - num 갖여오기

    from mnist.db import get_conn
    from random import randrange
    conn = get_conn()

    with conn:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM image_processing WHERE prediction_result IS NULL ORDER BY num"
            cursor.execute(sql)
            result = cursor.fetchall() #모든 행을 가져옴

    # STEP 2
    # RANDOM 으로 0 ~ 9 중 하나 값을 prediction_result 컬럼에 업데이트
    # 동시에 prediction_model, prediction_time 도 업데이트

            for i in result:
                number = randrange(10)
                num_id = i["num"]
                sql = f"""
                        UPDATE image_processing
                        SET prediction_result = {number},
                            prediction_model = {number},
                            prediction_time = '{jigeum.seoul.now()}'
                        WHERE num = {num_id}
                        """
                cursor.execute(sql)
            
            conn.commit()
    
    
    # STEP 3
    # LINE 으로 처리 결과 전송
    KEY = os.environ.get('API_TOKEN')
    url = "https://notify-api.line.me/api/notify"
    data = {"message": "성공적으로 저장했습니다!"}
    headers = {"Authorization": f"Bearer {KEY}"}
    response = requests.post(url, data=data, headers=headers)

    print(jigeum.seoul.now())
    print(response.text)
    return True
