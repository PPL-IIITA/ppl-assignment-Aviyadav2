import random
import csv
def create_util():
     boys = []
     girls = []
     gifts = []
     type_boy = ['Miser','Generous','Geek']
     type_girl = ['Choosy','Normal','Desperate']
     type_gift = ['Essential','Luxury','Utility']

     i = 0
     j = 0
     k = 0
     while(i < 100):
          boys += [('boy'+str(i),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),type_boy[random.randint(0,2)])]
          i +=1

     while(j < 10):
          girls += [('girl'+str(j),random.randint(0,20),random.randint(0,20),random.randint(0,20),type_girl[random.randint(0,2)])]
          j += 1
          
     while(k < 11):
          gifts += [('gift'+str(k),random.randint(0,100),random.randint(0,100),type_gift[random.randint(0,2)])]
          k += 1
     fp0 = open('b_list.csv','w')
     writer0 = csv.writer(fp0,delimiter = ',')

     for i in boys:
          writer0.writerow(i)

     fp1 = open('g_list.csv','w')
     write1 = csv.writer(fp1,delimiter = ',')
     for i in girls:
           write1.writerow(i)

     fp2  = open('gift.csv','w')
     write2 = csv.writer(fp2,delimiter = ',')

     for i in gifts:
          write2.writerow(i)

create_util()
