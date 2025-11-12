from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .models import Font


def home(request):
    
    return render(request, "index.html")# , {"a":a})


def generate_answer_sheet(request):
    # pass
    
    if request.method == "POST":
        start = int(request.POST.get('start'))
        name = str(request.POST.get('name'))
        def a(a):
            if start <a:
                return True
            else :
                return False

            
        test_count = request.POST.get("test_count")
        if request.POST.get('type') == 'linear':
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
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    text_lines.append(f)
                    text_lines.append(f)
                    text_lines.append(f)
                    

                    if n % 18 == 0 or (n + 1) % 18 == 0:

                        text_lines.append(True)
                        n=0
            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if a(100):
                w = y
                q=start
                while q < 10:
                    q += 1
                while w > 100:
                    w -= 1

                for i in range(q, w, 2):
                    n+=2
                    e = f'''{i}. ① ② ③ ④                                     |  {i+1}. ① ② ③ ④'''
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    text_lines.append(f)
                    text_lines.append(f)
                    text_lines.append(f)
                    if n % 18 == 0 or (n + 1) % 18 == 0:
                        text_lines.append(True)
                        
                        n=0
                        #c.showpage()
                #            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if a(1000):
                w = y
                while w > 1000:
                    w -= 1
                q=start
                while q < 100:
                    q += 1
                for i in range(q, w, 2):
                    n+=2
                    e = f'''{i}. ① ② ③ ④                                   |  {i+1}. ① ② ③ ④'''
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    text_lines.append(f)
                    text_lines.append(f)
                    text_lines.append(f)
                    if n % 18 == 0 or (n + 1) % 18 == 0:
                        n=0

                        text_lines.append(True)
                            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if a(10000):
                w = y
                while w > 10000:
                    w -= 1
                q=start
                while q < 1000:
                    q += 1
                for i in range(q, w, 2):
                    n+=2
                    e = f'''{i}. ① ② ③ ④                                |  {i+1}. ① ② ③ ④'''
                    f='.........................................................   |   .........................................................'
                    text_lines.append(e)
                    text_lines.append(f)
                    text_lines.append(f)
                    text_lines.append(f)
                    if n % 18 == 0 or (n + 1) % 18 == 0:
                        n=0

                        text_lines.append(True)
                            # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            if y % 2 ==0:
                e = f'''{y}. ① ② ③ ④                                       '''
                f='.........................................................   '
                text_lines.append(e)
                text_lines.append(f)
                text_lines.append(f)
                text_lines.append(f)

                if n % 18 == 0 or (n + 1) % 18 == 0:

                    text_lines.append(True)
        if request.POST.get('type') == 'simple':
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
                q=start
                while q < 10:
                    q += 1
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
                q=start
                while q < 100:
                    q += 1
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
                q=start
                while q < 1000:
                    q += 1
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
        a = Font.objects.all()
        for i in a:
            font_b64 = i.data_b64
        font_bytes = BytesIO(base64.b64decode(font_b64))
        pdfmetrics.registerFont(TTFont('Vazir', font_bytes))
        # تنظیمات صفحه
        width, height = (595, 842)  # A4
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=(width, height))
        draw_frame_and_watermark(c, width, height,name)
                
        c.setFont("Vazir", 14)
        y = 750
        # فرض کنیم text_lines از قبل تعریف شده
        for line in text_lines:
            if line is True:  # جداکننده‌ی صفحه جدید
                # قاب و واترمارک صفحه فعلی
                c.showPage()
                draw_frame_and_watermark(c, width, height,name)
                c.setFont("Vazir", 14)
                y = 750
            else:
                c.drawString(80, y, line)
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
    margin = 20
    c.setLineWidth(3)
    c.setStrokeColorRGB(0.2, 0.2, 0.2)
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

    # --- واترمارک ---
    c.saveState()
    c.setFont("Helvetica-Bold", 60)
    c.setFillColorRGB(0.85, 0.85, 0.85)
    c.translate(width / 2, height / 2)
    c.rotate(43)
    c.drawCentredString(0, 0, "answer-sheet.liara.run")
    c.drawCentredString(50, 57, a)
    c.restoreState()



# from django.conf import settings
# import os
# from .models import Font
# from django.shortcuts import redirect
# def a(request):
#     import base64
#     with open("C:\\Users\\1\\Desktop\\NotoSansSymbols-VariableFont_wght.ttf", "rb") as f:
#         font_data = f.read()

#     font_b64 = base64.b64encode(font_data).decode("utf-8")
#     Font.objects.create(data_b64=font_b64)
#     return redirect('home')