from random import sample,choices,randrange,uniform
from os.path import getsize,exists
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor
import csv

alpha='abcdefghijklmnopqrdtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dot='._'
al=r'[];/.][[\!@#$\'%^&*()_+""'
numerical='1234567890'

password=alpha+al+numerical
domain_names=['@yahoo.com','@gmail.com','@outlook.com']

length=10
number_rows=10
columns ={'tetstet': ['String','20'], 'apple': ['Integer', '20'], 'apple2': ['Float', '20'], 'apple33': ['Boolean', '20']}
#csv_string={}
class Generate_data():
    row_id=0
    @staticmethod #just for info
    def data_generate(columns,number_rows,length):
        with open('csv_db_data.csv', 'w') as csvfile:
            csvfile.write('id,'+",".join(list(columns.keys()))+'\n')
            for rows in range(0,number_rows):
                csvfile.write(str(rows)+',')
                for key,values in columns.items():
                    column_value=''
                    if values[0] == 'String':
                        # for n in range(number_rows):
                        column_value="".join(choices(password, k=int(values[1])))
                        #csv_string[key]={values[0]:column_value}
                    elif values[0] == 'Integer':
                        for n in range(length):
                            column_value+=str(randrange(0,9))
                        #csv_string[key]={values[0]:column_value}
                    elif values[0] == 'Float':
                        for n in range(length):
                            column_value+=str(randrange(0,9))
                        column_value=str(int((column_value))/10)
                        #csv_string[key]={values[0]:column_value}
                    elif values[0] == 'Boolean':
                        bol=['0','1']
                        # for n in range(number_rows):
                        column_value=choices(bol)[0]
                        #csv_string[key]={values[0]:column_value}
                    csvfile.write(column_value)
                    if list(columns.keys())[-1]!=key:
                        csvfile.write(',')
                csvfile.write('\n')
                #row_id+=1 #use rows instead if you want
def main_program(columns,number_rows,length):
    with ProcessPoolExecutor() as exe:
        exe.submit(Generate_data.data_generate,columns,number_rows,length)

if __name__=="__main__":
    main_program(columns,number_rows,length)