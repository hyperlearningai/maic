# Smart Cutebot for micro:bit.
# Description: Maintain a consistent distance to a slower car on a route.

# Global variables that can be accessed by any function.
sonar = 0

def on_forever():

    # Get the distance to the closest object in centimeters using the ultrasonic sensor.
    global sonar
    sonar = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)

    # If the left line-tracking sensor no longer detects a black line.
    # But the right line-tracking sensor continues to detect a black line.
    # This means that the track is turning right.
    if cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        
        # Turn right by controlling the speeds of the individual wheels.
        cuteBot.motors(20, 0)

    # If the left line-tracking sensor continues to detect a black line.
    # But the right line-tracking sensor no longer detects a black line.
    # This means that the track is turning left.
    if cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        
        # Turn left by controlling the speeds of the individual wheels.
        cuteBot.motors(0, 20)

    # If the left line-tracking sensor continues to detect a black line.
    # And the right line-tracking sensor also continues to detect a black line.
    # That means that the track is continuing in a straight line.
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        
        # If we are approaching a slower car, then stop to
        # maintain a consistent distance.
        if sonar > 4 and sonar < 8:
            cuteBot.motors(0, 0)
            
        # If we are dangerously close to the car in front then reverse.
        elif sonar < 4:
            cuteBot.motors(-20, -20)
            
        # Otherwise move forwards.
        else:
            cuteBot.motors(20, 20)


# Keep running the 'on_forever' function in the background.
basic.forever(on_forever)
