import psycopg2


conn = psycopg2.connect (   database = "d9c2c2jfvm9j41",
                            user = "bxjoluxvhbsctk",
                            password = "e8c038377c3be9709be100f30e4cc5f177cad8074f96e93587e2e91875d84ef3",
                            host = "ec2-44-205-41-76.compute-1.amazonaws.com",
                            port = "5432"
                        )

print("Opened database successfully")

cursor = conn.cursor()


cursor.execute( '''CREATE TABLE member
                (
                "day" VARCHAR(50) NOT NULL,
                "hours" INT NOT NULL,
                "min" VARCHAR(20) NOT NULL,
                "area" VARCHAR(20) NOT NULL,
                "death" VARCHAR(20) NOT NULL,
                "hurt" VARCHAR(20) NOT NULL,
                "type" VARCHAR(20) NOT NULL,
                "hurtlevel" VARCHAR(20) NOT NULL,
                "license" VARCHAR(20) NOT NULL,
                "drink" VARCHAR(20) NOT NULL,
                "run" VARCHAR(20) NOT NULL,
                "isue" VARCHAR(20) NOT NULL
                );'''
                )

conn.commit()
print("Create table successfully")
cursor.close()


cursor.execute("CREATE TABLE now (current INT NOT NULL);")
cursor.execute("INSERT INTO now (current) VALUES (0);")

conn.commit()
print("Create table successfully")
cursor.close()




