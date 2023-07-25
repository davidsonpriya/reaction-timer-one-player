wrong_start = False
start_time = 0
game_running = False
end_time = 0

def on_pin_pressed_p0():
    global start_time, game_running
    basic.show_number(3)
    basic.show_number(2)
    basic.show_number(1)
    basic.clear_screen()
    wrong_start = False
    basic.pause(1000 + randint(0, 2000))
    if not (wrong_start):
        start_time = input.running_time()
        game_running = True
        basic.clear_screen()
        led.plot(randint(0, 4), randint(0, 4))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p1():
    global end_time, game_running, wrong_start
    if game_running:
        end_time = input.running_time()
        basic.show_leds("""
            . . # . .
            . # . # .
            . # # # .
            . # . # .
            . # . # .
            """)
        basic.pause(1000)
        basic.clear_screen()
        basic.show_number((end_time - start_time) / 1000)
        game_running = False
    else:
        wrong_start = True
        basic.show_leds("""
            . . . . .
            # . # . .
            . # . . .
            # . # . .
            . . . . .
            """)
        game_running = False
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
