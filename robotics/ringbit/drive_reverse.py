# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Move forwards
def on_button_pressed_a():
    RingbitCar.forward()

# Reverse
def on_button_pressed_b():
    RingbitCar.back()

# Brake
def on_button_pressed_ab():
    RingbitCar.brake()

# Bind the functions to the relevant input event handlers
# Reference: https://makecode.microbit.org/reference/input/on-button-pressed
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_button_pressed(Button.AB, on_button_pressed_ab)