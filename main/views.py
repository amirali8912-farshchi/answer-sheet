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




def draw(black,c,x,y):
    # global iop
    # iop=60+(186*x)
    # for i in range(10):
    #     wer.append(iop)
    # global uio
    # uio=750
    x = 40+(186*x)          # فاصله از چپ
    y = 550-(240*y)          # فاصله از پایین
    width = 150      # عرض
    height = 220     # ارتفاع
    radius = 20      # میزان گردی گوشه‌ه
    #     م مستطیل با گوشه گرد
    c.setStrokeColor(black)
    c.setLineWidth(2)
    c.roundRect(x, y, width, height, radius, stroke=1, fill=0)
    # z+=50     
# ser=[0,1,2,3,4,5,6,7,8,9]
row={1:36,2:36,3:36,4:35,5:36,6:35,7:32,8:36,9:30,10:33,11:36,12:26,13:28,14:30,15:32,16:34}
ser=0
def home(request):
    
    return render(request, "index.html")# , {"a":a})


def generate_answer_sheet(request):
    # pass
    
    if request.method == "POST":
        rows = int(request.POST.get("rows"))
        tyype=request.POST.get('type')
        test_count = int(request.POST.get("test_count"))
        # print(test_count)
        name = str(request.POST.get('name'))
        start = int(request.POST.get('start'))
        types = request.POST.get('types', None)
        
        
        
        
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
        
        
        
        
        
        if True:#test_count-start>90:
            if test_count/90==test_count//90:
                pages=test_count//90
            elif test_count/90>test_count//90:
                pages=(test_count//90)+1
            for i in range(0,pages):
                # print(start,i)
                if i==0:
                    start-=90
                    c = canvas.Canvas(buffer, pagesize=(width, height))
                elif i!=0:
                    c.showPage()
                    
                draw_frame_and_watermark(c, width, height,name)

                c.setFont("Vazir", 16)
                start+=((90))
                # if i!=pages:
                #     test_count-=(i+1*90)
                print(i,start,i*90)
                response=main(buffer,c,types,start,name,test_count+1,tyype,rows)
        c.save()
        buffer.seek(0)
        # global response
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="answer_sheet.pdf"'
        return response


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


















def main(buffer,c,types,start,name,test_count,tyype,rows):
    z=0
    def a(a):
        if start <a:
            global q
            q=start
            while q < a//10:
                q += 1
            if start%2 ==1:
                q+=1
            return q
        else :
            return False
        
    if tyype == 'linear':
        types=None
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
                e = f'''{i}. ① ② ③ ④                                       |  {i+1}. ① ② ③ ④'''
                f='.........................................................   |   .........................................................'
                text_lines.append(e)
                for i in range(rows):
                    text_lines.append(f)
                # text_lines.append(f)
                # text_lines.append(f)
                
                # if n % 18 == 0 or (n + 1) % 18 == 0:
                # for as,ad in row.values(),row.keys()
                if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                    text_lines.append(True)
                    n=0
                # else:
                #     if ((rows+1)*((n//2)+1)) % 35 > 0 or ((rows+1)*(n+2)) % 35 > 0:
                #         pass
                #     else:
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
                e = f'''{i}. ① ② ③ ④                                     |  {i+1}. ① ② ③ ④'''
                f='.........................................................   |   .........................................................'
                text_lines.append(e)
                for i in range(rows):
                    text_lines.append(f)
                # if ((rows+1)*(n)) % 30 in ser and ((rows+1)*(n)) > 30 and ((rows+1)*(n+1)) % 30 not in ser:#or ((rows+1)*2*n) % 36 == 0:
                # for i in range(30,40):
                i=38
                if ((rows+1)*n) % row[rows] == 0 or ((rows+1)*n) % row[rows] == 0:
                    text_lines.append(True)
                    n=0
                # else:
                #     if ((rows+1)*((n//2)+1)) % 35 > 0 or ((rows+1)*(n+2)) % 35 > 0:
                #         pass
                #     else:
    #        text_lines.append(True)
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
                    text_lines.append(True)
                    n=0
                #     if ((rows+1)*((n//2)+1)) % 35 > 0 or ((rows+1)*(n+2)) % 35 > 0:
                #         pass
                #     else:
                      
                      
                      
                      
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
                    text_lines.append(True)
                    n=0
    if tyype == 'simple':
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
    if types=='second':
        text_lines = [
            ]
        for i in range(int(start),int(test_count)):
            text_lines.append(f'{i}. ① ② ③ ④')
    # print(text_lines)
    def wer(c,qi,text_lines):
        i=0
        b=0
        page=0
        n=0
        qwe={}
        for line in text_lines:
            # qi=int(text_lines.index(line))
            if types=='second':
                if line != ' k':
                    if i==0:
                        draw(black,c,i,b)
                    # if line[:2].isdigit():
                    if qi//10==qi/10:
                        draw(black,c,n,b)
                        page+=1
                        if qi//(30)!=qi/30 :#and not int(text_lines.index(line))>=30:
                            if qi>90:
                                pass
                            else:
                                qwe[qi]=f' '
                        
                        b+=1
                        if b%3==0:
                            b=0
                            n+=1
                        # qwe[i+1]='  '
                        # print(i)
                    # elif i%13==0:
                        # b+=1
                        # draw(black,c,b//5,b)
                        # qwe[i]=' '
                    # i=0
                    i+=1
            qi+=1
        vbn=0   
        bnm=0         
        for gh,jk in qwe.items():
            #if not (int(gh)+10+vbn+bnm)%34 ==0 or not (int(gh)+11+vbn+bnm)%34 ==0:
            text_lines.insert(int(gh)+vbn+bnm,jk)
            text_lines.insert(int(gh)+vbn,jk)
            vbn+=2
        qwe={}
            # bnm+=1
                        # .insert(i,i)
                # c.showPage()
        satar=60
        y=750
        n = {}
        for i in range(len(text_lines)):  # تعداد دلخواه
            n[i] = i + 1
        # print(n)
        for line in text_lines:   
            if line is True:  # جداکننده‌ی صفحه جدید
                # قاب و واترمارک صفحه فعلی
                c.showPage()
                draw_frame_and_watermark(c, width, height,name)
                c.setFont("Vazir", 16)
                y = 750
            else:
                if types=='second':
                    # wer
                    # ui
                    # print(wer,ui)
                        # print(text_lines)
                        c.drawString(satar, y, str(line))
                        y -= 20
                        # print(text_lines.index(text_lines[34])//34)
                        if text_lines.index(line)!=0:
                            jk=text_lines.index(line)
                            if n[int(jk)]%(34+0)==0 :#and text_lines.index(line)//34>=1:
                                y=750
                                satar+=186
                                # n+=1
                                # n=1
                else:
                    c.drawString(40, y, str(line))
                    y -= 20
            # if qi>(90*((page//9)+1)):
            #     break
        # آخرین صفحه هم قاب و واترمارک بگیرد
        # draw_frame_and_watermark(c, width, height,name)

    y = 750
    # فرض کنیم text_lines از قبل تعریف شده
    wer(c,0,text_lines)
    # if types=='second':
    #     for i in range(1,(len(text_lines)//102)):
    #             c.showPage()
    #             draw_frame_and_watermark(c, width, height,name)
    #             # c.setFont("Vazir", 16)
    #             # y = 750
    #             # print(text_lines[((90*i)-1):],((90*i)-1),i,len(text_lines)//90)
    #             # text_lines.append(True)
    #             wer(c,0,text_lines[((102*i)):])
    return buffer
    
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
