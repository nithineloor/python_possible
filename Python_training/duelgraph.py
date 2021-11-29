import matplotlib.pyplot as plt 
  
# Y1-axis values 
y1 = [12, 32, 50] 
  
# Y2-axis values  
y2 = [11,45, 55] 

x = ['student1', 'student2','student3']
  

plt.plot(x,y1, marker='*', color='b') 
plt.plot(x,y2, marker='*', color='r') 
  

plt.legend(["maths", "science"], loc ="upper right") 
 
plt.show()