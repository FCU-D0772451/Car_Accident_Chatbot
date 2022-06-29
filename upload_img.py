import pyimgur


client_id ='0d519e46f026f35'
path = 'total.png'

im = pyimgur.Imgur(client_id)
upload_image = im.upload_image(path, title = '456')
print(upload_image.link)