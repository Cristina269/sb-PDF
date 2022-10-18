import pdfplumber

def newline_character_abs():  # 摘要所有换行符位置
    file_path = r'test4.pdf'
    with pdfplumber.open(file_path) as pdf:
        num=len(pdf.pages[1].chars)
        a=[]
        b={}
        c=[]
        title=''
        for i in range(num):
            print(pdf.pages[0].chars[i]['size'],pdf.pages[0].chars[i]['text'])
            a.append(pdf.pages[0].chars[i]['size'])
        for i in range(num):
            if pdf.pages[0].chars[i]['size']==max(a):
                b[i]=pdf.pages[0].chars[i]['text']
                c.append(pdf.pages[0].chars[i]['text'])
            else:
                pass
        for i in range(len(c)):
            title=title+str(c[i])
        print(title)
        # pagetext = str(page0.extract_text())
        # print(page0.extract_text())

newline_character_abs()