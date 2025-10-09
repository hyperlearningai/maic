def on_button_pressed_a():

    # Move forwards (lspeed: 0-100, rspeed: 0-100).
    cuteBot.motors(20, 20)

def on_button_pressed_b():

    # Reverse (lspeed: 0-100, rspeed: 0-100).
    cuteBot.motors(-20, -20)

def on_button_pressed_ab():

    # Stop the car.
    cuteBot.stopcar()


# When the A button is pressed, run the 'on_button_pressed_a' function.
input.on_button_pressed(Button.A, on_button_pressed_a)

# When the B button is pressed, run the 'on_button_pressed_b' function.
input.on_button_pressed(Button.B, on_button_pressed_b)

# When the A and B buttons are pressed together, run the 'on_button_pressed_ab' function.
input.on_button_pressed(Button.AB, on_button_pressed_ab)