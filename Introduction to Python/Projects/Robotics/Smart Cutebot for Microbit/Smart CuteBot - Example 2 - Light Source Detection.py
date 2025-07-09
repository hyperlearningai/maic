# Smart Cutebot for micro:bit.
# Description: Detect and move towards a light source.

def on_forever():
    
    # If the light level recorded by the light sensor is greater than a certain number.
    # 0 = Pitch black <-> 255 = Bright white.
    if input.light_level() > 50:
        
        # Move forwards.
        cuteBot.motors(20, 20)
        
    else:
        
        # Otherwise stop the car.
        cuteBot.stopcar()


# Keep running the 'on_forever' function in the background.
basic.forever(on_forever)
