#import pymysql
import pandas as pd
from datetime import datetime
import numpy as np
import csv
import psycopg2

 

conn = psycopg2.connect (   database = "d9c2c2jfvm9j41",
                            user = "bxjoluxvhbsctk",
                            password = "e8c038377c3be9709be100f30e4cc5f177cad8074f96e93587e2e91875d84ef3",
                            host = "ec2-44-205-41-76.compute-1.amazonaws.com",
                            port = "5432"
                        )

cursor = conn.cursor()


fp = open("11012.csv", "r", encoding="utf-8")
csv_reader = csv.reader(fp)
data = list(csv_reader)
fp.close()

for row in data[1:]:
    print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
    cursor.execute("INSERT INTO member(day, hours, min, area, death, hurt, type, hurtlevel, license, drink, run, isue) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11] ) )

conn.commit()
print("Create table successfully")
cursor.close()