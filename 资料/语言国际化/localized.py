# -*- coding: utf-8 -*-
import sys
import xdrlib
import xlrd
import os
import shutil
##########################################################
reload(sys)
sys.setdefaultencoding('utf-8')

##########################################################
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

###################### 自定义常量 ####################################
localizeSheet = 6 # 导出第几个sheet的table数据
keyColumnIndex = 3 # key在第几列
languageStartIndex = 4 # 语言从第几列开始

##########################################################

def main(argv):
    data = open_excel(sys.argv[1])
    if data:
        table = data.sheets()[localizeSheet] # 第几个tab的table
        colnames = table.row_values(0)       # 第一行数据
        colKeys = table.col_values(keyColumnIndex)  # key的列
        nrows = len(colKeys)    # 总行数
        ncols = len(colnames)   # 总列数
        
        # 语言列表
        languageList = []
        # 国际化文件名列表
        fileNameList = []
        
        parent = os.path.dirname(os.path.realpath(__file__))
        dirPath = parent + '/localize'
        # 建一个文件夹放语言文件
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)
        # excel表语言开始的列开始遍历
        for indexCol in range(languageStartIndex,ncols):
            list = []
            # 当前列的数据
            colValues = table.col_values(indexCol)
            # 第一行的内容作为文件名
            fileNameList.append(colValues[0] + '.strings')
            
            # 跳过第一行，开始读取当前列内容
            for indexRow in range(1,nrows):
                value = str(colValues[indexRow]).replace("%s", "%@");
                key = colKeys[indexRow]
                if (len(key)==0): continue
                if (len(value)==0):
                   value = key
                keyValue = '"' + key + '"' + ' = ' + '"' + value + '"' + ';\n'
                list.append(keyValue)
            languageList.append(''.join(list))
        
        for index in range(len(languageList)):
            # 根据多语言个数，创建文件，写入内容
            fileName = dirPath + '/' + fileNameList[index]
            os.system(r'touch %s' % fileName)
            
            fp = open(fileName,'wb+')
            fp.write(languageList[index])
            fp.close()
    else :
        print "can not open file"

if __name__=="__main__":
    main(sys.argv[1])
