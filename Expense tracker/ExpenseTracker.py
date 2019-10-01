import pandas as pd
import msvcrt
import os
import sys
from datetime import date
import matplotlib.pyplot as plt
from tabulate import tabulate
#-----------------------------------
now = date.today()
month = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}


#Funcions
#------------------------------------
def open_file():
    month = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    path_folder = 'DataSheet' 
    file_name = '\{}-{}.csv'.format(month[now.month],now.year)
    file_loc = path_folder+file_name
    try:
        dataframe = pd.read_csv(file_loc)
    except:
        if os.path.exists(path_folder):
            pass
        else:
            os.mkdir(path_folder)
        while True:
            try:
                Bal = int(input('Enter previous balance: '))
                break
            except:
                continue
        dataframe = pd.DataFrame.from_dict([{'Date':0,
                                             'Description/Info':'Previous sheet balance',
                                             'Debit Amount':0,
                                             'Credit Amount':0,
                                             'Balance':Bal}])
        dataframe.to_csv(file_loc,index = False)
        open_file()
            
    return (dataframe,file_loc)

def exit_win():
    print('\nPlease save data before uou exit!\nDo you want to exit?')
    inp = input('\n[Y/N]>> ')
    if inp in ['y','Y']:
        return False
    

    

#Classes
#------------------------------------
class ExpenseTracker(object):
    def __init__(self,dataframe,file_loc):
        self.dataframe = dataframe
        self.file_loc = file_loc

    def add_entry(self,Date,Desctiption,DA=0,CA=0,Bal=0):         #add at end
        if self.dataframe.last_valid_index():
            num = self.dataframe.last_valid_index()
        else:
            num = 0 
        self.dataframe.loc[num+1]=[Date,Desctiption,DA,CA,Bal]


    def show_data(self):
        print(tabulate(self.dataframe, headers='keys', tablefmt='psql'))
        #print(self.dataframe)

    def delete_entry(self,index=None):
        if index == None:
            index = self.dataframe.last_valid_index()            #delete at end
        self.dataframe.drop(index,axis=0,inplace=True)
        

    def show_graph(self):
        new = self.dataframe.drop(0)
        new.plot(x='Date',marker = 'o',kind='line',
                            grid=True,legend=True,title='Chart')
        plt.show()

    def save(self):
        self.dataframe.to_csv(self.file_loc,index = False)

    def get_pre_bal(self):
        return self.dataframe.loc[self.dataframe.last_valid_index()]['Balance']

def get_ch():
    char = input('\nEnter Option\n>>')
    if len(char) != 1:
        print('\nInvalid Option!')
        get_ch()
    return char
        
#main----------------------        
def main():
    running = True
    file = open_file()
    current_page = ExpenseTracker(file[0],file[1])
    while running:
        current_page.show_data()
        print('\n____ Menu ____\n')
        print('1. Add entry\n2. Delete entry\n3. show graph\n4. Save file\n5. Exit')
        while True:
            option = get_ch()
            if option in ['1','2','3','4','5']:
                break
            else:
                print('\nInvalid Option!')
        #options---------------
        if option == '1':
            try:
                Date = '{}-{}-{}'.format(now.day,now.month,now.year)
                Des = input('Enter Description/Info: ')
                DA = int(input('Enter Debit Amount: '))
                CA = int(input ('Enter Credit Anount: '))
                Bal = DA - CA + current_page.get_pre_bal()
                current_page.add_entry(Date,Des,DA,CA,Bal)
            except ValueError:
                print('Please enter valid data!')
        elif option == '2':
            print('\nDelete last entry?')
            choice = input('\n[Y/N]>>')
            if choice in ['y','Y']:
                current_page.delete_entry()
        elif option == '3':
            try:
                current_page.show_graph()
            except:
                print('\nInvalid Data in Sheet!')
        elif option == '4':
            current_page.save()
            print('File Saved!')
        elif option == '5':
            running = exit_win()
            if not running:
                sys.exit(0)
        msvcrt.getch()
        os.system('cls')    #refresh screen <-------
        
    



#run-----------------
if __name__=='__main__':
    main()
    


