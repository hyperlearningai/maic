# Smart Cutebot for micro:bit.
# Description: Basic movements.

def on_button_pressed_a():

    # Move forwards (speed of left wheel: 0-100, speed of right wheel: 0-100).
    cuteBot.motors(20, 20)


def on_button_pressed_b():

    # Stop the car.
    cuteBot.stopcar()


# When the A button is pressed, run the 'on_button_pressed_a' function.
input.on_button_pressed(Button.A, on_button_pressed_a)

# When the B button is pressed, run the 'on_button_pressed_b' function.
input.on_button_pressed(Button.B, on_button_pressed_b)
