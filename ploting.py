import numpy as np
import matplotlib.pyplot as plt


#10 000 people
#10 in a day
#probility of vaccan work in age>50 equal 25% and 75% for other


termineted=[0]*11
n=1_000_000



x_tick=['0','1','2','3','4','5','6','7','8','9','10']
y_tick=[]
for i in range(0,26,5):
    y_tick.append(str(i/100))
    

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

for i in range(n//10):
    counter=0
    for j in range(10):
        possibility=np.random.uniform(0,1)
        if possibility<=0.25:
            counter+=1         
    termineted[counter]+=1/n
    

y1=np.array(termineted)
x=np.arange(0,11,1)
plt.subplot(2,2,1)
plt.ylabel("probability ")
plt.xlabel('age>50 people cured')

plt.xticks(x,x_tick)

plt.bar(x,y1,color='red')



termineted=[0]*11

for i in range(n//10):
    counter=0
    for j in range(10):
        possibility=np.random.uniform(0,1)
        if possibility<=0.75:
            counter+=1         
    termineted[counter]+=1/n


y2=np.array(termineted)
plt.subplot(2,2,2)
plt.ylabel("probability ")
plt.xlabel('age<=50 people cured')

plt.xticks(x,x_tick)


plt.bar(x,y2,color='green')
       
    

termineted=[0]*11


for i in range(n//10):
    counter=0
    for j in range(10):
        age=np.random.choice([0,1])
        #age>=50:1 ,else:0
        possibility=np.random.uniform(0,1)
        if age==1:
            if possibility<=0.25:
                counter+=1
        elif age==0:
            if possibility<=0.75:
                counter+=1
        termineted[counter]+=1/n

y3=np.array(termineted)
plt.subplot(2,2,3)
plt.ylabel("probability ")
plt.xlabel('all people cured')

plt.xticks(x,x_tick)


plt.bar(x,y3,color='blue')



plt.show() 
