# Global speed, distance and time tracking variables.
forever_loop_active = False
start_time = input.running_time()
initial_distance_to_object = -1
closest_distance_to_object = 15
speed = -1


def on_button_pressed_a():
    """
    This function will reset the global distance and time tracking variables, 
    clear the Micro:bit LED screen, and 'activate' the forever loop.
    """
    
    # Reset the speed, distance and time tracking variables.
    global forever_loop_active, start_time
    global initial_distance_to_object, speed
    start_time = input.running_time()
    initial_distance_to_object = -1
    speed = -1

    # Clear the Micro:bit LED screen.
    basic.clear_screen()

    # 'Activate' the forever loop.
    forever_loop_active = True


def on_forever():
    """
    This function will move the car forwards at a constant speed, 
    measure the distance to the approaching object, 
    stop the car when it is within the specified distance to the object, 
    and calculate & display the linear speed at which it was travelling.
    """

    global forever_loop_active, start_time
    global initial_distance_to_object, closest_distance_to_object, speed

    # Determine whether the forever loop is active.
    if forever_loop_active:

        # Move forwards at a constant speed.
        cuteBot.motors(20, 20)

        # Measure the distance to the approaching object in cm 
        # using the ultrasonic sensor.
        distance_to_object = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)

        # Determine the initial distance to the object when it was first detected.
        if initial_distance_to_object == -1 and distance_to_object > 1:
            initial_distance_to_object = distance_to_object

        # Determine whether the distance to the object is 
        # less than the specified threshold e.g. 15cm.
        if distance_to_object <= closest_distance_to_object and distance_to_object > 1:

            # Stop the car.
            cuteBot.stopcar()

            # Calculate the speed (speed = distance / time).
            distance_cm = initial_distance_to_object - distance_to_object
            time_seconds = (input.running_time() - start_time) / 1000
            speed = distance_cm / time_seconds

            # Display the speed on the Micro:bit LED screen.
            basic.show_number(speed)

            # 'Deactivate' the forever loop until the A button is pressed again.
            forever_loop_active = False

    else:

        # Stop the car.
        cuteBot.stopcar()

        # Continue to display the last recorded speed  
        # on the Micro:bit LED screen.
        if speed > 0:
            basic.show_number(speed)


# Specify the event handler for button A.
input.on_button_pressed(Button.A, on_button_pressed_a)

# Run the 'on_forever' function in the background in a forever loop.
basic.forever(on_forever)