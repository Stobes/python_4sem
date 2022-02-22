import numpy as np

if __name__=="__main__":
    filename = './data/befkbhalderstatkode.csv'

    bef_statkode = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

    ger_child = np.sum((bef_statkode[:,3] == 5180) & (bef_statkode[:,2] == 0) & (bef_statkode[:,0] == 2015))

    def pop_data(aar,bydel,alder,stat):
        data = (bef_statkode[:,0] == aar) & (bef_statkode[:,1] == bydel) & (bef_statkode[:,2] == alder) & (bef_statkode[:,3] == stat)
        return data

    def sum_pop_data(aar,bydel,alder,stat):
        if alder == None:
            data = (bef_statkode[:,0] == aar) & (bef_statkode[:,1] == bydel) & (bef_statkode[:,3] == stat)
        else:
            data = (bef_statkode[:,0] == aar) & (bef_statkode[:,1] == bydel) & (bef_statkode[:,2] == alder) & (bef_statkode[:,3] == stat)
        return np.sum(data)

    def pop_data_con(dataset,aar=None,bydel=None,alder=None,stat=None):
        alder_mask = dataset[:,2] == alder if alder != None else True
        bydel_mask = dataset[:,1] == bydel if bydel != None else True
        aar_mask = dataset[:,0] == aar if aar != None else True
        stat_mask = dataset[:,3] == stat if stat != None else True

        #masked_data = ()
        return np.sum(dataset[aar_mask & bydel_mask & alder_mask & stat_mask][:,4])

    print(pop_data_con(bef_statkode,aar=1992, bydel=1,alder=10, stat=5100))

