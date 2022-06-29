from aiohttp import payload_type
import psycopg2
#import pymysql
import pyimgur
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from flask import Flask, request, make_response, jsonify
from linebot import LineBotApi

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

#db = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='car', charset='utf8',autocommit=True)
# 使用 cursor() 方法建立一個指標物件 cursor
#cursor = db.cursor()

conn = psycopg2.connect (   database = "d9c2c2jfvm9j41",
                            user = "bxjoluxvhbsctk",
                            password = "e8c038377c3be9709be100f30e4cc5f177cad8074f96e93587e2e91875d84ef3",
                            host = "ec2-44-205-41-76.compute-1.amazonaws.com",
                            port = "5432"
                        )

cursor = conn.cursor()

def xi(keyword = None):
    
    cursor.execute("SELECT count(area) FROM member WHERE area = '{}'".format(keyword))
    accident_times = cursor.fetchall()

    cursor.execute("SELECT hurt FROM member WHERE hurt != '{}' and area = '{}'".format('0', keyword))
    hurt_times = cursor.fetchall()
    hurt_all = []
    for i in hurt_times:
        hurt_all.append(int(i[0]))


    cursor.execute("SELECT count(death) FROM member WHERE death = '{}' and area = '{}'".format('1', keyword))
    death_times = cursor.fetchall()

    cursor.execute("SELECT drink FROM member WHERE area = '{}'".format(keyword))
    bar_times = cursor.fetchall()
    
    bar = 0
    for i in bar_times:
        if(i[0] == '3' or i[0] == '4' or i[0] == '5' or i[0] == '6'):
            bar += 1

    msg = ""
    msg += "共發生:" + str(accident_times[0][0]) + "次車禍\n"
    msg += "共造成:" + str(sum(hurt_all)) + "人受傷\n"
    msg += "共造成:" + str(death_times[0][0]) + "人死亡\n"
    msg += "酒駕次數:" + str(bar) + "次"

    return msg


def eachtime(keyword = None):
    cursor.execute("SELECT hours, COUNT(hours) FROM member WHERE area = '{}' GROUP BY hours ORDER BY hours DESC".format(keyword))
    clock = cursor.fetchall()

    hours = []
    times = []
    for i in clock:
        hours.append(str(i[0]))

    for i in clock:
        times.append(i[1])

    fig = plt.figure()
    plt.bar(
            hours, # X資料
            times, # Y資料
            0.6, # bar寬度
            color='#7CA5B8' # bar顏色
            )
    plt.xlabel("時間")
    plt.ylabel("車禍次數")
    plt.title(keyword + "各時段對應車禍次數")
    fig.savefig('clock.png', dpi = fig.dpi)

    client_id ='0d519e46f026f35'
    path = 'clock.png'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)

    return upload_image.link

##各地區總車禍次數排行統計
def total():
    cursor.execute("SELECT area, COUNT(area) FROM member GROUP BY area ORDER BY COUNT(area) DESC")
    accident = cursor.fetchall()
        
    area = []
    times = []
    for i in accident:
        area.append(i[0])

    for i in accident:
        times.append(int(i[1]))

    fig = plt.figure()

    plt.title('各地車禍統計\n共' + str(sum(times)) + '次車禍')
    plt.bar(area, # X資料
            times, # Y資料
            0.6, # bar寬度
            color='#7CA5B8' # bar顏色
            )
         
    plt.xticks(rotation ='vertical')
    fig.savefig('total.png', dpi = fig.dpi)

    client_id ='0d519e46f026f35'
    path = 'total.png'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)

    return upload_image.link


##各地區死亡人數比例
def death():
    cursor.execute("SELECT area , COUNT(death) FROM member WHERE death = '{}' GROUP BY area ORDER BY COUNT(death) DESC".format('1'))
    death = cursor.fetchall()

    area = []
    times = []
    for i in death:
        area.append(i[0])

    for i in death:
        times.append(int(i[1]))

    fig = plt.figure()
    # 圓餅圖
    plt.pie(
            times , # 各數值比例
            labels = area , # 標籤
            autopct = '%1.1f%%' , # 數值格式
            pctdistance = 0.6 , 
            startangle = 90 # 轉向角度
            )
    plt.title('各地死亡占比\n共' + str(sum(times)) + '死')

    fig.savefig('death.png')

    client_id ='0d519e46f026f35'
    path = 'death.png'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path, title = '123')

    return upload_image.link

def acci_type():

    cursor.execute("SELECT type FROM member")
    accident_type = cursor.fetchall()

    type = []

    for i in accident_type:
        t = i[0]
        if(t != ''):
            t = int(t)
            if(t == 1):
                type.append("對向通行中")
            elif(t == 2):
                type.append("同向通行中")
            elif(t == 3):
                type.append("穿越道路中")
            elif(t == 4):
                type.append("在路上嬉戲")
            elif(t == 5):
                type.append("在路上作業")
            elif(t == 6):
                type.append("衝進路中")
            elif(t == 7):
                type.append("從停車後穿出")
            elif(t == 8):
                type.append("佇立路邊")
            elif(t == 9):
                type.append("其它")
            elif(t == 10):
                type.append("對撞")
            elif(t == 11):
                type.append("對向擦撞")
            elif(t == 12):
                type.append("同向擦撞")
            elif(t == 13):
                type.append("追撞")
            elif(t == 14):
                type.append("倒車撞")
            elif(t == 15):
                type.append("路口交叉撞")
            elif(t == 16):
                type.append("側撞")
            elif(t == 17):
                type.append("其它")
            elif(t == 18):
                type.append("路上翻車")
            elif(t == 19):
                type.append("衝出路外")
            elif(t == 20):
                type.append("撞護欄")
            elif(t == 21):
                type.append("撞號誌")
            elif(t == 22):
                type.append("撞收費亭")
            elif(t == 23):
                type.append("撞交通島")
            elif(t == 24):
                type.append("撞非固定設施")
            elif(t == 25):
                type.append("撞橋梁或建築物")
            elif(t == 26):
                type.append("撞路樹或電線桿")
            elif(t == 27):
                type.append("撞動物")
            elif(t == 28):
                type.append("工程施工")
            elif(t == 29):
                type.append("其它")

    words = " ".join(type)

    my_wordcloud = WordCloud(background_color = 'white', prefer_horizontal = 1, min_font_size = 10, width = 1080, height = 1080, font_path='jf-jinxuan-bold.otf').generate(words)

    fig = plt.figure()
    plt.imshow(my_wordcloud)
    plt.axis("off")

    fig.savefig('cloud.png')
    client_id ='0d519e46f026f35'
    path = 'cloud.png'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path, title = '123')

    return upload_image.link


app = Flask(__name__)


line_bot_api = LineBotApi('9stiBZCUuA2lqLd2MM3rRMHpvknAPg/6OCHAN9bLYDBTzePOD7hRLYcLm1ICQq6ZNwG9M04o1u0vicRZBfrBJQ4GNnkiY2akRzMlXI4VZTCIT8EVMiiXXKV8Y2fmyvvo/XvCKwdrfuOOV4STv0eo8AdB04t89/1O/w1cDnyilFU=')


@app.route('/', methods=['POST'])
def webhook():
    json = request.get_json(silent=True,force=True)
    
    cursor.execute("SELECT current FROM now")
    index = cursor.fetchone()

    res_message = {"fulfillmentText": None}
    
    if json['queryResult']['parameters']['any'] == "菜單":
        cursor.execute("UPDATE now SET current = %d" %(0))
        msg = ""
        msg += "以下為所有功能:\n"
        msg += "輸入 '車禍'\n"
        msg += "輸入 '時段'\n"
        msg += "輸入 '車禍次數'\n"
        msg += "輸入 '死亡比例'\n"
        msg += "輸入 '事故類型'\n"

        res_message = {"fulfillmentMessages": [ { "text": { "text": [msg] } } ] }

    ##功能 車禍列印
    elif json['queryResult']['parameters']['any'] == "車禍":
        cursor.execute("UPDATE now SET current = %d" %(1))
        cursor.execute("SELECT DISTINCT area FROM member")
        area = cursor.fetchall()
        msg = ""
        for i in area:
            msg += i[0] + '\n'
        res_message = {"fulfillmentText":"請輸入下列地區查找車禍詳情:" + '\n' + msg}

    elif json['queryResult']['parameters']['any'] == "時段":
        cursor.execute("UPDATE now SET current = %d" %(2))
        cursor.execute("SELECT DISTINCT area FROM member")
        area = cursor.fetchall()
        msg = ""
        for i in area:
            msg += i[0] + '\n'
        res_message = {"fulfillmentText":"請輸入下列地區幫您分析車禍時段:" + '\n' + msg}

    elif json['queryResult']['parameters']['any'] == "車禍次數": 
        msg = total()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 
        
    elif json['queryResult']['parameters']['any'] == "死亡比例":
        msg = death()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 
    
    elif json['queryResult']['parameters']['any'] == "事故類型":
        msg = acci_type()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 
        
    elif index[0] == 1:
        keyword = json['queryResult']['parameters']['any']
        msg = xi(keyword)
        res_message = {"fulfillmentMessages": [ { "text": { "text": [msg] } } ] }
        cursor.execute("UPDATE now SET current = %d" %(0))

    elif index[0] == 2:
        keyword = json['queryResult']['parameters']['any']
        msg = eachtime(keyword)
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 
        cursor.execute("UPDATE now SET current = %d" %(0))

    return make_response(jsonify(res_message))


if __name__ == "__main__":
    app.run(port=5000)





