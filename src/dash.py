import rich 
from rich import print
import sqlite3
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time 

#idk if I will use this 
import numpy as np 
import pandas as pd

db = sqlite3.connect(r"C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Presentation\DataBase.db")
cursor = db.cursor()

class DASHBOARD():
    def queries(self):
        itemlist = ['Female', 'Male', 'Other']
        mylist = []
        cursor.execute(f"Select gender, count(*) from evaluator group by gender")
        result = cursor.fetchall()
        for row in result: 
            #l = list(map(int, row))
            mylist.append(row[1])
        #db.close()

        #labels = itemlist
        #counts = mylist
        plt.subplot(2,2,2)
        #fig1, ax1 = plt.subplots(figsize=(15,15))
        print(mylist)
        plt.pie(mylist,  autopct='%1.1f%%', shadow=True, startangle=90) 
        plt.axis('equal')
        plt.legend(itemlist,loc='upper center', bbox_to_anchor=(0.5, 1.13), ncol=2, fancybox=True, shadow=True)
        plt.plot()   
        # Fetching Data From mysql to my python program
        cursor.execute(f"Select * from AgeRange")
        result = cursor.fetchall
        
        age_range = []
        count = []
        
        for i in cursor:
            age_range.append(i[0])
            count.append(i[1])
            
        print("Range = ", age_range)
        print("Total = ", count)
        
        
        # Visualizing Data using Matplotlib
        plt.subplot(2,2,4)
        plt.bar(age_range, count)
        plt.ylim(0, 10)
        plt.xlabel("Age range")
        plt.ylabel("Total")
        plt.title("Age range")
    
        # plt.plot()
        #plt.show()
        cursor.execute(f"SELECT FavAspectDescription, total FROM AspectsofProjects;")
        todos = cursor.fetchall

        aspects = []
        total = []
        for a in cursor:
            aspects.append(a[0])
            total.append(a[1])


        plt.subplot(2,2,3)
        plt.title("Total of Evaluations by Project")
        plt.stem(aspects, total, orientation = "horizontal")
        plt.xlim(0, 10)
        plt.xlabel("Total of evaluations")
        plt.plot()

        array = ['Yes', 'No']
        alist = []
        cursor.execute(f"select WillVisit, total from Visit_Again")
        query = cursor.fetchall()
        for m in query: 
            alist.append(m[1])
        plt.subplot(2,2,1)
        print(alist)
        plt.pie(alist,  autopct='%1.1f%%', shadow=True, startangle=90) 
        plt.axis('equal')
        plt.legend(array,loc='upper center', bbox_to_anchor=(0.5, 1.13), ncol=2, fancybox=True, shadow=True)
        plt.title("Will return?", loc="left")
        plt.plot()   

        plt.suptitle('Exhibition Dashboard',fontsize=20)
        plt.get_current_fig_manager().full_screen_toggle()
        plt.show()



# plt.style.use('_mpl-gallery-nogrid')
#figure = plt.figure()

# x = data.iloc[:,:0,:1,:2]

# colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
# fig, ax = plt.subplots()
# ax.pie(x, colors=colors, radius=3, center=(4, 4),
#        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()






# my_labels = 'Teste1', 'Um test'
# plt.pie(data, labels=my_labels, autopct='%1.1f%%')
# plt.title("Gender")
# plt.axis('equal')






