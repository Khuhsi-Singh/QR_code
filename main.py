import qrcode

# website = "https://chatgpt.com/"
# qr = qrcode.make(website)
# qr.save("qrcode.png")


website = input("Please paste the link of the website for which you want to generate QR code : ")
FillColor = input("Enter the fill color : ")
Backcolor = input("Enter the back color : ")

qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4  
)
qr.add_data(website)
qr.make(fit=True)

# qr = add_data(website)
# qr = qrcode.make(website)
img = qr.make_image(fill_color = FillColor, back_color = Backcolor)
img.save("Qrcode.png")
img.show()