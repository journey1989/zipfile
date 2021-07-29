import os


files = os.listdir(os.getcwd())


'''
1、先遍历当前目录所有文件
2、然后把文件进行拆分：文件名+文件格式
3、再重新生成新的文件名+文件格式
4、os.rename修改文件格式

'''
def rename_file():
    for currentfilename in files:
        p = os.path.splitext(currentfilename)
        if p[1] == '.apk':
            try:
                newfilename = p[0] + '.zip'
            except Exception as e:
                print(e)
            else:
                os.rename(currentfilename, newfilename)
                print('把%s后缀修改成zip格式' % currentfilename, ',修改后文件名为:%s'%newfilename)




if __name__ == '__main__':
    rename_file()
