import matplotlib.pyplot as plt
x_values = list(range(1,5001))
y_values = [x*x*x for x in x_values]
plt.scatter(x_values,y_values,s=10,c=y_values,cmap=plt.cm.Reds,edgecolor='none')
plt.savefig('lifang.png',bbox_inches='tight')