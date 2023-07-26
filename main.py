bad_start = False
start_game_timer = False
start_time = 0
end_time = 0
Reaction_Time = 0

def on_pin_pressed_p0():
    global bad_start, start_game_timer, start_time
    bad_start = False
    start_game_timer = False
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.pause(1000)
    if not (bad_start):
        start_game_timer = True
        start_time = input.running_time()
        led.plot(2, 2)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p1():
    global end_time, Reaction_Time, bad_start
    if start_game_timer == True:
        end_time = input.running_time()
        basic.show_icon(IconNames.YES)
        basic.pause(100)
        basic.clear_screen()
        Reaction_Time = (end_time - start_time) / 1000
        basic.show_number(Reaction_Time)
    else:
        bad_start = True
        basic.show_icon(IconNames.NO)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
