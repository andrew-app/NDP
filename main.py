import math
import numpy as np
from numpy.random import default_rng
import random
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

class event_sim:
    def __init__(self,maxArrival, avg_arrival, k):
        # instantiate max number of arrivals, k and offered load
        self.maxArrival = maxArrival
        self.avg_arrival = avg_arrival
        self.k = k
        
    
    def result(self):
        npr = default_rng()
        
        arrival_time = [1]
        mu = 1

        service_duration = [0] * self.maxArrival
        no_busy_server = [0] * self.maxArrival
        block_arrival = [False] * self.maxArrival
        service_finish_time = [0] * self.maxArrival

        current_load = 0

        avg_inter_arrival_time = 1/self.avg_arrival

        
        for i in range(0,self.maxArrival):
            if i > 0:
                inter_arrival_time = npr.exponential(avg_inter_arrival_time)
                arrival_time.append(round(arrival_time[i-1] + inter_arrival_time,4))
            
            service_duration[i] = round(npr.exponential(1/mu),4)
            service_finish_time[i] = round(arrival_time[i] + service_duration[i],4)

            if i > 0 and service_finish_time[i-1] >= arrival_time[i]:
                current_load += 1
            no_busy_server[i] = current_load
            if no_busy_server[i] == int(self.k):
                no_busy_server[i] = int(self.k)
                block_arrival[i] = True
                current_load = 0
                service_finish_time[i] = 0


        no_block_arrival = block_arrival.count(True)

        return no_block_arrival/self.maxArrival
        



if __name__ == "__main__":

    k = math.floor(42/2)

    offered_load = []

    system_bpr = []

    mu = 1
    simulation = event_sim(2000, k, k)#first simulation uses k as offered load value

    offered_load.append(k)
    system_bpr.append(simulation.result())

    for event in range (k-3,3,-3): #run 5 simulations decreasing offered load by 3 each time
        simulation.avg_arrival = event
        offered_load.append(event)
        system_bpr.append(simulation.result())

    offered_load = offered_load[::-1]

    system_bpr = system_bpr[::-1]

    #plot graph

    x = np.array(offered_load)
    y = np.array(system_bpr)

    xnew = np.linspace(x.min(), x.max(), 18)

    spl = make_interp_spline(x, y, k=3)  

    ynew = spl(xnew)
    fig, ax = plt.subplots()
    ax.plot(xnew,ynew)

    ax.set(xlabel='offered load(Erlang)', ylabel='system blocking probability',
        title="Blocking Probability of a M/M/k/k system")
    ax.grid()

    fig.savefig("results.png")
    plt.show()






    



    

