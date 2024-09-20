from typing import Annotated
import os
from fastapi import FastAPI, File, UploadFile
from datetime import datetime
import pymysql.cursors

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    #파일 저장
    img = await file.read()
    file_name = file.filename
    upload_dir = "/Users/seon-u/photo"
    file_full_path = os.path.join(upload_dir, file_name)

    with open(file_full_path, 'wb') as f:
        f.write(img)


    #파일 저장 경로 DB INSERT
    #tablename : image_processing
    #컬럼 정보 : num (초기 인서트, 자동 증가)
    #컬럼 정보 : 파일이름, 파일경로, 요청시간(초기 인서트), 요청사용자(n00)
    #컬럼 정보 : 예측모델, 예측결과, 예측시간(추후 업데이트)

    connection = pymysql.connect(host="localhost",
                                 user='food',
                                 password='1234',
                                 database='imgdb',
                                 port=int(os.getenv(33306)),
                                 cursorclass=pymysql.cursors.DictCursor)
    sql = "INSERT INTO image_processing(`filename`, `file_full_path`, `dt`, `username`) VALUES(%s,%s,%s,%s)"

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(sql, (file.filename, file_full_path, datetime.now(), 'n01'))

        connection.commit()

    return {
            "filename": file.filename,
            "content_type": file.content_type,
            "file_full_path": file_full_path,
            "time": datetime.now()
            }
