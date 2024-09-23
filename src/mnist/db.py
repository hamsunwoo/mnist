import pymysql.cursors

def get_conn():
    conn = pymysql.connect(host="b2f0495c2a99",
                            user='mnist',
                            password='1234',
                            database='mnistdb',
                            port=int(53306),
                            cursorclass=pymysql.cursors.DictCursor)

    return conn

def select(query:str, size= -1):
    conn = get_conn()
    with conn:
        with conn.cursor() as cursor:
          cursor.execute(query)
          result = cursor.fetchmany(size)

    return result

def dml(sql, *values):
    conn = get_conn()

    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
            conn.commit()

            return cursor.rowcount
