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
        
        
        
        a=Font.objects.all()
        for i in a:
            a=i.data_b64
        font_bytes = BytesIO(base64.b64decode(a))
        # ثبت فونت
        pdfmetrics.registerFont(TTFont('Vazir', font_bytes))

        # ایجاد PDF در حافظه
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=(595, 842))  # A4
        c.setFont("Vazir", 14)
        y = 750
         # موقعیت عمودی شروع متن
        for line in text_lines:
            if line == True:
                y = 750
                c.showPage()
                c.setFont("Vazir", 14)
            else:
                c.drawString(80, y, line)
                y -= 20 # فاصله بین خطوط

        c.showPage()
        c.save()
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="answer_sheet.pdf"'  # نمایش در مرورگر
        return response
        # سرور HTTP موقت
        # class PDFHandler(BaseHTTPRequestHandler):
        #     def do_GET(self):
        #         self.send_response(200)
        #         self.send_header('Content-type', 'application/pdf')
        #         self.end_headers()
        #         self.wfile.write(buffer.getvalue())

        # server = HTTPServer(('localhost', 1234), PDFHandler)
        # webbrowser.open("http://localhost:1234")
        # server.serve_forever()
        # import time
        # time.sleep(6)
        # server.shotdown()








#        filename = request.POST.get("filename", "answer_sheet")
#
#        # اعتبارسنجی
#        if not test_count or not test_count.isdigit():
#            return HttpResponse("تعداد تست نامعتبر است", status=400)
#
#        y = int(test_count)
#
#        # ساخت فایل PDF در حافظه
#        buffer = BytesIO()
#        p = canvas.Canvas(buffer, pagesize=A4)
#        width, height = A4
#
#        p.setFont("Helvetica", 12)
#        p.drawString(200, height - 50, "پاسخ‌برگ")
#
#        x_left = 50
#        x_right = 300
#        y_pos = height - 100
#        step = 40  # فاصله بین ردیف‌ها
#
#        for i in range(1, y + 1, 2):
#            # شماره و گزینه‌ها در سمت چپ
#            p.drawString(x_left, y_pos, f'''{i}. ① ② ③ ④
#    ................................
#    ................................
#    ................................
#    ''')
#            if i + 1 <= y:
#                # شماره و گزینه‌ها در سمت راست
#                p.drawString(x_right, y_pos, f'''{i+1}. ① ② ③ ④
#    ................................
#    ................................
#    ................................
#    ''')
#
#            y_pos -= step
#            if y_pos < 50:  # اگه صفحه پر شد برو صفحه بعد
#                p.showPage()
#                p.setFont("Helvetica", 12)
#                y_pos = height - 50
#
#        p.save()
#
#        buffer.seek(0)
#
#        # نمایش مستقیم PDF در مرورگر (بدون دانلود اجباری)
#        return HttpResponse(buffer, content_type="application/pdf")
#




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