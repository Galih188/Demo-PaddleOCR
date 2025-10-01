from paddleocr import PaddleOCR

# Inisialisasi OCR
ocr = PaddleOCR(
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

# Input gambar (lokal atau URL)
image_path = "contoh.jpg"
# jika menggunakan URL: "https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png"

# Jalankan prediksi OCR
result = ocr.predict(input=image_path)

# Menampilkan hasil di console
for res in result:
    res.print() 

    # Menyimpan hasil
    res.save_to_img("output")   # menyimpan gambar hasil (kotak + teks)
    res.save_to_json("output")  # menyimpan JSON hasil
