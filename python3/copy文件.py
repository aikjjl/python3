
#多进程复制文件


import os
from multiprocessing import Pool

def copyFileTask(name, oldFName, newFName):
    #完成copy文件的功能
    fr = open(oldFName+"/"+name)
    fw = open(newFName+"/"+name, "w")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()

def main():
    oldFName = input("请输入要copy的文件夹：")
    #创建文件夹
    newFName = oldFName +"-复件"
    os.mkdir(newFName)

    #获取old文件夹中所有文件的名称
    FNames = os.listdir(oldFName)

    #多进程方式copy文件到new文件夹
    pool = Pool(5)
    pool.apply_async(copyFileTask, args=(name, oldFName, newFName))

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()