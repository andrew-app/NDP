import math
import pandas
import numpy.random as npr
import random

if __name__ == "__main__":
    maxArrival = 10

    avg_arrival = random.random()

    arrival_time = [1]
    service_duration = [0] * maxArrival
    no_busy_server = [0] * maxArrival
    block_arrival = [False] * maxArrival
    service_finish_time = [0] * maxArrival

    mu = 1

    k = math.floor(42/2)

    avg_inter_arrival_time = 1/avg_arrival

    for i in range(1,maxArrival):
        inter_arrival_time = npr.exponential()
        arrival_time.append(round(arrival_time[i-1] + inter_arrival_time,3))

    for i in range(0,maxArrival):
        service_duration[i] = round(npr.exponential(),3)



    print(arrival_time)
    print(service_duration)



    

