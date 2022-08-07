import pdfplumber


def main():
    file_path = r'test.pdf'
    with pdfplumber.open(file_path) as pdf:
        page0 = pdf.pages[0]
        # print(page0.extract_text())
        # Chemosphere 摘要开始与结束
        # 格式化为str
        page0_1 = str(page0.extract_text())
        # 只能循环两次
        while 1:
            start_abstract = int(
                page0.extract_text().find('A B S T R A C T', 1))  # page0.extract_text().find('A B S T R A C T')+1))
            end_abstract = int(page0.extract_text().find('* Corresponding author.'))
            if page0_1[start_abstract - 3] == 'L':
                start_abstract = int(
                    page0.extract_text().find('A B S T R A C T', page0.extract_text().find('A B S T R A C T') + 1))
                break
            else:
                break
        # start_abstract+15,end_abstract
        # TODO 查找一行一个或两个的单词
        o_abstract = page0_1[start_abstract + 16:end_abstract]
        while 1:
            double_space=o_abstract.find(' ')

        # TODO 查找多余一个的空格，并删除所在位置与前一个空格之间的单词

        # 去除换行符
        abstract = page0_1[start_abstract + 16:end_abstract]  # .replace("\n", "")
        print(abstract)


if __name__ == '__main__':
    main()
