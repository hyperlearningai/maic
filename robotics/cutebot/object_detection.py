# Global variable that can be accessed by any function.
sonar = 0

# Move forwards at a constant speed.
cuteBot.motors(20, 20)


def on_forever():
    global sonar

    # Get the distance to the closest object in cm using the ultrasonic sensor.
    sonar = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)

    # If the distance to the closest object is less than a certain distance
    # e.g. 15cm, then stop the car.
    if sonar < 15 and sonar > 1:
        cuteBot.stopcar()
        basic.pause(200)

    else:

        # Otherwise move forwards.
        cuteBot.motors(20, 20)


# Keep running the 'on_forever' function in the background in a forever loop.
basic.forever(on_forever)