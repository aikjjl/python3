import os
from multiprocessing import Pool

def copyFileTask(name, oldFolderName, newFolderName):
    #完成copy文件的功能
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name, "w")
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()

def main():
    oldFloderName = input("请输入要copy的文件夹：")
    #创建文件夹
    newFolderName = oldFolderName +"-复件"
    os.mkdir(newFolderName)

    #获取old文件夹中所有文件的名称
    fileNames = os.listdir(oldFloderName)

    #多进程方式copy文件到new文件夹
    pool = Pool(5)
    pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName))

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()