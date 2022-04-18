//------------------------------------------------------------------------
// ----------------
// Code template for C/C++ for discrete event program for single server with M/M/k/k model
// Read the introduction on how to calculate the value of k for your own project
//------------------------------------------------------------------------
// ----------------
maxArrival =  ;  // Total number of events you want to simulate, you need to adjust this value to get an accurate result
// based on the blocking probability
lambda =  ;  // Average arrival rate, you need to adjust this value to get different blocking probability.
// You can start from value k
mu = 1;  // Average service rate
k =  ;  // Calculate the k value based on the introduction of project - part 1
// Generate all the columns of the table based on exercise 3 in week 5
double arrival_time[maxArrival] = {0};
double service_duration[maxArrival] = {0};
int no_busy_server[maxArrival] = {0};
bool block_accept[maxArrival] = {0};  // 0: accept the request, 1: reject/block the request
double service_finish_time[maxArrival] = {0};
// Student defined parameters (optional)
// Generate the arrival time of each request.
// To do this, you need to generate the inter-arrival time between every two requests.
// The inter-arrival time should follow exponential distribution with mean value ave_inter_arrival_time.
arrival_time[0] = 1;
ave_inter_arrival_time = 1/lambda;
for (int i=1;i<maxArrival;i++) {
inter_arrival_time = ;  // Generate a random value following exponential distribution with mean
//value ave_inter_arrival_time
arrival_time[i] = arrival_time[i-1] + inter_arrival_time;
}
// Generate the service time of each request following exponential distribution with mean 1/mu
for (int i=0;i<maxArrival;i++) {
service_duration(i) =     ;  // Generate a random value following 
exponential distribution with
//mean value 1/mu
}
// Fill in the first row
no_busy_server[1] = 0;
block_accept[1] = 0;
service_finish_time[1] = arrival_time[1] + service_duration[1];
// Finish the remaining rows in the table
for (int i=1;i<maxArrival;i++) {
// Calculate the number of busy servers in the system when the new request arrvial
// Decide whether this request will be rejected or accepted
// Calculate the finish time of this request
}
// Calculate the total number of blocked request and then calculate the blocking probability
//End of the program