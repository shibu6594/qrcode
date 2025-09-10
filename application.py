import streamlit as s
import qrcode 

s.title("QrCode Generated")

QRcod = s.text_input("Enter the URL")

makeqr = qrcode.make(QRcod)
file_name = s.text_input("Enter File Name : ")
if s.button('success'):
    
    makeqr.save(f"{file_name}.png")
    s.success("qr code genereted successfully")
    image_name = f"{file_name}.png"
    s.image(image_name)

a = "http://agastyaan.com"
qr = qrcode.make(a)
qr.save("ag.png")

