import zipfile
def extractFile(file,password):
    try:
        file.extractall(pwd=password.encode("ascii"))
        print("发现密码",password)
        return password
    except:
        print("密码错误！",password)
        return
def main():
    file=zipfile.ZipFile("filename.zip")#破解文件名
    f=open("dic.txt")#打开密码字典
    for line in f.readlines():
        password=line.strip("\n")
        result=extractFile(file,password)
        if result==None:
            continue
        else:
            f.close()
            return
if __name__=="__main__":
    main()
