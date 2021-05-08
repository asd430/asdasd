import os
print(os.getcwd())
fp=open("C:\\Users\\user/Desktop/test\\file0.txt",'r')
tmp=fp.readline()
print(tmp)
tmp2=tmp.split(',')
tmp2[2]=tmp2[2].replace('\n','')
print(tmp2)
while(tmp!=""):
    tmp=fp.readline().replace('\n','')
    print(tmp)
fp.close()