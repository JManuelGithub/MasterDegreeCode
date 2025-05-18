import matplotlib.pyplot as plt

def max_values(p, by='Year'):
    max_vals = {}
    for pn in p['unique_id'].unique():
        plot_df = p[p['unique_id']==pn]
        fig = plt.figure(figsize=(2,5), layout='constrained')
        df = plot_df[[by,'y']]
        data=[]
        for _ in df[by].unique():
            d=df[df[by]==_]['y']
            data.append(d)

        box = plt.boxplot(data)
        plt.close()
        max_whisker = []
        #print(pn)
        #print(box['caps'])
        #print(box['caps'][0].get_ydata())
        #print(box['caps'][1].get_ydata())
        #print(box['caps'][2].get_ydata())
        #print(box['caps'][3].get_ydata())
        #print('Analizar con for')
        for i in range(len(df[by].unique())*2):
            if i%2!=0:
                #print(box['caps'][i].get_ydata()[0])
                max_whisker.append(box['caps'][i].get_ydata()[0])

        max_vals[pn] = max_whisker
        #print('Max: ',max_whisker)
    #print(d)
    return max_vals

def cleaning(p, by='Year'):
    d = max_values(p=p,by=by)
    #p['y_original'] = p['y'].copy()
    #p['y_new'] = p['y'].copy()
    print(d)
    for pn in p['unique_id'].unique():
        print(pn)
        for year in range(len( p['Year'].unique() )):

            maxi=d[pn][year]
            year2=p['Year'].unique()[year]

            p.loc[(p['unique_id']==pn) & (p['Year']==year2) & (p['y']>maxi), ['y']] = maxi


    return p



        