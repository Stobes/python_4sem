import pandas as pd
import matplotlib as plt


def pd_rep(*lists):

    df_list = []

    for list in lists:
        df = pd.DataFrame(list, columns=['Product Name', 'Price', 'Price/Unit'])
        df_list.append(df)

    for df in df_list:
        sum = df['Price'].astype(float).sum()
    
        
    return df, sum


