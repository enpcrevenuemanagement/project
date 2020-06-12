import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
 
def plot_remplissage_ventes(sales, nb_seats):
    #arguments : sales = dictionnaire qui associe à chaque vente (numero de client) un quadruplet (prix de la place vendue, horaire du vol, remplissage de l'avion, numero de l'expérience)

    count = 0 #pour numeroter les expériences pour les plotter sur des courbes différentes
    mat_list =[] #liste de matrices à concatener pour faire un dataframe a plotter
    for dic in sales:

        count += 1
        exp = []
        prix = []
        vol_h = []
        sold=[]

        lists = sorted(dic.items())
        client, y = zip(*lists)

        for pair in y:
            prix.append(pair[0])
            vol_h.append(pair[1])
            sold.append(nb_seats-pair[2])
            exp.append(count)
            
        mat_list.append(np.transpose([client, prix, vol_h, sold, exp]))

    big_matrix = np.concatenate(mat_list, axis=0) 
    #creation du df
    df = pd.DataFrame(big_matrix, columns = ['client', 'prix', 'vol_horaire', 'remplissage', 'exp'])
    #creation des 2 plots : remplissage et prix des ventes
    ax1 = sns.lineplot(x="client", y="prix", hue="exp", style="vol_horaire", data=df)
    ax2 = ax1.twinx()
    sns.lineplot(x="client", y='remplissage', hue="exp", style="vol_horaire", palette="ch:2.5,.25", ax=ax2, data=df)
    plt.show()