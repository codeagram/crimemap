import pymysql
import dbconfig

connection = pymysql.connect(host='localhost',
                            user=dbconfig.db_user,
                            password=dbconfig.db_password)


try:
    with connection.cursor() as cursor:

        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
        id int NOT NULL AUTO_INCREMENT,
        latitude float(10, 6),
        longtitude float(10, 6),
        date DATETIME,
        catagory varchar(50),
        description varchar(1000),
        updated_at TIMESTAMP,
        PRIMARY_KEY (id)
        """
        )
        cursor.execute(sql)

    connection.commit()

finally:
    connection.close()
