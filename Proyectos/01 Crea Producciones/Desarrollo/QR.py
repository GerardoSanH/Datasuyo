import qrcode

# Contenido del código QR
data = "https://www.example.com"

# Crear instancia del objeto QRCode
qr = qrcode.QRCode(
    version=1,  # controla el tamaño del código QR (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controla el nivel de corrección de errores
    box_size=10,  # Tamaño de cada caja en el código QR
    border=4,  # Ancho del borde (en cajas)
)

# Agregar datos al QRCode
qr.add_data(data)
qr.make(fit=True)

# Crear una imagen del QRCode
img = qr.make_image(fill='black', back_color='white')

# Guardar la imagen
img.save("qrcode_example.png")

print("Código QR generado y guardado como qrcode_example.png")
