import pandas as pd
import numpy as np


def calc_distance(c, p):
    x = abs(c[0] - p[0])
    y = abs((c[1]-p[1]))
    return x+y


def calc_avg(c):
    x = c[0].mean()
    y =c[1].mean()
    return x, y


def main():
    pont = [[1,1], [5,7], [1.5,2], [3,4], [3.5,5], [4.5,5], [3.5,4.5]]
    points = pd.DataFrame(pont, dtype='float32')
    print(points)
    distance = points
    distance = distance.replace(distance, 0)
    clust_no = pd.Series(np.arange(len(pont)))
    clust_old = clust_no
    Clusters = 2
    Centriods = points.iloc[:Clusters]
    cond = True
    while cond:
        for i, j in Centriods.iterrows():
            for k, l in points.iterrows():
                y = calc_distance(j, l)
                distance[i][k] = y
        clust_no = distance.idxmin(axis=1)
        # print("Clusters\n", clust_no)
        ibm = clust_old == clust_no
        showdf = distance.copy()
        showdf['cluster'] = clust_no
        if ibm.all():
            cond = False
        else:
            points['cluster'] = clust_no
            for i in range(Clusters):
                ibm = points[points['cluster'].values == i]
                x, y = calc_avg(ibm)
                Centriods.iloc[i][0] = x
                Centriods.iloc[i][1] = y
            del points['cluster']
        clust_old = clust_no
    print(showdf)

if __name__ == '__main__':
    main()