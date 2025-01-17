"""
Different Screens
Most people want to have a main menu with various different screens.
You need a variable to store your current screen. Then, in the
update and draw functions, you have and if statement to check
what the current screen is.

Eventually you will want to have an update and draw function for each screen.
"""

import arcade


WIDTH = 640
HEIGHT = 480

current_screen = "menu"

ball_x = 0


def update(delta_time):
    global ball_x

    if current_screen == "play":
        ball_x += 1


def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()


def on_key_press(key, modifiers):
    global current_screen

    if current_screen == "menu":
        if key == arcade.key.I:
            current_screen = "instructions"
        elif key == arcade.key.P:
            current_screen = "play"
        elif key == arcade.key.ESCAPE:
            exit()
    elif current_screen == "instructions":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"
    elif current_screen == "play":
        if key == arcade.key.ESCAPE:
            current_screen = "menu"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)
    arcade.draw_text("Main Menu", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("I for Instructions", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")
    arcade.draw_text("P to Play", WIDTH/2, HEIGHT/2-90,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_instructions():
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("ESC to go back", WIDTH/2, HEIGHT/2-60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_play():
    arcade.set_background_color(arcade.color.ORANGE_RED)
    arcade.draw_text("Play", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")

    arcade.draw_circle_filled(ball_x, 100, 30, arcade.color.WHITE)


if __name__ == '__main__':
    setup()
