import zipfile, os

files = os.listdir(os.getcwd())

'''
1、先遍历当前目录所有文件
2、然后把文件进行拆分：文件名+文件格式
3、获取zip 格式的文件进行解压
4、读取解压后的文件info.channel内容
https://www.cnblogs.com/fangyu19900812/p/3696886.html
'''
def unzip_file():
    for i in files:
        p = os.path.splitext(i)
        if p[1] == '.zip':
            zfile = zipfile.ZipFile(i, 'r')
            for allfiles in zfile.namelist():
                filename = p[0]
                file = zfile.extract(allfiles, filename)
                if file == filename + "/assets/info.channel":
                    read(filename)
                else:
                    print('解压文件异常，请重试')
            zfile.close()


def read(filename):
    h = os.getcwd() + '/' + filename + '/assets/info.channel'
    print('解压文件名称路径：%s'% h)
    with open(os.getcwd() + '/' + filename + '/assets/info.channel', 'r', encoding='utf-8') as f:
        r = f.read()
        print('渠道号为：%s'% r)
        f.close()


if __name__ == '__main__':
    unzip_file()