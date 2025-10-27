# Initialise the sonar variable
sonar = 0

# Initialise the wheels
RingbitCar.init_wheel(AnalogPin.P1, AnalogPin.P2)

# Perform obstacle detection and avoidance
def on_forever():

    # Read the distance (cm) to an object detected by the ultrasonic sensor
    # that is connected to the 0VS GVS pin.
    # Store the distance in the global sonar variable.
    global sonar
    sonar = sonarbit.sonarbit_distance(Distance_Unit.DISTANCE_UNIT_CM, DigitalPin.P0)

    # Display the current distance on the micro:bit board
    basic.show_number(sonar)

    # If the distance to the object is less than 15cm and is not 0cm
    # then avoid the object by turning.
    # Otherwise continue to move forwards.
    if sonar < 15 and sonar > 0:
        RingbitCar.freestyle(0, 50)
        basic.pause(500)
    else:
        RingbitCar.freestyle(50, 50)

# Indefinitely avoid obstacles when the A button is pressed
def on_button_pressed_a():

    # Move forwards
    RingbitCar.freestyle(50, 50)

    # Run a given function body continuously in an event-based forever loop
    # Reference: https://makecode.microbit.org/reference/basic/forever
    basic.forever(on_forever)

# Bind the function to the relevant input event handler
# Reference: https://makecode.microbit.org/reference/input/on-button-pressed
input.on_button_pressed(Button.A, on_button_pressed_a)