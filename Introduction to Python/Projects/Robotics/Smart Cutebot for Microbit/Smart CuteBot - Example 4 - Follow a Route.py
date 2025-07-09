# Smart Cutebot for micro:bit.
# Description: Follow a route.

def on_forever():

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
        
        # Move forwards.
        cuteBot.motors(20, 20)


# Keep running the 'on_forever' function in the background.
basic.forever(on_forever)
