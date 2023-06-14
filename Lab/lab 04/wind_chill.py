"""CS 108 - Lab 4.1

Program that calculates wind chill temperature and how many layers to wear. 

@author: Stella Kim (sk98)
@author: ZeAi Sun (zs35)
@date: Fall, 2021
"""
#Get two input from the user. 
temp = float(input('Temperature: '))
wind_speed = float(input('Wind speed: '))

#Condition for calculating invalid input.
if wind_speed < 2 or temp < -58 or temp > 41:
    print('Invalid input')

#Calculate wind chill and how many layers to wear. 
else:
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * wind_speed**0.16 + 0.4275 * temp * wind_speed**0.16
    print('Wind chill:', wind_chill)
    if wind_chill <-40:
        print('Stay home!')
    elif wind_chill < -10:
        print('Four layers')
    elif wind_chill < 20:
        print('Three layers')
    elif wind_chill < 40:
        print('Two layers')
    else:
        print('One layer')


