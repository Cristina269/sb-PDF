import pdfplumber


# 每段处理完再删除（通过文字查找）和翻译
# 翻译摘要就算成功...后面同理

def all_newline(page_number=1):
    # 返回换行符（目前只有第一页
    newline = [0, 1]
    file_path = r'test.pdf'
    with pdfplumber.open(file_path) as pdf:
        len(pdf.pages[:])
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
    # 返回了所有双三空格 列表
    two = [0, 1]
    three = [0, 1]
    file_path = r'test.pdf'
    with pdfplumber.open(file_path) as pdf:
        len(pdf.pages[:])
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
    return two, three


def return_interaim(aim1, aim2):  # 返回列表中aim1和aim2之间的数字   后面要根据这个删除字符串（两个aim之间的所有字符串
    # aim1 是个数字          =7
    # aim2 是列表   升序     =[1,2,3,5,8,10]
    # 就要返回7-5之间=6，即删除第六个字符串（每页为单位
    # 输出为两个数字表示范围
    aim2.append(aim1)
    aim2.sort()
    target_location = aim2.index(aim1)  # aim1在aim2里的位置
    in_front_variable = aim2[target_location - 1]  # aim1前面一个数字的位置
    aim1 - in_front_variable
    waiting_for_delete = []  # 等待删除的
    waiting_for_delete.append(in_front_variable + 1)
    waiting_for_delete.append(aim1)
    print(waiting_for_delete)


def returns_intersection(pagetext, black_new, start_abstract, end_abstract):
    # 返回在这一行之间的换行符的位置，需要当页文字数，非摘要是全部字数
    front = []
    back = []
    while 1:
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

def main2():
    file_path = r'test.pdf'
    with pdfplumber.open(file_path) as pdf:
        page0 = pdf.pages[0]
        pagetext = str(page0.extract_text())
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

def main_abstract():
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
        # 查找一行一个或两个的单词 特征是 一行之间空格少于三个（大概
        # 先获取abs那一段文字，然后找里面的换行符并获取位置，
        # 第一页才需要用到start_abstract ，end_abstract，
        o_abstract = pagetext[start_abstract + 16:end_abstract]
        front = []
        back = []
        remember_to_delete = []
        while 1:  # 返回在这一行之间的换行符的位置
            for i in range(len(newline)):
                if int(newline[i]) < start_abstract:
                    front.append(i)
                elif int(newline[i]) > end_abstract:
                    back.append(i)
                else:
                    pass
            break
        re_newline = newline[len(front):len(newline) - len(back)]  # 两个元素之间是一行
        for i in range(len(re_newline)):
            try:
                a = pagetext.count(' ', re_newline[i], re_newline[i + 1])
                if a < 4:
                    # pagetext=str(pagetext[:re_newline[4]])+str(pagetext[:re_newline[4]])
                    remember_to_delete.append(str(pagetext[re_newline[i]:re_newline[i + 1]]))
                    print(remember_to_delete)
            except:
                pass
        # 要删除的文字在最后一块删

        # TODO 和主体不是一块的内容，特征是有两个或三个的空格，并删除所在位置与前一个空格之间的单词，或者是与前一个换行符之间的单词

        # 去除换行符
        two, three = all_balck()
        # TODO 删掉的应该是空格和换行符之间的

        abstract = pagetext[start_abstract + 16:end_abstract]  # .replace("\n", "")
        print(abstract)


if __name__ == '__main__':
    main2()


