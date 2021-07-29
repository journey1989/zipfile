import os

'''
前提条件： 运行代码要和apk放到一个层级目录下


1、renames.py 修改包文件格式apk = zip
2、unzipandread   把zip文件进行解压，并读取渠道来源


'''
os.system("python3 renames.py")
os.system("python3 unzipandread.py")
