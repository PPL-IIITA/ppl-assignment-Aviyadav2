from cmath import exp, log10
from math import floor
from gift_class import gift
from couple_class import couple
from boy_class import boy
from random import randint
import csv
from girl_class import girl
import logging
from utility import creating_csv
from utility import properties_gift
from utility import printc_hc



'''logging.basicConfig(filename='text.log',filemode='w',datefmt='%d:%m:%Y %I/%M/%S %p',format='%(asctime)s %(name)-s %(levelname) s: %(message)s',level=logging.DEBUG)

creating_csv()
    
'read data from \'data_boy.csv\' file'
    
'after taking input i have to create list based on current deatils'
glist = []
blist = []
couple_list = []
'same goes for girl'
csv_girl = open('data_girl.csv')
girl_reader = csv.reader(csv_girl, delimiter = ',')

for _i in girl_reader:
    glist += [girl(_i[0],int(_i[1]),int(_i[2]),int(_i[3]),_i[4])]
with open('data_boy.csv','r') as csv_boy:
     boy_reader = csv.reader(csv_boy,delimiter = ',')
     blist = [boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5])for row in boy_reader]
     

for a in glist:
    for b in blist:
        logging.info(a.name_girl+' is looking for ' +b.name_boy)
        if  b.suitable(a.required_budget,a.attraction_girl) and a.suitable(b.budget_for_girlfriend) and b.status_boy=='single' and a.status_girl=='single':
            'after checking all the conditions if both are eligible and single'
                
            'updating girlfriend\'s name and boy\'s status'
            b.name_girlfriend = a.name_girl
            b.status_boy = 'In-relationship'
                
            'updating boyfriend\'s name and status'
            a.name_boyfriend = b.name_boy
            a.status_girl = 'In-relationship'
            print(a.name_girl + ' in relationship with '+b.name_boy)
                
            logging.info(a.name_girl + ' in relationship with '+b.name_boy)
            couple_list += [(a,b)]
                

            ' girl already found a boy she is no longer looking for a boy so we havev to break the loop'
            break
X = [couple(x[0],x[1])for x in couple_list]
#calculate_happiness(X)'''
'''def properties_gift(H):
    #print(list(H))    
    for i_ in H:
        print('From  ' + i_.name_boy.name_boy +'to '+i_.name_girl.name_girl)
        for j_ in i_.gft:
            print('Gift '+ j_.name_gift + 'type '+ j_.gift_type)
        print('\n')
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
        print(B[i_].name_boy.name_boy+' , '+B[i_].name_girl.name_girl)'''
               



def calculate_happiness(H):
    with open('data_gift.csv',"r") as csvfile:
        fp1 = csv.reader(csvfile,delimiter = ',')
        gft = [gift(j_[0],int(j_[1]),int(j_[2]),j_[3])for j_ in fp1]
        csvfile.close()

    gft = sorted(gft,key = lambda k:k.price_gift)
    logging.info('boyfriend is giving gift')

    for x in H:
        if(x.name_boy.boy_type == 'Geek'):
            ghpy(gft,x)

        if(x.name_boy.boy_type == 'Miser'):
            mhpy(gft,x)

        if(x.name_boy.boy_type == 'Generous'):
            genhpy(gft,x)
            
    properties_gift(H)
    
def ghpy(gift,x):
    x_ = 0
    y_ = 0
    for i_ in gift:
        if (i_.price_gift == x.name_girl.required_budget) or (i_.price_gift - x.name_girl.required_budget <= 100)and (x.name_boy.budget_for_girlfriend >= 0 ) and (x.name_boy.budget_for_girlfriend - i_.price_gift > 0):
            if(i_.gift_type == 'LUXURY'):
                y_ = _y + 2*i_pricegift
            else:
                y_ +=  i_.price_gift
            x_ += i_.price_gift
            x.gft += [i_]
            x.name_boy.budget_for_girlfriend = x.name_boy.budget_for_girlfriend - i_.price_gift
            logging.info(x.name_boy.name_boy + ' gives gift to '+ x.name_girl.name_girl+' worth '+ str(i_.price_gift))



    for j_ in gift:
        if (j_ not in x.gft) and (j_.gift_type == 'Luxury') and (j_.price_gift <= x.name_boy.budget_for_girlfriend):
            x_ += j_.price_gift
            y_ += 2*j_.price_gift
            x.gft += [j_]
            x.name_boy.budget_for_girlfriend -= j_price
            logging.info(x.name_boy.name_boy + ' gives gift to '+ x.name_girl.name_girl+' worth '+ str(i_.price_gift))
            break


    if(x.name_girl.girl_type == 'Normal'):
        x.name_girl.joy_level = x_

    elif(x.name_girl.girl_type == 'Choosy'):
        x.name_girl.joy_level = log10(y_ if y_ > 0 else 1)

    else:
        x.name_girl.joy_level = exp(x_).real

    x.name_boy.joy_level = x.name_girl.brain_level_girl

    x.calculate_compatibility()
    x.count_happiness()


def genhpy(gift,x):
    x_ = 0
    y_ = 0

    for i_ in gift:
        if(i_.price_gift - x.name_girl.required_budget <= 100) or (i_.price_gift == x.name_girl.required_budget) and (x.name_boy.budget_for_girlfriend - i_.price_gift > 0) and (x.name_boy.budget_for_girlfriend >= 0):
            if(i_.gift_type == 'Luxury'):
                y_ += 2*i_.price_gift
            else :
                y_ += i_.price_gift
            x_ += i_.price_gift
            x.gift += [i_]
            x.name_boy.budget_for_girlfriend  -= i_.price_gift
            logging.info(x.name_boy.name_boy + ' gives gift to '+ x.name_girl.name_girl+' worth '+ str(i_.price_gift))

    if (x.name_girl.girl_type == 'Normal'):
        x.name_girl.joy_level = x_

    elif(x.name_girl.girl_type == 'Luxury'):
        x.name_girl.joy_level = exp(x_).real
    else:
        x.name_girl.girl_type = log10(y_ if y_ >0 else 1)

    x.name_boy.joy_level = x.name_girl.joy_level
    x.calculate_compatibility()
    x.count_happiness()


def mhpy(gift,x):
    x_ = 0
    y_ = 0
    for i_ in gift:
        if(i_.price_gift - x.name_girl.required_budget <= 100) or (i_.price_gift == x.name_girl.required_budget) and (x.name_boy.budget_for_girlfriend - i_.price_gift > 0) and (x.name_boy.budget_for_girlfriend > 0):
            if(i_.gift_type == 'Luxury'):
                y_ += (2*i_.price_gift)
            else:
                y_ += i_.price_gift
        x_ += i_.price_gift
        x.gft += [i_]
        x.name_boy.budget_for_girlfriend  -= i_.price_gift
        logging.info(x.name_boy.name_boy + ' gives gift to '+ x.name_girl.name_girl+' worth '+ str(i_.price_gift))

    if (x.name_girl.girl_type == 'Normal'):
        x.name_girl.joy_level = x_
    elif(x.name_girl.girl_type == 'Choosy'):
         x.name_girl.joy_level = log10(y_ if y_ > 0 else 1).real

    else:
        try:
            x.name_girl.joy_level = exp(x_).real
        except OverflowError:
         x.name_girl.joy_level = float('inf')
    

    x.name_boy.joy_level = x.name_boy.budget_for_girlfriend
    x.calculate_compatibility()
    x.count_happiness()
         
        


logging.basicConfig(filename='text.log',filemode='w',datefmt='%d:%m:%Y %I/%M/%S %p',format='%(asctime)s %(name)-s %(levelname) s: %(message)s',level=logging.DEBUG)
'read data from \'data_boy.csv\' file'
'after taking input i have to create list based on current deatils'
def main():
    blist = []
    couple_list = []
    csv_girl = open('data_girl.csv','r')
    girl_reader = csv.reader(csv_girl, delimiter = ',')

    glist =[]
    for _i in girl_reader:
        glist += [girl(_i[0],int(_i[1]),int(_i[2]),int(_i[3]),_i[4])]
    csv_girl.close()
    with open('data_boy.csv','r') as csv_boy:
         boy_reader = csv.reader(csv_boy,delimiter = ',')
         blist = [boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4]),row[5])for row in boy_reader]
         
    csv_boy.close()
    for a in glist:
        for b in blist:
            logging.info(a.name_girl+' is looking for ' +b.name_boy)
            if  b.suitable(a.required_budget,a.attraction_girl) and a.suitable(b.budget_for_girlfriend): #and b.status_boy=='single' and a.status_girl=='single':
            #'updating girlfriend\'s name and boy\'s status'
                b.name_girlfriend = a.name_girl
                b.status_boy = 'In-relationship'               
            #'updating boyfriend\'s name and status'
                a.name_boyfriend = b.name_boy
                a.status_girl = 'In-relationship'
                print(a.name_girl + ' in relationship with '+b.name_boy)
                
                logging.info(a.name_girl + ' in relationship with '+b.name_boy)
                couple_list = couple_list + [(a,b)]
                #' girl already found a boy she is no longer looking for a boy so we havev to break the loop'
                break
            
    H = [couple(x[0],x[1]) for  x in couple_list]
        #print(H.gift)
    calculate_happiness(H)

            
creating_csv()
main()
    
    
    
    
