import random
from time import sleep
#Class for creating a TrafficLight object
class TrafficLight:
    def __init__(self,car_value,state):
        self.value = car_value
        self.state = state
    def change(self,state):
        self.state = state

    def cars_coming(self):
        x = random.randint(0,5)
        return x
    def cars_leaving(self):
        y=random.randint(5,10)
        if y>self.value:
            y = random.randint(5,self.value)
        return y


#Traffic Lights
tr1 = TrafficLight(random.randint(0,101),False)
tr2 = TrafficLight(random.randint(0,101),False)
tr3 = TrafficLight(random.randint(0,101),False)

Traffic_Lights = [tr1,tr2,tr3]
#Function that evalutates which Trafic Light turns on first
def find_tf(Traffic_Lights):
    max = Traffic_Lights[0].value
    max_light = 0
    counter = 0
    
    for i in range (1,3):
        if Traffic_Lights[i].value>max:
            max = Traffic_Lights[i].value
            max_light = i
        elif Traffic_Lights[i].value == max:
            counter+=1
            max_temp = i

    if counter == 1:
        for i in range (1,3):
            if max == Traffic_Lights[i].value:
                temp = i 
        traffic_light = random.choice[max_light,temp]
        return traffic_light
    elif counter == 2:
        traffic_light = random.choice[0,1,2]
        return traffic_light    
    return max_light    

if __name__ == '__main__':
    while True:
        max = find_tf(Traffic_Lights)
        Traffic_Lights[max].change(True)
        for tf in Traffic_Lights:
            if tf.state == True:
                print('There are ',tf.value,'cars in the Green Traffic Light')
                temp = tf.cars_leaving()
                sleep(2)
                print(temp,' cars left ')
                tf.value -= temp
            else:
                print('There are',tf.value,' cars in this Red Traffic Light')
                temp = tf.cars_coming()
                sleep(2)
                print(temp, 'cars came')
                tf.value += temp
            tf.change(False)