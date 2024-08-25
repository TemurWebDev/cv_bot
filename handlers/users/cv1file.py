from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_image_with_greeting(file_path, image_path,data):
    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFillColorRGB(*background_color_top)

    


    c.rect(0, 0, letter[0]-370, letter[1], fill=True)

    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))

    


    # Rasmni olish
    img = ImageReader(image_path)

    # Rasmni chap tarafga joylashtirish
    c.drawImage(img, 70, 620, width=110, height=130)

    ism = data['name']

    # O'ng tarafdagi matn
    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Times-Roman", 28)
    c.drawString(270,700, ism.split()[0].upper())


    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Times-Roman", 30)
    c.drawString(270,670, ism.split()[-1].upper())

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Times-Roman", 14)
    c.drawString(270,640, data['job'].upper())

    c.setFillColorRGB(0, 0, 1)  # kok rang
    c.setFont("Helvetica-Bold", 18)
    c.drawString(30,580, "Persanal Info")

    c.setFillColorRGB(0, 0, 1)  # kok rang
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30,550, "Tel:")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(120,550, f"{data['tel']}")

    c.setFillColorRGB(0, 0, 1)  # kok rang
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30,530, "Telegram:")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(120,530, f"@{data['username']}")

    c.setFillColorRGB(0, 0, 1)  # kok rang
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30,510, "Email:")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(120,510, f"{data['email']}")

    c.setFillColorRGB(0, 0, 1)  # kok rang
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30,490, "Addres:")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(120,490, f"{data['addres']}")


    c.setFillColorRGB(0, 0, 1)  # kok rang
    c.setFont("Times-Roman", 18)
    c.drawString(30,460, "Education")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(30,440, "TATU")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(30,420, "2019-2023 TATU studen")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(30,400, "2019/Sep - 2023/June")


    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(30,360, "TechSchool ")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(30,340, "Backend developer course")

    c.setFillColorRGB(1, 1, 1)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(30,320, "2022/Few - 2019/June")


    # c.setFillColorRGB(1, 1, 1)  # kok rang
    # c.setFont("Times-Roman", 12)
    # c.drawString(30,280, "Economics")

    # c.setFillColorRGB(1, 1, 1)  # kok rang
    # c.setFont("Times-Roman", 12)
    # c.drawString(30,260, "Academic Lyceium in Samarkand")

    # c.setFillColorRGB(1, 1, 1)  # kok rang
    # c.setFont("Times-Roman", 12)
    # c.drawString(30,240, "2016 - 2019")


    c.setFillColorRGB(0, 0, 1)  # kok rang
    c.setFont("Times-Roman", 18)
    c.drawString(30,200, "Skills")


    boshlash = 170
    skills = ["Python","Django","Django-rest-framevork","aiogram","postgres","doccer"]


    for skil in skills:
        c.setFillColorRGB(1, 1, 1)  # kok rang
        c.setFont("Times-Roman", 12)
        c.drawString(30,boshlash, skil)

        boshlash = boshlash - 20


    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Helvetica-Bold", 16)
    c.drawString(280,580, "Work Experience")

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(280,560, "Frelanser")

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(500,560, "09/2022-01/2024")

    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Helvetica-Bold", 12)
    c.drawString(280,540, "Freelancer on the Upwork.com platform")

    text1 = "Together with the Ktem team, we have completed many tasks on the upwork.com platform"

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Helvetica-Bold", 10)
    c.drawString(280,520, text1[:60])

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Helvetica-Bold", 10)
    c.drawString(280,500, text1[61:120])


    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(280,460, "Backend Developer")

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(500,460, "02/2023-01/2024")

    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Helvetica-Bold", 12)
    c.drawString(280,440, "In bazar online store")

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Helvetica-Bold", 10)
    c.drawString(280,420, "In bazar is a backend developer in an online store")

    # c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    # c.setFont("Helvetica-Bold", 10)
    # c.drawString(280,400, "Inspecting dining and serving areas, as well as all the equipment in")


    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(280,360, "It specialist")

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Times-Roman", 12)
    c.drawString(500,360, "08/2023-12/2023")

    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Helvetica-Bold", 12)
    c.drawString(280,340, "It specialist at Bayan Kids School")

    c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    c.setFont("Helvetica-Bold", 10)
    c.drawString(280,320, "I worked as an IT specialist at Bayan Kids School")

    # c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    # c.setFont("Helvetica-Bold", 10)
    # c.drawString(280,300, "Inspecting dining and serving areas, as well as all the equipment in")


    c.setFillColorRGB(0, 0, 0)  # kok rang
    c.setFont("Helvetica-Bold", 18)
    c.drawString(280,260, "Languages")

    boshlanishtil = 240
    language = ["English language","Russian language","Uzbek language"]


    for lan in language:
        c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
        c.setFont("Times-Roman", 10)
        c.drawString(280,boshlanishtil, lan)
        boshlanishtil = boshlanishtil - 20

    # c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    # c.setFont("Times-Roman", 10)
    # c.drawString(280,220, "Rus tili")

    # c.setFillColorRGB(0.5, 0.5, 0.5)  # kok rang
    # c.setFont("Times-Roman", 10)
    # c.drawString(280,200, "O'zbek tili")






    c.save()

# if __name__ == "__main__":

#     background_color_top = (0.23, 0.23, 0.23)

#     image_file_path = "cv2.jpg"
#     pdf_file_path = "filee6.pdf"
#     create_image_with_greeting(pdf_file_path, image_file_path)
#     print(f"PDF file created at: {pdf_file_path}")


background_color_top = (0.23, 0.23, 0.23)