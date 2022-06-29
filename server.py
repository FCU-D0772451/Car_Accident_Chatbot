from flask import Flask, request, make_response, jsonify

import pyimgur
import random



## heruko
def morning():

    r = random.randrange(1, 7)


    client_id = '0d519e46f026f35'
    print(r)
    path = '早安/' + '長輩圖 ' + '(' + str(r) + ')' + '.jpg'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)

    return upload_image.link



def afternoon():

    r = random.randrange(1, 8)

    client_id = '0d519e46f026f35'
    print(r)
    path = '午安/' + '長輩圖 ' + '(' + str(r) + ')' + '.jpg'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)

    return upload_image.link

def goodnight():

    r = random.randrange(1, 7)

    client_id = '0d519e46f026f35'
    print(r)
    path = '晚安/' + '長輩圖 ' + '(' + str(r) + ')' + '.jpg'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)

    return upload_image.link


def hell():

    r = random.randrange(1, 8)

    client_id ='0d519e46f026f35'
    print(r)
    path = '地獄/' + '地獄 ' + '(' + str(r) + ')' + '.jpg'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)

    return upload_image.link

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def webhook():
    json = request.get_json(silent=True,force=True)

    res_message = {"fulfillmentText": None}
    
    if json['queryResult']['parameters']['any'] == "菜單":
        msg = ""
        msg += "以下為所有功能:\n"
        msg += "輸入 早安\n"
        msg += "輸入 午安\n"
        msg += "輸入 晚安\n"
        msg += "輸入 地獄\n"
        
        res_message = {"fulfillmentMessages": [ { "text": { "text": [msg] } } ] }

    elif json['queryResult']['parameters']['any'] == "早安":
    
        msg = morning()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 


    elif json['queryResult']['parameters']['any'] == "地獄":
    
        msg = hell()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 


    elif json['queryResult']['parameters']['any'] == "午安":
    
        msg = afternoon()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 
    
    elif json['queryResult']['parameters']['any'] == "晚安":
    
        msg = goodnight()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 

    return make_response(jsonify(res_message))


if __name__ == "__main__":
    app.run(port=5000)