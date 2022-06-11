import math
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from operator import itemgetter
import random

if __name__ == "__main__":
    

    npr = default_rng()

    mu = 1
    
    bpr = []
    k = math.floor(42/2)
    lamda = k
    max_arrival = 100
    offered_load = []
    for sim in range(0,6):
        links = {
        'l1' : [10,[0]*max_arrival],
        'l2' : [15,[0]*max_arrival],
        'l3' : [10,[0]*max_arrival],
        'l4' : [20,[0]*max_arrival],
        'l5' : [15,[0]*max_arrival],
        'l6' : [20,[0]*max_arrival],
        'l7' : [15,[0]*max_arrival],
        'l8' : [15,[0]*max_arrival],
        'l9' : [20,[0]*max_arrival]
        }


        paths = {
            1:['l2','l8','l9'],
            2:['l4','l6'],
            3:['l4','l6','l7'],
            4:['l1','l4'],
            5:['l4','l1','l2'],
            6:['l3','l7'],
            7:['l5','l9'],
            8:['l8','l9','l5'],
            9:['l3'],
            10:['l1','l2']
        }
        

        arrival_time = [0] * max_arrival
        service_duration = [0] * max_arrival
        
        block_accept = [False] * max_arrival

        arrival_time[0] = 1
        avg_inter_arrival_time = 1/lamda

        for i in range(1,max_arrival):
            inter_arrival_time = npr.exponential(avg_inter_arrival_time)
            arrival_time[i] = arrival_time[i-1] + inter_arrival_time
        
        for i in range(0,max_arrival):
            service_duration[i] = npr.exponential((1/mu))
        

        current_path = random.randint(1, 10)
        
        block_accept[0] = False

        for link in paths[current_path]:
            links[link][1][0] = arrival_time[0] + service_duration[0]

        for i in range(1,max_arrival):
            current_path = random.randint(1, 10)

            for link in paths[current_path]:
                for j in range(i-1,0,-1):
                    if links[link][1][j] > arrival_time[i] and links[link][0] > 0:
                        links[link][0] = links[link][0] - 1
                        
                              
                if links[link][0] > 0:
                    block_accept[i] = False
                    
                else:
                    block_accept[i] = True
                    break
                    
                links[link][1][i] = arrival_time[i] + service_duration[i]
            

        
        print(sum(block_accept))
        b = sum(block_accept)/max_arrival

        bpr.append(b)
        offered_load.append(lamda)
        lamda = lamda - 3
    bpr.reverse()
    offered_load.reverse()
    print(bpr)
  

    ### plot graph ###

    x = np.array(offered_load)
    y = np.array(bpr)

    


    xnew = np.linspace(x.min(), x.max(), 18)

    spl = make_interp_spline(x, y, k=1)  

    ynew = spl(xnew)
    
    fig, ax = plt.subplots()
    
    
    ax.plot(xnew,ynew)

    ax.legend(["Discrete Event Simulation"])
    

    ax.set(xlabel='offered load(Erlang)', ylabel='system blocking probability',
        title="Blocking Probability of a M/M/k/k system")

    # ax.set_yscale('log')

    plt.ylim(0.2,1)
    plt.xlim(6,k)
    

    fig.savefig("results.png")
    plt.show()








    



    

