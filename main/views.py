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

    return render(request, "index.html")


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
        if Help2==None:
            print(Help2,True)
            Help={0:0}
        else:
            print(Help2,False)
            Help=json.loads(Help2)

        #دریافت فونت از پایگاه داده
        pdfmetrics.registerFont(TTFont("font_ashkal", BytesIO(base64.b64decode(Font.objects.first().data_b64))))
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
                c.setFont("font_ashkal", 16)
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
                print(check(Help.keys(),test),Help.keys())
                if check(Help.keys(),test):
                    for i in range(0,int(Help[str(test)]),2):
                        how_many+=1
                        if int(Help[str(test)])>1:
                            if int(Help[str(test)])%2==1 and i+1==int(Help[str(test)]):
                                another_lines_last=True
                                first_line=f'''{test}) {abjad[i]} )   :......................{'              '[len(str(test))*2:]}|   {test+1})   :......................'''
                            elif i<int(Help[str(test)]):
                                another_lines_last=True
                                first_line=f'''{test+1}) {abjad[i]} )   :......................{'                   '[len(str(test+1))*2:]}|   {test+1}) {abjad[i+1]} )   :......................'''
                        else:
                            another_lines_last=True
                            first_line=f'''{test}) {abjad[i]} )   :......................{'              '[len(str(test))*2:]}|  {test+1})   :......................'''
                        text_lines.append(first_line)
                        another_lines = "S.........................................................   |   ........................................................."
                        another_lines_last=True
                        for _ in range(rows):
                            text_lines.append(another_lines)
                    how_many-=1
                elif check(Help.keys(),test+1):
                    how_many+=1
                    first_line=f'''{test} ) :......................{'                      '[len(str(test))*2:]}|  {test+1}) {abjad[0]} )   :......................'''
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
                                first_line=f'''{test+1}) {abjad[i]} )   :......................{'              '[len(str(test+1))*2:]}|   {test+1} )   :......................'''
                                text_lines.append(first_line)
                            elif i<int(Help[str(test+1)]):
                                another_lines_last=True
                                first_line=f'''{test+1}) {abjad[i]} )   :......................{'              '[len(str(test+1))*2:]}|   {test+1} ) {abjad[i+1]} )   :......................'''
                                text_lines.append(first_line)
                                another_lines = "D.........................................................   |   ........................................................."
                                for _ in range(rows):
                                    text_lines.append(another_lines)                    
                elif another_lines_last==False :
                    first_line=f"""{test})  :......................{'                     '[len(str(test))*2:]}|  {test+1} )  :......................"""
                    text_lines.append(first_line) 
                    
            else:
                first_line = f"""{test} ) ① ② ③ ④{'                                               '[len(str(test))*2:]}|  {test+1} ) ① ② ③ ④"""
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
                    c.setFont("font_ashkal", 16)
                elif types == "anatomical":
                    c.setFont("font_farsi", 16)
                column_y = 750
            else:
                if types == "Standard":
                    c.setFont("font_ashkal", 16)
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
                    k_x_2=0
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
                            k_x+=10+k_x_2
                            k_x_2+=10
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














