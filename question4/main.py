import random
import csv
import logging
import math
import pprint

from miser import Miser
from geek import Geek
from generous import Generous
from choosy import Choosy
from desperate import Desperate
from normal import Normal
from essential import Essential
from luxury import Luxury
from utility import Utility

from couple import couple
from boy import boy
from girl import girl
from gift import gift
from util import create_util

def log_maker(write):
     logging.basicConfig(filename='text.log',datefmt = '%d/%m/Y %I:%M:%S %p',format='%(asctime)s %(name)-6s %(levelname)s :%(message)s',level = logging.DEBUG,filemode='w')
     logging.info(write)
logging.basicConfig(filename='text.log',datefmt = '%d/%m/%y %I:%M:%S %p',format = '%(asctime)s %(name)-6s %(levelname) s :%(message)s',level = logging.DEBUG,filemode = 'w')

def cal_hn(H):
     with open('gift.csv','r') as csvfile:
          fp = csv.reader(csvfile,delimiter = ',')
          gifts = []
          for row in fp:
               if(row[3] == 'Luxury'):
                    gifts += [Luxury(row[0],int(row[1]),int(row[2]),row[3])]
               elif (row[3] == 'Essential'):
                    gifts += [Essential(row[0],int(row[1]),int(row[2]),row[3])]
               elif(row[3] == 'Utility'):
                    gifts += [Utility(row[0],int(row[1]),int(row[2]),row[3])]
          csvfile.close()

          gifts = sorted(gifts,key = lambda item: item.cost)
          logging.warning('\n gifts:\n')

          for i in H:
               if(i.boy.type_boy == 'Miser'):
                    mr(gifts,i)
               if(i.boy.type_boy == 'Generous'):
                    gs(gifts,i)
               if(i.boy.type_boy == 'Geek'):
                    geek(gifts,i)

          g_dt(H)

          
def h_c(H,k):
     A = sorted(H,key = lambda item: item.happiness,reverse = True)
     B = sorted(H, key = lambda item: item.compatibility_status,reverse = True)
     print('\n most compatible couples\n')
     i =0
     while(i < k):
          print(B[i].boy.name_boy + ' and '+ B[i].girl.name_girl)
          i += 1
     print('\n most happy couples \n')
     j = 0
     while(j < k):
          j += 1
          print(A[j].boy.name_boy +' and '+ A[j].girl.name_girl)

def gs(gifts,p):
     x = 0
     y = 0
     for z in gifts :
          if(p.boy.budget_for_girlfriend - z.cost > 0) and (p.boy.budget_for_girlfriend >= 0) and ((p.boy.budget_for_girlfriend - z.cost <= 300)or(z.cost == p.budget_for_girlfriend)):
               if(z.type_gift == 'Luxury'):
                    y = y+2*z.cost
               else:
                    y = y+ z.cost
               x  = x + z.cost
               p.gift = p.gift+ [z]
               p.boy.budget_for_girlfriend = p.boy.budget_for_girlfriend -z.cost

               logging.info(p.boy.name_boy + ' gavve '+p.girl.name_girl+' gift '+ z.name)

     

     
     if(p.girl.type_girl == 'Choosy' and y > 0):
          p.girl.happiness = math.log10(y)

     elif(p.girl.type_girl == 'Normal'):
          p.girl.happiness = x
     else:
          p.girl.happiness = math.exp(x)
     p.boy.happiness = p.girl.happiness
     p.set_comp()
     p.set_hn()

def mr(gifts,x):
     w = 0
     y = 0
     for z in gifts:
          if(x.boy.budget_for_girlfriend >= 0)and ((z.cost - x.girl.maintence_budget_girl <= 100) or(z.cost == x.girl.maintence_budget_girl)) and (x.boy.budget_for_girlfriend - z.cost > 0):
               if(z.type_gift == 'Luxury'):
                    y = y+2*z.cost
               else:
                    y = y+ z.cost
               w = w+ z.cost
               x.gift = x.gift+[z]
               x.boy.budget_for_girlfriend = x.boy.budget_for_girlfriend - z.cost
               log_maker(x.boy.name_boy +' gave '+ x.girl.name_girl+" gift "+z.name)

     if(x.girl.type_girl == 'Choosy' and y > 0):
          x.girl.happiness = math.log10(y)

     elif(x.girl.type_girl == 'Normal'):
          x.girl.happiness = w
     else:
          x.girl.happiness = math.exp(w)

     x.boy.happiness = x.girl.happiness
     x.set_hn()
     x.set_comp()


def geek(gifts,c):
     x = 0
     y = 0
     for z in gifts:
          if(c.boy.budget_for_girlfriend >= 0) and ((z.cost - c.girl.maintence_budget_girl <= 100) or (z.cost == c.girl.maintence_budget_girl)) and (c.boy.budget_for_girlfriend -z.cost > 0):
               if (z.type_gift == 'Luxury'):
                    y  = y+ 2* z.cost
               else:
                    y = y + z.cost
               x  = x + z.cost
               c.gift = c.gift + [z]
               c.boy.budget_for_girlfriend = c.boy.budget_for_girlfriend - z.cost
               log_maker(c.boy.name_boy+' gave '+c.girl.name_girl + ' gift '+ z.name)

     for z in gifts:
          if( z not in c.gift)and(z.type_gift == 'Luxury') and (z.cost <= c.boy.budget_for_girlfriend):
               y  = y+ 2 * z.cost
               x = x + z.cost
               c.gift = c.gift+[z]
               c.boy.budget_for_girlfriend = c.boy.budget_for_girlfriend - z.cost
               log_maker(c.boy.name_boy + ' gave ' + c.girl.name_girl +' gift '+ z.name)
               break

     if(c.girl.type_girl == 'Choosy' and y > 0):
          c.girl.happiness = math.log10(y)

     elif(c.girl.type_girl == 'Normal'):
          c.girl.happiness = x

     else:
          c.girl.happiness = math.exp(x)

     c.boy.happiness = c.girl.intelligence
     c.set_hn()
     c.set_comp()

def g_dt(H):
     for h in H:
          print('Gift given from ' + h.boy.name_boy + ' to ' + h.girl.name_girl +'\n')
          for x in h.gift:
               print(x.name + ' type : '+ x.type_gift)
          print('\n')
          k = random.randint(1,len(H))
     h_c(H,k)

def tt():
     with open('b_list.csv','r') as csvfile:
          fp1 = csv.reader(csvfile,delimiter = ',')
          b_l = []
          for i in fp1:
               if(i[5] == 'Miser'):
                    b_l += [Miser(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])]
               elif(i[5] == 'Generous'):
                    b_l += [Generous(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])]
               elif(i[5] =='Geek'):
                    b_l += [Geek(i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4]),i[5])]
          csvfile.close()
     with open('g_list.csv','r') as csvfile:
          fp2 = csv.reader(csvfile,delimiter = ',')
          g_l = []
          for i in fp2 :
               if (i[4] == 'Choosy'):
                    g_l += [Choosy(i[0],int(i[1]),int(i[2]),int(i[3]),i[4])]
               elif(i[4] == 'Normal'):
                    g_l += [Normal(i[0],int(i[1]),int(i[2]),int(i[3]),i[4])]
               elif(i[4] == 'Desperate'):
                    g_l += [Desperate(i[0],int(i[1]),int(i[2]),int(i[3]),i[4])]
          csvfile.close()

     c_l = []

     for x  in g_l:
          for y in b_l:
               log_maker(x.name_girl + ' is searching '+ y.name_boy)
               if x.r_s == 'single' and  y.r_s == 'single' and (x.chk_elg(y.budget_for_girlfriend) and (y.chk_elg(x.maintence_budget_girl,x.attraction_girl))):
                    x.r_s = 'in_relationship'
                    y.r_s = 'in-relationship'
                    x.bf = y.name_boy
                    y.gf = x.name_girl
                    log_maker(x.name_girl+' is in relationship with ' + y.name_boy)
                    c_l = c_l + [(y,x)]
                    break
     for m in g_l:
          if m.r_s == 'single':
               print(m.name_girl+' is still single \n')
          else:
               print(m.name_girl+ ' is in realtionship with '+ m.bf+'\n')

     H = []
     for i in c_l:
          H += [couple(i[0],i[1])]
     cal_hn(H)
     n = []
     k = random.randint(1,len(H)-1)
     for i in range(k):
          n.append(H[i])
     for h in H[0:k]:
          h.boy.r_s = 'single'
          h.girl.r_s = 'single'
     for g in n:
          k = g.girl
          for l in b_l:
               log_maker(k.name_girl +' is searching ' +l.name_boy)
               if l.name_boy and l.r_s == 'single' and k.r_s == 'single' and (k.chk_elg(l.budget_for_girlfriend)) and ( l.chk_elg(k.maintence_budget_girl,k.attraction_girl)):
                    k.r_s = 'in_relationship'
                    l.r_s = 'in-relationship'
                    k.bf = l.name_boy
                    l.gf = k.name_girl
                    log_maker(k.name_girl + ' is in realtionship with ' + l.name_boy)
                    c_l = c_l+[(l,k)]
                    break
     for m in g_l:
          if m.r_s == 'single':
               print(m.name_girl +'is still single \n')
          else:
               print(m.name_girl+ ' with '+m.bf +'\n')
          

create_util()
tt()
                    
