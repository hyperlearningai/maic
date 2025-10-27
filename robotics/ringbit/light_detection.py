# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Follow a light source
def on_forever():

    # Check the light level using a comparison operator.
    # If the light level is greater than 200 then move forwards otherwise brake.
    # Reference: https://makecode.microbit.org/reference/input/light-level
    if input.light_level() > 200:
        RingbitCar.forward()
    else:
        RingbitCar.brake()

# Run a given function body continuously in an event-based forever loop
# Reference: https://makecode.microbit.org/reference/basic/forever
basic.forever(on_forever)