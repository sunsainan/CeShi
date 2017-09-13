import time;
for i in range(1,10):
    for j in range(1,10):
        if(j<=i):
           print(j,"*",i,"=",i*j,end="   ");
        else:
            print();
            break;


print ('hello');print ('runoob');
list = ['runoob', 786, 2.23, 'john', 70.2]
print (list[1:3])
print (time.asctime( time.localtime(time.time()) ))