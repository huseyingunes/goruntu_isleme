import easyocr

reader = easyocr.Reader(['tr'])
result = reader.readtext('resim/metin.jpg')

print(result)
