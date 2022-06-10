import math
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline

class event_sim:
    def __init__(self,maxArrival, avg_arrival, k, sys_util):
        # instantiate max number of arrivals, k and offered load
        self.maxArrival = maxArrival
        self.avg_arrival = avg_arrival
        self.k = k
        self.sys_util = sys_util
    
    def result(self):
        npr = default_rng()
        
        arrival_time = [1]
        mu = 1

        service_duration = [0] * self.maxArrival
        no_busy_server = [0] * self.maxArrival
        block_arrival = [False] * self.maxArrival
        service_finish_time = [0] * self.maxArrival

    
        avg_inter_arrival_time = 1/self.avg_arrival

        for i in range(1,self.maxArrival):
            inter_arrival_time = npr.exponential(avg_inter_arrival_time)
            arrival_time.append(round(arrival_time[i-1] + inter_arrival_time,4))

        
        for i in range(0,self.maxArrival):
            service_duration[i] = round(npr.exponential(1/mu),4)
            service_finish_time[i] = round(arrival_time[i] + service_duration[i],4)


        for i in range(1,self.maxArrival):
            current_load = 0
            for j in range(i,0,-1):
                if service_finish_time[j] > arrival_time[i]:
                    current_load += 1
            no_busy_server[i] = current_load
            if no_busy_server[i] == self.k:
                block_arrival[i] = True
                current_load = 0
                service_finish_time[i] = 0
        no_block_arrival = block_arrival.count(True)

        self.sys_util = no_busy_server
        return no_block_arrival/self.maxArrival
        



if __name__ == "__main__":

    k = math.floor(42/2)
    it = 100
    mu = 1

    avg_bpr = [[],[],[],[],[],[]]

    #discrete event simulation
    for i in range(0,6):
        offered_load = []
        
        system_util = []
        erl = 500
        simulation = event_sim(erl, k, k, 0)#first simulation uses k as offered load value

        offered_load.append(k)
        avg_bpr[0].append(simulation.result())
        system_util.append((sum(simulation.sys_util)/len(simulation.sys_util))/k)
        
        j = 1
        for event in range (k-3,3,-3): #run 5 simulations decreasing offered load(lambda) by 3 each time
            simulation.maxArrival = erl + it
            simulation.avg_arrival = event
            avg_bpr[j].append(simulation.result())
            offered_load.append(event)
            system_util.append((sum(simulation.sys_util)/len(simulation.sys_util))/k)
            j += 1

    offered_load = offered_load[::-1]

    
    system_bpr = []
    
    
    for vals in avg_bpr:
        
        system_bpr.append(sum(vals)/6)
    
    system_bpr.reverse()
    system_util.reverse()

    ### markov chain simulation ###

    Q = 0

    mkbpr = [] #blocking probability from markov chain calculations

    MaxNa = 500

    Na = 0

    Nb = 0

    service_rate = 1

    for arrival_rate in range (k,3,-3):
        

        while(Na < MaxNa):
            R = np.random.uniform()

            if R <= arrival_rate/(arrival_rate+Q*service_rate):
                Na += 1
                if Q == k:
                    Nb += 1
                else:
                    Q += 1
            else:
                Q -= 1
    
        mkbpr.append(Nb/Na)

        MaxNa = MaxNa + 100

    mkbpr.reverse()
    

    ### plot graph ###

    x = np.array(offered_load)
    y = np.array(system_bpr)

    y_sys = np.array(system_util) * 100


    ymk = np.array(mkbpr)

    xnew = np.linspace(x.min(), x.max(), 18)

    spl = make_interp_spline(x, y, k=1)  

    ynew = spl(xnew)
    
    fig, ax = plt.subplots()
    
    ax.plot(x,y)
    ax.plot(xnew,ynew)

    ax.legend(["Markov Chain Simulation","Discrete Event Simulation"])
    

    ax.set(xlabel='offered load(Erlang)', ylabel='system blocking probability',
        title="Blocking Probability of a M/M/k/k system")

    ax.set_yscale('log')

    plt.ylim(10**-5,1)
    plt.xlim(8,k)
    

    fig.savefig("results.png")
    plt.show()

    plt.plot(x,y_sys)


    plt.xlim(6,k)

    plt.xlabel('offered load(Erlang)') 
    plt.ylabel('System Utilization (%)')
    plt.title("System Utilization of M/M/k/k")

    plt.show()







    



    

