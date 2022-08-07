import pdfplumber


# 翻译摘要就算成功...

def all_newline(page_number=1):
    newline = [0, 1]
    file_path = r'test.pdf'
    with pdfplumber.open(file_path) as pdf:
        all_page_number = len(pdf.pages[:])
        if page_number == 1:
            while newline[-1] != -1:
                page0_1 = str(pdf.pages[0].extract_text())
                newline.append(page0_1.find('\n', newline[-1] + 1))
            del (newline[0])
            del (newline[0])
            del (newline[-1])
            return newline
        else:
            # TODO 完善根据页码返回功能，目前默认第一页
            pass
def all_balck(page_number=1):
    two = [0, 1]
    three =[0,1]
    file_path = r'test.pdf'
    with pdfplumber.open(file_path) as pdf:
        all_page_number = len(pdf.pages[:])
        if page_number == 1:
            while two[-1] != -1:
                page0_1 = str(pdf.pages[0].extract_text())
                two.append(page0_1.find('  ', two[-1] + 1))
            del (two[0])
            del (two[0])
            del (two[-1])
    with pdfplumber.open(file_path) as pdf:
        all_page_number = len(pdf.pages[:])
        if page_number == 1:
            while three[-1] != -1:
                page0_1 = str(pdf.pages[0].extract_text())
                three.append(page0_1.find('   ', three[-1] + 1))
            del (three[0])
            del (three[0])
            del (three[-1])
        else:
            # TODO 完善根据页码返回功能，目前默认第一页
            pass
    return two,three
# 返回了所有双三空格

def returns_intersection(pagetext,black_new,start_abstract,end_abstract):
    front = []
    back = []
    while 1:  # 返回在这一行之间的换行符的位置
        for i in range(len(black_new)):
            if int(black_new[i]) < start_abstract:
                front.append(i)
            elif int(black_new[i]) > end_abstract:
                back.append(i)
            else:
                pass
        break
    re_newline = black_new[len(front):len(black_new) - len(back)]  # 两个元素之间是一行
    print(re_newline)

def main():
    file_path = r'test.pdf'
    with pdfplumber.open(file_path) as pdf:
        page0 = pdf.pages[0]
        # print(page0.extract_text())
        # Chemosphere 摘要开始与结束
        # 格式化为str,这是没有动过的原文。
        pagetext = str(page0.extract_text())
        # 只能循环两次
        while 1:
            start_abstract = int(
                page0.extract_text().find('A B S T R A C T', 1))  # page0.extract_text().find('A B S T R A C T')+1))
            end_abstract = int(page0.extract_text().find('* Corresponding author.'))
            if pagetext[start_abstract - 3] == 'L':
                start_abstract = int(
                    page0.extract_text().find('A B S T R A C T', page0.extract_text().find('A B S T R A C T') + 1))
                break
            else:
                break
        newline = all_newline()
        # start_abstract+15,end_abstract
        # TODO 查找一行一个或两个的单词 特征是 一行之间空格少于三个（大概
        # 先获取abs那一段文字，然后找里面的换行符并获取位置，
        o_abstract = pagetext[start_abstract + 16:end_abstract]
        front = []
        back = []
        remember_to_delete=[]
        while 1:    #返回在这一行之间的换行符的位置
            for i in range(len(newline)):
                if int(newline[i]) < start_abstract:
                    front.append(i)
                elif int(newline[i]) > end_abstract:
                    back.append(i)
                else:
                    pass
            break
        re_newline = newline[len(front):len(newline) - len(back)]   #两个元素之间是一行
        for i in range(len(re_newline)):
            try:
                a=pagetext.count(' ',re_newline[i],re_newline[i+1])
                if a < 4:
                    #pagetext=str(pagetext[:re_newline[4]])+str(pagetext[:re_newline[4]])
                    remember_to_delete.append(str(pagetext[re_newline[i]:re_newline[i+1]]))
                    print(remember_to_delete)
            except:
                pass
        #要删除的文字在最后一块删


        # TODO 和主体不是一块的内容，特征是多余一个的空格，并删除所在位置与前一个空格之间的单词，或者是与前一个换行符之间的单词

        # 去除换行符
        two,three= all_balck()
        print(two)
        abstract = pagetext[start_abstract + 16:end_abstract]  # .replace("\n", "")
        print(abstract)


#if __name__ == '__main__':
file_path = r'test.pdf'
with pdfplumber.open(file_path) as pdf:
    page0 = pdf.pages[1]
    # print(page0.extract_text())
    # Chemosphere 摘要开始与结束
    # 格式化为str,这是没有动过的原文。
    pagetext = str(page0.extract_text())
    print(pagetext)
