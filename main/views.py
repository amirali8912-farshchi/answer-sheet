from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import Font

# ser=[0,1,2,3,4,5,6,7,8,9]
row={1:36,2:36,3:36,4:35,5:36,6:35,7:32,8:36,9:30,10:33,11:36,12:26,13:28,14:30,15:32,16:34}
ser=0
def home(request):
    
    return render(request, "index.html")# , {"a":a})


def generate_answer_sheet(request):
    # pass
    
    if request.method == "POST":
        start = int(request.POST.get('start'))
        name = str(request.POST.get('name'))
        def a(a):
            if start <a:
                global q
                q=start
                while q < a//10:
                    q += 1
                if start%2 ==1:
                    q+=1
                # print(q)
                return q
            else :
                return False

            
        test_count = request.POST.get("test_count")
        if request.POST.get('type') == 'linear':
            rows = int(request.POST.get("rows"))
            n=0
            #y=int(test_count)
            # متن شما (چند سطر)
            y=int(test_count)
            text_lines = [
            ]
            if a(10):
                
                w=y
                while w > 10:
                    w -= 1
                for i in range(start, w, 2):
                    n+=1
                    # print(rows,n)
                    e = f'''{i}. ① ② ③ ④                                       |  {i+1}. ① ② ③ ④'''
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    for i in range(rows):
                        text_lines.append(f)
                    # text_lines.append(f)
                    # text_lines.append(f)
                    

                    # if n % 18 == 0 or (n + 1) % 18 == 0:
                    # for as,ad in row.values(),row.keys()
                    print(row[rows] , rows )
                    if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                        # print(rows,n)

                        text_lines.append(True)
                        n=0
                    # else:
                    #     if ((rows+1)*((n//2)+1)) % 35 > 0 or ((rows+1)*(n+2)) % 35 > 0:
                    #         pass
                    #     else:
                    #         # print('''
                          
                          
                          
                          
                    #     #    ''',(((rows+1)*(n//2)) % 35 == 0) % 35)
                    #         text_lines.append(True)
                    #         n=0
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
            if a(100):
                q=a(100)
                w = y

                while w > 100:
                    w -= 1

                for i in range(q, w, 2):
                    n+=1
                    # print(rows,n)
                    e = f'''{i}. ① ② ③ ④                                     |  {i+1}. ① ② ③ ④'''
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    for i in range(rows):
                        text_lines.append(f)
                    # print('''
                          
                          
                    #       dadsdasasdsadsda
                          
                    #     #    ''',(rows+1)*((n//2)+1),(n//2)+1,n)
                    # if ((rows+1)*(n)) % 30 in ser and ((rows+1)*(n)) > 30 and ((rows+1)*(n+1)) % 30 not in ser:#or ((rows+1)*2*n) % 36 == 0:
                    # for i in range(30,40):
                    i=38
                    if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                        # print(rows,n)

                        text_lines.append(True)
                        n=0
                        # print(n)
                    # else:
                    #     if ((rows+1)*((n//2)+1)) % 35 > 0 or ((rows+1)*(n+2)) % 35 > 0:
                    #         pass
                    #     else:
                    #         print('''
                          
                          
                    #       dadsdasasdsadsda
                          
                    #        ''',(((rows+1)*(2*n)) % 35 == 0))
                    #         text_lines.append(True)
                    #         n=0
                #            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if a(1000):
                q=a(1000)
                w = y
                while w > 1000:
                    w -= 1
                # q=start
                # while q < 100:
                #     q += 1
                for i in range(q, w, 2):
                    n+=1
                    e = f'''{i}. ① ② ③ ④                                   |  {i+1}. ① ② ③ ④'''
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    for i in range(rows):
                        text_lines.append(f)
                    if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                        # print(rows,n)

                        text_lines.append(True)
                        n=0
                    #     if ((rows+1)*((n//2)+1)) % 35 > 0 or ((rows+1)*(n+2)) % 35 > 0:
                    #         pass
                    #     else:
                    #         print('''
                          
                          
                          
                          
                    #        ''',(((rows+1)*(n//2)) % 35 == 0) % 35)
                    #         text_lines.append(True)
                    #         n=0
                            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if a(10000):
                q=a(10000)
                w = y
                while w > 10000:
                    w -= 1
                # q=start
                # while q < 1000:
                #     q += 1
                for i in range(q, w, 2):
                    n+=1
                    e = f'''{i}. ① ② ③ ④                                |  {i+1}. ① ② ③ ④'''
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    for i in range(rows):
                        text_lines.append(f)
                    if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                        # print(rows,n)

                        text_lines.append(True)
                        n=0
                            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if start % 2 == 1 :
                if y %2 ==1:
                    e = f'''{y}. ① ② ③ ④                                       '''
                    f='.........................................................   '
                    text_lines.append(e)
                    for i in range(rows):
                        text_lines.append(f)
                    if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                        # print(rows,n)

                        text_lines.append(True)
                        n=0#rint('''
                          
                          
                          
                          
                        #    ''',((rows+1)*((n//2)+1)) % 35)
            else:
                if y % 2 == 0:
                    e = f'''{y}. ① ② ③ ④                                       '''
                    f='.........................................................   '
                    text_lines.append(e)
                    for i in range(rows):
                        text_lines.append(f)

                    if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                        # print(rows,n)

                        text_lines.append(True)
                        n=0
        if request.POST.get('type') == 'simple':
            types=request.POST.get('types')
            print(type(types))
            if types=='first':
                n=0
                #y=int(test_count)
                # متن شما (چند سطر)
                y=int(test_count)
                text_lines = [
                ]
                if a(10):
                    w=y
                    while w > 10:
                        w -= 1
                    for i in range(start, w, 2):
                        n+=2
                        e = f'''{i}. ① ② ③ ④                                       |  {i+1}. ① ② ③ ④'''
                        text_lines.append(e)
                        

                        if n % 65 == 0 or (n + 1) % 65 == 0:

                            text_lines.append(True)
                            n=0
                # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                if a(100):
                    w = y
                    q=a(100)
                    while w > 100:
                        w -= 1

                    for i in range(q, w, 2):
                        n+=2
                        e = f'''{i}. ① ② ③ ④                                     |  {i+1}. ① ② ③ ④'''
                        text_lines.append(e)
                        if n % 65 == 0 or (n + 1) % 65 == 0:
                            text_lines.append(True)
                            
                            n=0
                            #c.showpage()
                    #            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                if a(1000):
                    w = y
                    while w > 1000:
                        w -= 1
                    q=a(1000)
                    for i in range(q, w, 2):
                        n+=2
                        e = f'''{i}. ① ② ③ ④                                   |  {i+1}. ① ② ③ ④'''
                        text_lines.append(e)
                        if n % 65 == 0 or (n + 1) % 65 == 0:
                            n=0

                            text_lines.append(True)
                                # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # if y % 2 == 1:
                #     e = f'''{y}. ① ② ③ ④                                       '''
                #     text_lines.append(e)

                #     if n % 65 == 0 or (n + 1) % 65 == 0:

                #         text_lines.append(True)
                    #            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                if a(10000):
                    w = y
                    while w > 10000:
                        w -= 1
                    q=a(10000)
                    for i in range(q, w, 2):
                        n+=2
                        e = f'''{i}. ① ② ③ ④                                 |  {i+1}. ① ② ③ ④'''
                        text_lines.append(e)
                        if n % 65 == 0 or (n + 1) % 65 == 0:
                            n=0

                            text_lines.append(True)
                                # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                if start % 2 == 1 :
                    if y %2 ==1:
                        e = f'''{y}. ① ② ③ ④                                       '''
                        text_lines.append(e)
                else:
                    if y % 2 == 0:
                        e = f'''{y}. ① ② ③ ④                                       '''
                        text_lines.append(e)

                        if n % 65 == 0 or (n + 1) % 65 == 0:

                            text_lines.append(True)
        # elif types    
        from http.server import BaseHTTPRequestHandler, HTTPServer
        from io import BytesIO
        from reportlab.pdfgen import canvas
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        import webbrowser
        import os
        from django.conf import settings
        import base64
        
        
        
        # a=Font.objects.all()
        # for i in a:
        #     a=i.data_b64
        # font_bytes = BytesIO(base64.b64decode(a))
        # # ثبت فونت
        # pdfmetrics.registerFont(TTFont('Vazir', font_bytes))

        # # ایجاد PDF در حافظه
        # buffer = BytesIO()
        # c = canvas.Canvas(buffer, pagesize=(595, 842))  # A4
        # c.setFont("Vazir", 14)
        # y = 750
        #  # موقعیت عمودی شروع متن
        # for line in text_lines:
        #     if line == True:
        #         y = 750
        #         c.showPage()
        #         c.setFont("Vazir", 14)
        #     else:
        #         c.drawString(80, y, line)
        #         y -= 20 # فاصله بین خطوط
        #     # --- قاب در اطراف صفحه ---
        #     margin = 20
        #     c.setLineWidth(3)
        #     c.setStrokeColorRGB(0.2, 0.2, 0.2)  # خاکستری تیره
        #     c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

        #     # --- واترمارک ---
        #     c.saveState()
        #     c.setFont("Helvetica-Bold", 60)
        #     c.setFillColorRGB(0.9, 0.9, 0.9)  # خیلی روشن
        #     c.translate(width / 2, height / 2)
        #     c.rotate(45)
        #     c.drawCentredString(0, 0, "CONFIDENTIAL")
        #     c.restoreState()


        # c.showPage()
        # c.save()
        # buffer.seek(0)
        # response = HttpResponse(buffer, content_type='application/pdf')
        # response['Content-Disposition'] = 'inline; filename="answer_sheet.pdf"'  # نمایش در مرورگر
        # return response
        a = Font.objects.first()
        b = Font.objects.last()
        # for i in a:
        font_b64 = a.data_b64
        font_b63 = b.data_b64
        font_bytes = BytesIO(base64.b64decode(font_b64))
        font_byts = BytesIO(base64.b64decode(font_b63))
        pdfmetrics.registerFont(TTFont('Vazir', font_bytes))
        pdfmetrics.registerFont(TTFont('asd', font_byts))
        # تنظیمات صفحه
        width, height = (595, 842)  # A4
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=(width, height))
        draw_frame_and_watermark(c, width, height,name)
                
        c.setFont("Vazir", 16)
        y = 750
        # فرض کنیم text_lines از قبل تعریف شده
        for line in text_lines:
            if line is True:  # جداکننده‌ی صفحه جدید
                # قاب و واترمارک صفحه فعلی
                c.showPage()
                draw_frame_and_watermark(c, width, height,name)
                c.setFont("Vazir", 16)
                y = 750
            else:
                c.drawString(40, y, line)
                y -= 20
        # آخرین صفحه هم قاب و واترمارک بگیرد
        c.showPage()
        draw_frame_and_watermark(c, width, height,name)
        c.save()
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="answer_sheet.pdf"'
        return response


def draw_frame_and_watermark(c, width, height,a):
    # --- قاب ---
    # c.setFont("asd", 16)
    margin = 20
    c.setLineWidth(3)
    c.setStrokeColorRGB(0.2, 0.2, 0.2)
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

    # --- واترمارک ---
    
    import arabic_reshaper
    from bidi.algorithm import get_display
    import re

    def is_persian(text):
        return bool(re.search(r'[\u0600-\u06FF]', text))

    text = a   # یا مثلاً: CONFIDENTIAL

    if is_persian(text):
        reshaped_text = arabic_reshaper.reshape(text)
        final_text = get_display(reshaped_text)
    else:
        final_text = text
    c.saveState()
    c.setFont("asd", 60)
    c.setFillColorRGB(0.65, 0.65, 0.65)
    c.translate(width / 2, height / 2)
    c.rotate(43)
    c.drawCentredString(0, 0, "answer-sheet.liara.run")
    c.drawCentredString(50, 60, final_text)
    c.restoreState()
    c.setFont("Vazir", 16)











# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont


# c = canvas.Canvas("watermark.pdf", pagesize=A4)
# w, h = A4

# pdfmetrics.registerFont(TTFont('Vazir', 'Vazir.ttf'))
# c.setFont('Vazir', 40)

# c.saveState()
# c.translate(w/2, h/2)
# c.rotate(45)
# c.setFillAlpha(0.15)
# c.drawCentredString(0, 0, final_text)
# c.restoreState()

# c.save()

















# from django.conf import settings
# import os
# from .models import Font
# from django.shortcuts import redirect
# def a(request):
#     import base64
#     with open("C:\\Users\\1\\Desktop\\Almarai-Light.ttf", "rb") as f:
#         font_data = f.read()

#     font_b64 = base64.b64encode(font_data).decode("utf-8")
#     Font.objects.create(data_b64=font_b64)
#     return redirect('home')