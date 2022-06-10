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
    lamda = 20
    offered_load =[]
    for i in range(0,6):
        links = {
        'l1' : 10,
        'l2' : 15,
        'l3' : 10,
        'l4' : 20,
        'l5' : 15,
        'l6' : 20,
        'l7' : 15,
        'l8' : 15,
        'l9' : 20
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
        
        max_arrival = 13

        arrival_time = [0] * max_arrival
        service_duration = [0] * max_arrival
        no_busy_server = [0] * max_arrival
        block_accept = [False] * max_arrival
        service_finish_time = [0] * max_arrival

        arrival_time[0] = 1
        avg_inter_arrival_time = 1/lamda

        for i in range(1,max_arrival):
            inter_arrival_time = npr.exponential(avg_inter_arrival_time)
            arrival_time[i] = arrival_time[i-1] + inter_arrival_time
        
        for i in range(0,max_arrival):
            service_duration[i] = npr.exponential((1/mu))

        no_busy_server[0] = 0

        block_accept[0] = False

        service_finish_time[0] = arrival_time[0] + service_duration[0]

        for i in range(1,max_arrival):
            current_path = random.randint(1, 10)

            for j in range(i-1,0,-1):
                if service_finish_time[j] > arrival_time[i]:
                    for link in paths[current_path]:
                        links[link] = links[link] - 1

            for link in paths[current_path]:      
                if links[link] > 0:
                    block_accept[i] = False
                    service_finish_time[i] = arrival_time[i] + service_duration[i]
                    
                else:
                    block_accept[i] = True
                    
                    break
        
        print(sum(block_accept), lamda)
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

    ax.set_yscale('log')

    plt.ylim(10**-6,0.3)
    plt.xlim(2,20)
    

    fig.savefig("results.png")
    plt.show()








    



    

