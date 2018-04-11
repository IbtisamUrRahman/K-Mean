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
    pont = [[1,1], [2,1], [4,3], [5,4]]
    points = pd.DataFrame(pont, dtype='float32')
    distance = points
    distance = distance.replace(distance, 0)
    clust_no = pd.Series(np.arange(len(pont)))
    clust_old = clust_no
    Clusters = 2
    Centriods = points.iloc[:Clusters]
    # Centriods.astype('float64')
    # print("Centriods\n",Centriods)
    cond = True
    while cond:
        print("Iteration")
        for i, j in Centriods.iterrows():
            for k, l in points.iterrows():
                y = calc_distance(j, l)
                distance[i][k] = y
        clust_no = distance.idxmin(axis=1)
        print("Clusters\n", clust_no)
        ibm = clust_old == clust_no
        print(distance)
        if ibm.all():
            cond = False
        else:
            # for i in range(Clusters):
            #     boll = clust_no == i
            #     for j in boll:
            #         if j:
            #             print(clust_no[i])
            points['cluster'] = clust_no
            # print(points['cluster'])
            print("Calculating Average of Centriods")
            for i in range(Clusters):
                # print("row",i)
                ibm = points[points['cluster'].values == i]
                x, y = calc_avg(ibm)
                # print("xaxis",x)
                # print("yaxis", y)
                Centriods.iloc[i][0] = x
                Centriods.iloc[i][1] = y
            # print("Centriods\n",Centriods)
            del points['cluster']
            # for i in clust_no[clust_no] == range(Clusters):
            #     print(i)
                # print(points.iloc[i])
            # clust_no[clust_no] == 1)
        clust_old = clust_no


if __name__ == '__main__':
    main()