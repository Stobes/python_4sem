import numpy as np

def price_pr_unit(productList):

    cheapes_unit_mask = ()

    new_list = []

    for sub_category in productList:
        sub_array = np.array(sub_category)

        mask = (sub_array[:,-1].astype(float) == np.min(sub_array[:,-1].astype(float)))

        u_price = sub_array[mask]
        for elem in u_price:
            new_list.append(elem.tolist())
    
    return new_list
    


    

