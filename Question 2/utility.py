import csv
from random import randint
from random import choice
import logging

def creating_csv():
     
    type_boy = ['Geneous','Geek','Miser']
    type_girl = ['Desperate','Normal','Choosy']
    type_gift = ['Utility','Luxury','Essential']
    
    Boy = [('boy'+str(i),randint(2,21),randint(20,100),randint(55,200),randint(1,16),choice(type_boy))for i in range(1,49)]
    Girl = [('girl'+str(i),randint(3,20),randint(20,100),randint(25,200),choice(type_boy))for i in range(1,24)]
    Gift = [('gift'+str(i),randint(50,200),randint(95,150),choice(type_gift))for i in range(1,100)]
    fp1 = open('data_boy.csv',"w")
    write = csv.writer(fp1,delimiter = ',')
    for x in Boy:
        write.writerow(x)
    fp2 = open('data_girl.csv',"w")
    write = csv.writer(fp2,delimiter = ',')
    for y in Girl:
        write.writerow(y)
    fp3 = open('data_gift.csv',"w")
    write = csv.writer(fp3,delimiter = ',')
    for z in Gift:
         write.writerow(z)

def properties_gift(H):
    #print(list(H))    
    for i_ in H:
        logging.info('From  ' + i_.name_boy.name_boy +'to '+i_.name_girl.name_girl)
        for j_ in i_.gft:
            logging.info('Gift '+ j_.name_gift + 'type '+ j_.gift_type)
        k = randint(1,len(H))
    
    printc_hc(H, k)

       
def printc_hc(X,k):
    A = sorted(X,key = lambda item:item.joy_level)
    B = sorted(X,key = lambda item: item.compatibility_level_couple)
    print(str(k)+'most happy couples:')
    for j_ in range(k):
        print(A[j_].name_boy.name_boy +' , '+ A[j_].name_girl.name_girl)
    print('most compti')
    for i_ in range(k):
        print(B[i_].name_boy.name_boy+' , '+B[i_].name_girl.name_girl)
               
