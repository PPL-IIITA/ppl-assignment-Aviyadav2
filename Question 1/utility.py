import csv
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
    
    
    
