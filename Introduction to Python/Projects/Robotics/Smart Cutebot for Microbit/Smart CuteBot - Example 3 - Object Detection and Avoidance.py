# Smart Cutebot for micro:bit.
# Description: Object detection and avoidance.

# Global variables that can be accessed by any function.
sonar = 0
cuteBot.motors(20, 20)


def on_forever():
    global sonar
    
    # Get the distance to the closest object in centimeters using the ultrasonic sensor.
    sonar = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    
    # If the distance to the closest object is less than a certain distance
    # e.g. 15cm, then stop the car.
    if sonar < 15 and sonar > 1:
        cuteBot.stopcar()
        basic.pause(200)
        
    else:
        
        # Otherwise move forwards.
        cuteBot.motors(20, 20)


# Keep running the 'on_forever' function in the background.
basic.forever(on_forever)
