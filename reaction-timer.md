# Reaction Timer Game
We will be making a Reaction Timer game. In this game, we will program microbit to measure the time it takes for player to react.

## Step 1
Under ``||input:Input||``, select ``||Input: on pin P0 pressed||`` block.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
})
```

## Step 2
Under ``||Variables||``, select ``||Variables:Make a Variable||``. 
Enter the variable name as **``bad_start``**. Add a ``||Variable:Set bad_start to||`` block to your code.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = 0
})
```

## Step 3
From ``||logic:Logic||``, bring the ``||Logic:False||`` block and snap it instead of 0.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
})
```

## Step 4
Make another ``||variable:Variable||`` and name it as **``start_game_timer``**. 
Bring ``||Variables:set start_game_timer||`` and add it to your code. 
Again, from ``||logic:Logic||`` bring the ``||Logic:False||`` block and place it instead of 0.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
})
```

## Step 5
From ``||basic:Basic||``, add ``||Basic: show icon||``. 
Select a Heart or any other image to signal the start of the game.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    
})
```

## Step 6
From ``||basic:Basic||``, add ``||Basic: clear screen||``.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    
})
```
## Step 7 
From ``||basic:Basic||``, add ``||Basic: pause (ms) 100||``. Change the value from 100 to 1000
```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)

})
```

## Step 8
Under ``||logic:Logic||``, find ``||logic: if-True-then||`` block and add it after ``||basic: pause (ms) 1000||``.
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

## Step 9
From ``||logic:Logic||``, get a comparison block ``||logic: 0 = 0 ||`` and snap it to replace ``||logic:True||`` within the ``||Logic: if||`` block.
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
## Step 10
From ``||variables:Variables||``, drag ``||Variables:bad_start||`` and from ``||logic:Logic||``, drag ``||logic:True||`` into the comparison block.
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

## Step 11
From ``||variables: Variables||``, get a ``||variables:set start_game_timer ||``.
This step will start the game timer.

```blocks 
input.onPinPressed(TouchPin.P0, function () {
    bad_start = false
    start_game_timer = false
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
    basic.pause(1000)
    if (bad_start != true) {
        start_game_timer = true
    }
})
```

## Step 12
From ``||variables: Variables||``, get a ``||variables:set start_time ||``.
Also, get ``||input: running time||`` from ``||input:Input||``. 
This step will record the current time as start time for the game.
Note" If you can't find ``||input: running time||`` then click on ``||input: Input||`` and
 then on ``||input: More||`` 


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

## Step 13
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

## Step 14
Add ``on pin pressed`` block again. Change the pin ``P0`` to ``P1``.

```blocks 
input.onPinPressed(TouchPin.P1, function () {
   
})
```

## Step 15
Add ``if block`` from Logic. Add a ``comparison`` block from Math and place it instead of ``True``
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == 0) {
        
    }
})
```

## Step 16
From ``Logic``, drag ``True`` and place it instead of 0
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {

    }
})
```

## Step 17
Add ``set`` block for marking the end time for game. Add ``running time`` from ``Input`` menu item. You can also search for the blocks you can't locate easily.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        }
})
```

## Step 18
Add ``showIcon`` and select a tick to represent good start.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
    }
})
```

## Step 19
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

## Step 20
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

## Step 21
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

## Step 22
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

## Step 23
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

## Step 24
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

## Step 25
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

## Step 26
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