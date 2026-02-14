from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import Font
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import webbrowser
import os
from django.conf import settings
import base64
import arabic_reshaper
from bidi.algorithm import get_display
import re
from PIL import Image
import json
import numpy as np
import cv2



# ساخته تنها مونده
def last_child(tyype, text_lines, rows, how_many, types, test_count):
    if (tyype == "simple" and types == "inventive") or (tyype == "linear" and types == 'solution'):
        first_line = f"""{test_count}. ① ② ③ ④"""
        text_lines.append(first_line)
    elif tyype == "linear" and types == "anatomical":
        first_line = f"""{test_count}. :......................"""
        text_lines.append(first_line)
    if tyype == "linear":
        another_lines = "........................................................."
        for _ in range(rows):
            text_lines.append(another_lines)
        if ((rows + 1) * how_many) % row[rows] == 0:
            text_lines.append(True)
            how_many = 0
    return text_lines, how_many


# باکس های پاسخبرگ نوع استاندارد
def draw(black, c, x, y):
    x = 40 + (186 * x)  # فاصله از چپ
    y = 550 - (240 * y)  # فاصله از پایین
    width = 150  # عرض
    height = 220  # ارتفاع
    radius = 20  # میزان گردی گوشه‌ه
    #     م مستطیل با گوشه گرد
    c.setStrokeColor(black)
    c.setLineWidth(2)
    c.roundRect(x, y, width, height, radius, stroke=1, fill=0)


# بررسی توانایی جادادن سطر ها در هر سوال
row = {
    1: 36,
    2: 36,
    3: 36,
    4: 35,
    5: 36,
    6: 35,
    7: 32,
    8: 36,
    9: 30,
    10: 33,
    11: 36,
    12: 26,
    13: 28,
    14: 30,
    15: 32,
    16: 34,
}


# رندر کردن صفحه اول
def home(request):

    return render(request, "make.html")


# تولید پاسخبرگ
def generate_answer_sheet(request):

    if request.method == "POST":
        # دریافت ورودی ها
        rows = int(request.POST.get("rows", None))
        tyype = request.POST.get("tynpe", None)
        test_count = int(request.POST.get("test_count", None))
        name = str(request.POST.get("name", ' '))
        start = int(request.POST.get("start", None))
        types = request.POST.get("types", None)
        Help2=request.POST.get("help",None)
        if Help2!=None:
            Help={0:0}
        else:
            Help=json.loads(Help2)

        #دریافت فونت از پایگاه داده
        pdfmetrics.registerFont(TTFont("font_askal", BytesIO(base64.b64decode(Font.objects.first().data_b64))))
        pdfmetrics.registerFont(TTFont("font_farsi", BytesIO(base64.b64decode(Font.objects.last().data_b64))))
        # تنظیمات صفحه
        width, height = (595, 842)  # A4
        buffer = BytesIO()

        # در صورتی که کاربر نوع استاندارد بخواهد تولید صفحات خالی مورد نیاز وبعد ارسال به تابع اصلی
        if types == "Standard":
            if (test_count-start) / 90 == (test_count-start) // 90:
                pages = (test_count-start) // 90
            elif (test_count-start) / 90 > (test_count-start) // 90:
                pages = ((test_count-start) // 90) + 1
            for i in range(0, pages):
                if i == 0:
                    start -= 90
                    c = canvas.Canvas(buffer, pagesize=(width, height))
                elif i != 0:
                    c.showPage()

                draw_frame_and_watermark(c, width, height, name)

                start += 90
                response = main(
                    Help,
                    height,
                    width,
                    buffer,
                    c,
                    types,
                    start,
                    name,
                    test_count + 1,
                    tyype,
                    rows,
                )
        # در صورت عادی بودن
        else:
            c = canvas.Canvas(buffer, pagesize=(width, height))
            draw_frame_and_watermark(c, width, height, name)
            if tyype == "simple" or (tyype == "linear" and types == "solution"):
                c.setFont("font_askal", 16)
            elif types == "anatomical":
                c.setFont("font_farsi", 16)
            response = main(
                Help,height, width, buffer, c, types, start, name, test_count, tyype, rows
            )
        # ذخیره pdf
        c.save()
        buffer.seek(0)
        # ارسال به کاربر
        response = HttpResponse(buffer, content_type="application/pdf")
        response["Content-Disposition"] = f'inline; filename="answer_sheet.pdf"'
        # خالی کردن خافظه
        del buffer, c,Help 
        import gc

        gc.collect()
        #بازگرداندن پاسخ
        return response


# -----------------------------------------------------------------------------------------------------------

# تعریف فونت های مورد نیاز
# from django.conf import settings
# import os
# from .models import Font
# from django.shortcuts import redirect
# def a(request):
#     import base64
#     with open("C:\\Users\\1\\Downloads\\Telegram Desktop\\Mj_Fossil.ttf", "rb") as f:
#         font_data = f.read()

#     font_b64 = base64.b64encode(font_data).decode("utf-8")
#     Font.objects.create(data_b64=font_b64)
#     return redirect('home')

# -----------------------------------------------------------------------------------------------------------

# تابع بررسی لیست
def check(List,data):
    for i in List:
        if int(data)==int(i):
            is_valid=True
            return is_valid
        else:
            is_valid=False
    return is_valid
    
# بدنه اصلی کد
def main(Help,height, width, buffer, c, types, start, name, test_count, tyype, rows):
    # تولید پاسخبرگ خط دار
    if tyype == "linear" or (tyype == "simple", types == "inventive"):
        how_many = 0
        test_count = int(test_count)
        text_lines = []
        abjad = ['ا', 'ب', 'ج', 'د', 'ه', 'و', 'ز', 'ح', 'ط', 'ی', 'ک', 'ل', 'م', 'ن', 'س', 'ع', 'ف', 'ص', 'ق', 'ر', 'ش', 'ت', 'ث', 'خ', 'ذ', 'ض', 'ظ', 'غ']
        
        Start = start
        test=Start
        while test<test_count:
            print(Help,test)
            another_lines_last=False
            how_many += 1
            if types == "anatomical":
                print(check(Help.keys(),7),Help.keys())
                if check(Help.keys(),test):
                    for i in range(0,int(Help[str(test)]),2):
                        how_many+=1
                        if int(Help[str(test)])>1:
                            if int(Help[str(test)])%2==1 and i+1==int(Help[str(test)]):
                                another_lines_last=True
                                first_line=f'''{test}) {abjad[i]} )   :......................{'              '[len(str(test))*2:]}|{test+1})   :......................'''
                            elif i<int(Help[str(test)]):
                                another_lines_last=True
                                first_line=f'''{test}) {abjad[i]} )   :......................{'              '[len(str(test))*2:]}|{test}) {abjad[i+1]} )   :......................'''
                        else:
                            another_lines_last=True
                            first_line=f'''{test}) {abjad[i]} )   :......................{'              '[len(str(test))*2:]}|{test+1})   :......................'''
                        text_lines.append(first_line)
                        another_lines = "S.........................................................   |   ........................................................."
                        another_lines_last=True
                        for _ in range(rows):
                            text_lines.append(another_lines)
                    how_many-=1
                elif check(Help.keys(),test+1):
                    how_many+=1
                    first_line=f'''{test}.:......................{'              '[len(str(test))*2:]}|{test+1}) {abjad[0]} )   :......................'''
                    text_lines.append(first_line)
                    another_lines = "A.........................................................   |   ........................................................."
                    another_lines_last=True          
                    for _ in range(rows):
                        text_lines.append(another_lines)                    
                    if int(Help[str(test+1)])>1 :
                        for i in range(1,int(Help[str(test+1)]),2):
                            how_many+=1
                            if  int(Help[str(test+1)])%2==1  and i==int(Help[str(test+1)]):
                                p=1
                                first_line=f'''{test}) {abjad[i]} )   :......................{'              '[len(str(test))*2:]}|{test+1})   :......................'''
                                text_lines.append(first_line)
                            # elif int(Help[str(test+1)])%2==0  and i<int(Help[str(test+1)]):
                            elif i<int(Help[str(test)]):
                                another_lines_last=True
                                first_line=f'''{test}) {abjad[i]} )   :......................{'              '[len(str(test))*2:]}|{test}) {abjad[i+1]} )   :......................'''
                                text_lines.append(first_line)
                                another_lines = "D.........................................................   |   ........................................................."
                                for _ in range(rows):
                                    text_lines.append(another_lines)                    
                elif another_lines_last==False :
                    first_line=f"""{test})  :......................{'                '[len(str(test))*2:]}|  {test+1} )  :......................"""
                    text_lines.append(first_line)
                    
            else:
                first_line = f"""{test} ) ① ② ③ ④{'                                         '[len(str(test))*2:]}|  {test+1} ) ① ② ③ ④"""
                text_lines.append(first_line)
            if tyype == "linear" and another_lines_last==False:
                another_lines = "L.........................................................   |   ........................................................."
                for _ in range(rows):
                    text_lines.append(another_lines)

            if (tyype == "linear" and ((rows + 1) * how_many) % row[rows] == 0) or (
                tyype == "simple" and how_many % 35 == 0
            ):
                text_lines.append(True)
                how_many = 0
            test+=2
        if start % 2 == 1:
            if test_count % 2 == 1:
                out_put = list(
                    last_child(tyype, text_lines, rows, how_many, types, test_count)
                )
                text_lines, how_many = out_put[0], out_put[1]
        else:
            if test_count % 2 == 0:
                text_lines, how_many = last_child(
                    tyype, text_lines, rows, how_many, types, test_count
                )
    if tyype == "simple" and types == "Standard":
        text_lines = []
        for test in range(int(Start), int(test_count)):
            text_lines.append(f"{test}) ① ② ③ ④")
    #Making box for tests 
    def mbft(c, text_lines):
        # Nomber for box : nfb
        nfb = 0
        row = 0
        page = 0
        column = 0
        #finish of box
        fob = {}
        for line in text_lines:
            if types == "Standard":
                if line != "":
                    if nfb == 0:
                        draw(black, c, column, row)
                    if nfb // 10 == nfb / 10:
                        draw(black, c, column, row)
                        page += 1
                        if (nfb // (30) != nfb / 30):
                            if nfb > 90:
                                pass
                            else:
                                fob[nfb] = ""

                        row += 1
                        if row % 3 == 0:
                            row = 0
                            column += 1
            nfb += 1
        #پس از رفع ارور متغیر eror اضافه شد
        eror = 0
        for nfb, _ in fob.items():
            text_lines.insert(int(nfb)+eror  , '')
            text_lines.insert(int(nfb)+eror , '')
            eror += 2
        fob = {}
        row_x = 60
        column_y = 750
        for line in text_lines:
            if line is True:  # جداکننده‌ی صفحه جدید
                # قاب و واترمارک صفحه فعلی
                c.showPage()
                draw_frame_and_watermark(c, width, height, name)
                if tyype == "simple" or (tyype == "linear" and types == "solution"):
                    c.setFont("font_askal", 16)
                elif types == "anatomical":
                    c.setFont("font_farsi", 16)
                column_y = 750
            else:
                if types == "Standard":
                    c.setFont("font_askal", 16)
                    c.drawString(row_x, column_y, str(line))
                    column_y -= 20
                    if text_lines.index(line) != 0:
                        #Number of test
                        nt = text_lines.index(line)
                        if ((int(nt)+1) % (34) == 0):
                            column_y = 750
                            row_x += 186
                elif types == "anatomical":
                    reshaped_text = arabic_reshaper.reshape(str('جواب نهایی'))
                    final_text = get_display(reshaped_text)
                    k_x=40
                    is_last_Number=False
                    is_dot=False
                    for k in line:
                        reshaped_text = arabic_reshaper.reshape(str('جواب نهایی'))
                        final_text = get_display(reshaped_text)

                        if k=='.' or k==':' or k==' '  or k==')' or k=='|':
                            is_dot=True
                            c.drawString(k_x, column_y, k)
                            k_x+=4
                        if k in abjad or k=='ا' :
                            k_x_2=0
                            if k=='ا' :
                                k='الف'
                                k_x_2+=10
                            reshaped_text = arabic_reshaper.reshape(str(k))
                            final_text = get_display(reshaped_text)
                            c.drawString(k_x, column_y, final_text)
                            k_x+=9+k_x_2
                            reshaped_text = arabic_reshaper.reshape(str('جواب نهایی'))
                            final_text = get_display(reshaped_text)
                            
                        if k.isdigit():
                            is_last_Number=True
                            c.drawString(k_x, column_y, k)
                            k_x+=6
                        
                        if is_last_Number :
                            try:
                                data=str(line)[str(line).index(k)+1]
                            except:
                                data=0

                            if data=='.':
                                k_x+=5
                                c.drawString(k_x, column_y, final_text)
                                k_x+=49
                                is_last_Number=False
                                is_dot=False                            
                    column_y -= 20  
                else:
                    c.drawString(40, column_y, line)                
                    column_y -= 20  
    column_y = 750
    #صدازدن تابع تولید و بررسی پاسخبرگ استاندارد
    mbft(c,  text_lines)
    return buffer


def draw_frame_and_watermark(c, width, height, text):
    # --- قاب ---
    margin = 20
    c.setLineWidth(3)
    c.setStrokeColorRGB(0.2, 0.2, 0.2)
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)



    # --- واترمارک ---
    def is_persian(text):
        return bool(re.search(r"[\u0600-\u06FF]", text))

#فارسی سازی واتر مارک
    if is_persian(text):
        reshaped_text = arabic_reshaper.reshape(text)
        final_text = get_display(reshaped_text)
    else:
        final_text = text
    #تولید واتر مارک
    c.saveState()
    c.setFont("font_farsi", 60)
    c.setFillColorRGB(0.65, 0.65, 0.65)
    c.translate(width / 2, height / 2)
    c.rotate(43)
    c.drawCentredString(0, 0, "answer-sheet.liara.run")
    c.drawCentredString(50, 60, final_text)
    c.restoreState()















def correction(request):
    return render(request, "check.html")
def check(request):
    selected={}
    if request.method == "POST":
        print(request.FILES)
        image=cv2.imdecode(np.asarray(bytearray(request.FILES['img'].read()),dtype=np.uint8),cv2.IMREAD_COLOR)
        how_man=30
        colum=3
        for i in range(0,colum):
            for r in range(1,how_man+1):
                selected[r+(i*30)]=checking([((15*r)+38,(150*i)+50),((15*r)+38,(150*i)+67),((15*r)+38,(150*i)+84),((15*r)+38,(150*i)+98)],image)
        print(selected)
        # checking([(53,114),(68,114),(85,114),(99,114)],image)
        return render(request,'index.html')
def checking(centers,image):
    # image = cv2.imread("C:\\Users\\1\\Desktop\\ocr\\ocr.jpg")
    # centers=[
    # (53,114)
    # ,(68,114)
    # ,(85,114)
    # ,(99,114)]
    orig = image.copy()

    # 1) Gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2) Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3) Edge Detection
    edges = cv2.Canny(blur, 50, 150)

    # 4) Find Contours
    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # 5) Largest Rectangle
    largest = None
    max_area = 0

    for c in contours:
        area = cv2.contourArea(c)

        if area > max_area:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            if len(approx) == 4:
                largest = approx
                max_area = area

    if largest is None:
        print(":x: Page not detected!")
        exit()

    pts = largest.reshape(4, 2).astype("float32")

    # 6) Sort Points
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    tl = pts[np.argmin(s)]
    br = pts[np.argmax(s)]
    tr = pts[np.argmin(diff)]
    bl = pts[np.argmax(diff)]

    ordered = np.array([tl, tr, br, bl], dtype="float32")

    # 7) Warp
    W, H = 800, 1100

    dst = np.array([
        [0, 0],
        [W, 0],
        [W, H],
        [0, H]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(ordered, dst)
    aligned = cv2.warpPerspective(orig, M, (W, H))

    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("Clicked at:", x, y)
    # 8) Output
    aligned=cv2.resize(aligned,(432, 613))




    def detect_choice(image, centers):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 3) threshold (سیاه سفید معکوس)
        thresh = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )[1]

        
        marked = None
        max_black = 0
        print(centers,enumerate(centers))
        for i, (x, y) in enumerate(centers):

            roi = thresh[y-10:y+10, x-10:x+10]

            black_pixels = cv2.countNonZero(roi)
            cv2.circle(image,(x, y),5,(0,0,255))
            if black_pixels > max_black:
                max_black = black_pixels
                marked = i+1   # گزینه شماره
            print('klklkkl',black_pixels)
        #if max_black
        

        return marked
    print(1)
    return detect_choice(aligned, centers)




    # image=cv2.resize(image,(432, 613))
    # cv2.imwrite("aligned.jpg", aligned)

    # cv2.imshow("Aligned", aligned)
    # cv2.imshow("Aled", image)
    # cv2.setMouseCallback("Aligned", click_event)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # print(":white_check_mark: Done! Saved aligned.jpg")    