# %% [markdown]
# # Charts
# generate graph to PIP class

# %%
import matplotlib.pyplot as plt

# %% [markdown]
# In this case the script doesn't stop with `plt.show()` but `plt.savefig`

# %%
def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('./py_project/charts/pie.png')
    plt.close() 


