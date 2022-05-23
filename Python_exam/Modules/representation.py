
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


  
# create data

def grouped_barplot(wordlist, *dfs):

    plt.figure()

    df_data = []

    for df in dfs:
        df_data.append(
            (df[0].columns.name,
            list(df[0]['Price']),
            df[1]))

    
    bilka = [float(i) for i in df_data[0][1]]
    føtex = [float(i) for i in df_data[1][1]]
    nemlig = [float(i) for i in df_data[2][1]]
    width = 0.20

    x = np.arange(len(wordlist))

    plt.bar(x-0.2, bilka, width, color='cyan')
    plt.bar(x, føtex, width, color='orange')
    plt.bar(x+0.2, nemlig, width, color='green')
    plt.ylim((0, 30))
    plt.xticks(x, wordlist)
    plt.legend(["Bilka", "Føtex", "Nemlig"])

    plt.savefig('grouped_barplot.png')

    return

def sum_barplot(*dfs):

    plt.figure()

    sum_data = []

    store_names = ["Bilka", "Føtex", "Nemlig"]

    x = np.arange(len(store_names))

    for df in dfs:
        sum_data.append((df[0].columns.name, df[1]))

    product_sums = [
        float(sum_data[0][1]),
        float(sum_data[1][1]),
        float(sum_data[2][1])
        ]
    
    width = 0.40

    plt.bar(store_names,product_sums)
    

    plt.savefig('sum_barplot.png')

    return

def print_result(*dfs):

    sum_data = []
        
    for df in dfs:
        sum_data.append((df[0].columns.name, df[1]))

    min_sum = min(
        float(sum_data[0][1]),
        float(sum_data[1][1]),
        float(sum_data[2][1])) 
        
    store = ''

    if min_sum == sum_data[0][1]:
        store = sum_data[0][0]
    elif min_sum == sum_data[1][1]:
        store = sum_data[1][0]
    else:
        store = sum_data[2][0]

    print('Det laveste beløb er på',min_sum,'kr. dermed får du den største bespargelse hos ', store,'!')


