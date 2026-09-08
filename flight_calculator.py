#Note: this program was writen using github copilots ghost writing feature by writing a text prompt
#to describe the functionality of the desired functions i wanted to create. 

#implement a function called calculate_flight_time that takes weight in grams(weight_grams).
#It returns active flight time in minuits for a given payloads weight using this formula, 
# T(w) = 180 - 0.1w. T is resulting active flight time in minuits and w is payload weight in
#grams, which must be greater than or equal to 0 grams. if the formula produces a negative value,
#return 0, if weight_grams is less than 0, raise a ValueError with the message "Weight must be 
#greater than or equal to 0 grams."

def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("Weight must be greater than or equal to 0 grams.")
    
    flight_time = 180 - 0.1 * weight_grams
    return max(0, flight_time)

#create a function called flight_time_table that takes in max weight in grams(max_weight_grams),
#and step_grams. the function returns a list of (weight, flight_time) pairs for payload weights
#from 0 up to and including max_weight_grams, in increments of step_grams. the function must internally
#call calculate_flight_time() for each weight rather than recalculating the formula

def flight_time_table(max_weight_grams, step_grams):
    table = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    return table

