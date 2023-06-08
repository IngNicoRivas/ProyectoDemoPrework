import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values): #name to change the name of savefig
    fig, ax = plt.subplots() # two variables given by matplotlib, fig and ax where fig are the figures/shapes and ax the coordinates to plot.
    ax.barh(labels, values, color = 'green') # values and labels need to graph
    font1 = {'color':'blue','size':20}  
    font2 = {'color':'darkred','size':15}
    plt.title("Population Growth", fontdict = font1)  
    plt.xlabel("Years", fontdict = font2)  
    plt.ylabel("Population", fontdict = font2)
    
    plt.grid(axis= 'y')
    #plt.show() # display plot
    plt.savefig(f'./py_project/app/imgs/{name}.png')
    plt.close() 

def generate_pie_chart(name, labels, values): 
    fig, ax = plt.subplots() # generated a pie chart
    # explode_labels = [0.2, 0, 0, 0, 0, 0, 0, 0]
    ax.pie(values, labels=labels, startangle= 90, shadow= True) # this is the syntax
    plt.legend(title = 'Countries')
    ax.axis('equal') # equal because it is a pie
    #plt.show()
    plt.savefig(f'./py_project/app/imgs/{name}.png')
    plt.close() 

if __name__ == '__main__' :
    labels = ['a', 'b', 'c']
    values = [10, 40, 120]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)