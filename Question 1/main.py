from boy_class import boy
from random import randint
import csv
from girl_class import girl
import logging
from utility import creating_csv


logging.basicConfig(filename='text.log',filemode='w',datefmt='%d:%m:%Y %I/%M/%S %p',format='%(asctime)s %(name)-s %(levelname) s: %(message)s',level=logging.DEBUG)

def creating_csv():
    Boy = [('a'+str(i),randint(1,100),randint(200,1000),randint(55,200),randint(1,100))for i in range(0,69)]
    Girl = [('b'+str(i),randint(20,100),randint(200,1000),randint(1,200))for i in range(0,51)]

    fp1 = open('data_boy.csv',"w")
    write = csv.writer(fp1,delimiter = ',')
    for x in Boy:
        write.writerow(x)
    fp2 = open('data_girl.csv',"w")
    write = csv.writer(fp2,delimiter = ',')
    for y in Girl:
        write.writerow(y)

def print_couple(glist):
    for g_ in glist:
        if g_.status_girl == 'single':
            print('Girl : '+g_.name_girl+ ' is not in relationship')
        else:
            print('Girl : '+g_.name_girl+ ' got commited with Boy : '+g_.name_boyfriend)
    
    
    
creating_csv()
    
  
'read data from \'data_boy.csv\' file'
    
'after taking input i have to create list based on current deatils'
glist = []
blist = []
'same goes for girl'
csv_girl = open('data_girl.csv')
girl_reader = csv.reader(csv_girl, delimiter = ',')

for _i in girl_reader:
    glist += [girl(_i[0],int(_i[1]),int(_i[2]),int(_i[3]))]
with open('data_boy.csv','r') as csv_boy:
     boy_reader = csv.reader(csv_boy,delimiter = ',')
     blist = [boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]))for row in boy_reader]
     

for a in glist:
    for b in blist:
        logging.info(a.name_girl+' is looking for ' +b.name_boy)
        if  b.suitable(a.required_budget,a.attraction_girl) and a.suitable(b.budget_for_girlfriend) :
            'after checking all the conditions if both are eligible and single'
                
            'updating girlfriend\'s name and boy\'s status'
            b.name_girlfriend = a.name_girl
            b.status_boy = 'In-relationship'
                
            'updating boyfriend\'s name and status'
            a.name_boyfriend = b.name_boy
            a.status_girl = 'In-relationship'
            logging.info(a.name_girl + ' in relationship with '+b.name_boy)
            ' girl already found a boy she is no longer looking for a boy so we havev to break the loop'
            break
                 
print("Printing couples \n")
print_couple(glist)
    
    
    
    
