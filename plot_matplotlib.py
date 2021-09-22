import matplotlib.pyplot as plt
import numpy as np
x=np.arange(9)
plt.plot(x)

#make a group of plots:subplots(first way)
fig=plt.figure()#empty plot window
ax1=fig.add_subplot(2,2,1) #the figure should be 2*2 and ax1 is the first subplot
ax2=fig.add_subplot(2,2,2) #the figure should be 2*2 and ax2 is the second subplot
ax3=fig.add_subplot(2,2,3) #the figure should be 2*2 and ax3 is the third subplot
ax4=fig.add_subplot(2,2,4) #the figure should be 2*2 and ax4 is the forth subplot
plt.plot(np.random.randn(50).cumsum(),'g--')
ax1.hist(np.random.randn(20).cumsum(),bins=30,color='r')
ax2.scatter(np.random.randn(20),np.random.randn(20)*3)



#create a figure with a grid of subplots(second way)
fig,axes=plt.subplots(2,3,sharex=True,sharey=True)#2:number of rows,3:number of columns in subplots
for i in range(2):
    for j in range(3):
        axes[i,j].hist(np.random.randn(500),bins=50)
plt.subplots.adjust(wspace=0,hspace=0)



#color,lines styles and markers:
plt.plot(np.random.rand(9),color='g',linestyle='dashed',marker='*')
plt.plot(np.random.rand(9),'g--',marker='o')

plt.plot(np.random.rand(9).cumsum(),color='g',drawstyle='steps-post',marker='o')
plt.legend(loc='best')  #???


#ticks, labels and legends
#ticks:
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
axe=fig.add_subplot(1,1,1)
axe.plot(np.random.randn(1000).cumsum(),color='b')
#change tickes on x:
ticks=axe.set_xticks([0,250,500,750,1000])
label=axe.set_xticklabels(['one','two','three','four','five'],fontsize='small',
                          rotation=30)
#change ticks on y:
plt.ylim(-40,40)
#add label to x:
axe.set_xlabel('stages')


#adding legends:
fig=plt.figure()
axe=fig.add_subplot(1,1,1)
axe.plot(np.random.randn(1000).cumsum(),color='b',label='one')
axe.plot(np.random.randn(1000).cumsum(),color='r',label='two')
axe.plot(np.random.randn(1000).cumsum(),color='k',label='three')
axe.legend(loc='best')
#annotations consist of text,arrows and other shapes:
plt.annotate('test',xy=(1000,20),xytext=(1000,30),
             arrowprops=dict(facecolor='blue',shrink=0.05),fontsize='large')

#configuration:
plt.rc('figure',figsize=(10,10))
fontoption={'size':'small','weight':'bold','family':'monospace'}
plt.rc('font',**fontoption)

#saving plot in temporary path(C:\Users\fatem):
plt.savefig('figpath.png',dpi=100,bbox_inches='tight',
            facecolor='pink',edgecolor='red')













