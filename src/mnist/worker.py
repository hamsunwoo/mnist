import jigeum.seoul

def run():
  """image_processing 테이블을 읽어서 가장 오래된 요청 하나씩을 처리"""
  
  # STEP 1
  # image_processing 테이블의 prediction_result IS NULL 인 ROW 1 개 조회 - num 갖여오기

  from mnist.db import get_conn
  conn = get_conn()

  with conn:
      with conn.cursor() as cursor:
          sql = "SELECT * FROM image_processing
                WHERE prediction_result IS NULL ORDER BY num"
        cursor.execute(sql)
        result = cursor.fetchmany(size=1)

    return result

  # STEP 2
  # RANDOM 으로 0 ~ 9 중 하나 값을 prediction_result 컬럼에 업데이트
  # 동시에 prediction_model, prediction_time 도 업데이트

  # STEP 3
  # LINE 으로 처리 결과 전송

  print(jigeum.seoul.now())
