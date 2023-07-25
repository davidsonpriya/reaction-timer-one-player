let bad_start = false
let start_game_timer = false
let start_time = 0
let end_time = 0
let Reaction_Time = 0
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)
    if (!(bad_start)) {
        start_game_timer = true
        start_time = input.runningTime()
        led.plot(2, 2)
    }
})
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = (end_time - start_time) / 1000
        basic.showNumber(Reaction_Time)
    } else {
        bad_start = true
        basic.showIcon(IconNames.No)
    }
})
