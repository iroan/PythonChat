class ShowText:
    def displayHelp(self):
        '''
        1. 文本文件字段之间用'|'隔开
        2. 读取文件的所有行
        3. 对一行的数据进行分割操作
        4. 对一行数据的每个字段使用encode()方法后统计字段长度
        5. 使用ljust方法打印
        :return:
        '''
        file = open('help.txt', 'r', encoding='utf-8')
        str = file.readlines()

        colum0_maxlen = 0
        colum1_maxlen = 0
        colum2_maxlen = 0
        x2 = []
        # print('str=',str)
        for x in str:
            x1 = x.split('|')
            x1[2] = x1[2].strip('\n')
            x2.append(x1)
            if len(x1[0]) > colum0_maxlen:
                colum0_maxlen = len(x1[0])
            if len(x1[1]) > colum1_maxlen:
                colum1_maxlen = len(x1[1])
            if len(x1[2]) > colum2_maxlen:
                colum2_maxlen = len(x1[2])

        # print('x2=',x2)
        space = 3
        colum1_maxlen = colum1_maxlen + space
        colum2_maxlen = colum2_maxlen + space
        colum0_maxlen = colum0_maxlen + space

        for x in x2:
            print(x[0].ljust(colum0_maxlen),end='')
            print(x[1].ljust(colum1_maxlen),end='')
            print(x[2].ljust(colum2_maxlen))

if __name__ == '__main__':
    s = ShowText()
    s.displayHelp()