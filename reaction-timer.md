# Reaction Timer Game
We will be making a Reaction Timer game. In this game, we will program microbit to measure the time it takes for player to react.

## Step 1
Under ``||input||``, select ``||on pin P0 pressed||`` block.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
})
```

## Step 2
Select ``||Variables:Make a Variable||``. Enter the variable name as ``bad_start``. Add a ``Set bad_start`` block to your code.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = 0
})
```

## Step 3
From Logic, bring the ``||Logic:False||`` block and snap it instead of 0.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
})
```

## Step 4
Make another variable and name it as ``start_game_timer``. Bring set start_game_timer and add it to your code. Again, bring the ``False`` block and place it instead of 0.
```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    
})
```
## Step 5
From **Basic**, add ``showIcon``. Select a Heart or any other image to signal the start of the game.
```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    
})
```

## Step 6
From **Basic**, add ``clearScreen``.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    
})
```
## From **Basic**, add ``pause``. Change the value from 100 to 1000
```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)

})
```

## Step 7
Under **Logic**, find ``if`` block and add it after ``pause``.
```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)
    if (true) {
        
    }
})
```

## Step 8
Add a comparison block and place it instead of ``True`` .
```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)
    if (0 == 0) {
        
    }
})
```
## Drag ``bad_start`` from Variables and ``True`` from Logic.
```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)
    if (bad_start != true) {
        
    }
})
```

## Step 9
Add a ``set`` block from variable to set values for starting the game timer and take the start time for the game.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)
    if (bad_start != true) {
        start_game_timer = true
        start_time = input.runningTime()
    }
})
```

## Step 10
find ``plot x() y()`` block under LED. Change the values for x and y. This will be the position of LED that will light up for for dot marker. 

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)
    if (bad_start != true) {
        start_game_timer = true
        start_time = input.runningTime()
        led.plot(2, 2)
    }
})
```

## Step 11
Add ``on pin pressed`` block again. Change the pin ``P0`` to ``P1``.

```blocks 
input.onPinPressed(TouchPin.P1, function () {
   
})
```

## Step 12
Add ``if block`` from Logic. Add a ``comparison`` block from Math and place it instead of ``True``
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == 0) {
        
    }
})
```

## Step 13
From ``Logic``, drag ``True`` and place it instead of 0
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {

    }
})
```

## Step 14
Add ``set`` block for marking the end time for game. Add ``running time`` from ``Input`` menu item. You can also search for the blocks you can't locate easily.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        }
})
```

## Step 15
Add ``showIcon`` and select a tick to represent good start.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
    }
})
```

## Step 16
Next add, pause and clear screen. 
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
    }
})
```

## Step 17
Next, we need to calculate the reaction time. Make a variable ``Reaction_time``. Use ``set`` block to get started.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = 0
    }
})
```

## Step 18
Drag the ``calculate`` block out and change the operator to ``/`` for division and value to 1000
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = 0 / 1000
    }
})
```

## Step 18
Drag another ``calculate`` block and snap it instead of ``0``. From **Variables**, bring ``end_time`` and ``start_time``. See the image to check out how it needs to be done.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = (end_time - start_time) / 1000
        
    }
})
```

## Step 19
Display the reaction time. Use ``showNumber`` and from **Variables** snap ``reaction_Time`` to replace the ``0``.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = (end_time - start_time) / 1000
        basic.showNumber(Reaction_Time)
    }
})
```

## Step 20
Click on the ``+`` at the end of ``if`` block. An additional ``else`` will appear.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = (end_time - start_time) / 1000
        basic.showNumber(Reaction_Time)
    } else {
    }
})
```

## Step 21
Within ``else`` block, add ``set`` block and select bad_start. Drag out ``True`` from **Logic** and snap it to set_start.
```blocks 
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
    }
})
```

## Step 22
Add ``showIcon`` for displaying a bad start. You can select a X or any other symbol for this.
```blocks 
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
```

## Completed code for ``on pin P1 pressed``
```blocks 
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
```