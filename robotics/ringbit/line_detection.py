# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Follow a black line
def on_forever():

    # Left infrared sensor detects deviation from the black line.
    # Stop the right wheel and slow the left wheel in order to turn.
    if RingbitCar.tracking(RingbitCar.TrackingStateType.TRACKING_STATE_2):
        RingbitCar.freestyle(25, 0)
        basic.pause(250)

    # Right infrared sensor detects deviation from the black line.
    # Stop the left wheel and slow the right wheel in order to turn.
    if RingbitCar.tracking(RingbitCar.TrackingStateType.TRACKING_STATE_1):
        RingbitCar.freestyle(0, 25)
        basic.pause(250)

    # Normal moving speed
    RingbitCar.freestyle(50, 50)

# Move indefinitely when the A button is pressed
def on_button_pressed_a():

    # Move forwards
    RingbitCar.freestyle(50, 50)

    # Run a given function body continuously in an event-based forever loop
    # Reference: https://makecode.microbit.org/reference/basic/forever
    basic.forever(on_forever)

# Bind the function to the relevant input event handler
# Reference: https://makecode.microbit.org/reference/input/on-button-pressed
input.on_button_pressed(Button.A, on_button_pressed_a)