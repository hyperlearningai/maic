def on_forever():

    # If the light level is greater than a certain number e.g. 200.
    # 0 = pitch black <---> 255 = bright white.
    if input.light_level() > 200:

        # Move forwards.
        cuteBot.motors(20, 20)

    else:

        # Otherwise stop the car.
        cuteBot.stopcar()

# Keep running the 'on_forever' function in the background in a forever loop.
basic.forever(on_forever)