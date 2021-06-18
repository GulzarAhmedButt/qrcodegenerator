import qrcode

input_link = "https://www.youtube.com/channel/UC1DvCS2RaGZPOI1387rwvyA"

qr = qrcode.QRCode(version=1,box_size=10,border=5)

qr.add_data(input_link)
qr.make(fit=True)

img = qr.make_image()
img.save('myyoutubecode.png')