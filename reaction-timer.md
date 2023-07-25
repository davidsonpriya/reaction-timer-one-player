# Reaction Timer Game
We will be making a Reaction Timer game. In this game, we will program microbit to measure the time it takes for player to react.
You will not need ``||Basic: on start||`` and ``||Basic: forever||`` blocks so get rid of these.
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
From ``||basic:Basic||``, add ``||Basic: pause (ms) 100||``. 
Change the value from 100 to 1 second. It will automatically be converted to 1000
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
From ``||logic:Logic||``, get a comparison block ``||logic: 0 = 0 ||`` 
and snap it to replace ``||logic:true||`` within the ``||Logic: if||`` block.

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
From ``||variables:Variables||``, drag ``||Variables:bad_start||`` and then
from ``||logic:Logic||``, drag ``||logic:true||`` into the comparison block.
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
From ``||variables: Variables||``, get ``||variables:set start_game_timer ||`` and place it within ``||Logic:if||`` loop.
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
Also, get ``||input: running time||`` from ``||input:Input||`` and snap it to **``0``** in ``||variables:set start_time = 0 ||``. 
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
Find ``||LED:plot x() y()||`` block under ``||led:LED||``. 
Change the values for **``x``** and **``y``**. 
This will be the position of marker to start the game. 

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
Add another ``||input:on pin P0 pressed||`` block. Change the pin **``P0``** to **``P1``**.

```blocks 
input.onPinPressed(TouchPin.P1, function () {
   
})
```

## Step 15
Add ``||Logic:if-true-then||`` from ``||logic:Logic||``. 

```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (true) {
        
    }
})
```

## Step 16
Add a comparison ``||logic: 0 = 0||`` block from ``||logic:Logic||`` and snap it to 
replace ``||Logic:true||``. 
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (0 == 0) {
        
    }
})
```
## Step 17
Next add ``||variable:start_game_timer||`` and drag it to replace 
the first 0 within ``||Logic:if||`` block.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == 0) {
        
    }
})
```

## Step 18
From ``||logic:Logic||``, drag ``||logic:true||`` and place it instead of 0
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {

    }
})
```

## Step 19
Add ``||variables: set end_time||`` block for marking the end time for game. 
from ``||input:Input||``, add ``||Input:running time||``. Remember, you can also search for the blocks you can't locate easily.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        }
})
```

## Step 20
Add ``||Basic: show icon||`` and select an icon to represent good start.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
    }
})
```

## Step 21
Next add, ``||Basic: pause (ms) 100||`` and ``||Basic: clear screen||``. 
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

## Step 22
Next, we need to calculate the reaction time. 
Make a new variable ``||variable:Reaction_Time||``. Use ``||variable:set Reaction_Time||`` block to get started.
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

## Step 23
From ``||math:Math||``, get the calculate block ``||math: 0 + 0||``.

```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = 0 + 0
    }
})
```



## Step 24
Change the **``+``** to **``/``** for division and value of the second 0 to 1000
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

## Step 25
Drag a second calculate block ``||math: 0 + 0||`` and snap it to the first **``0``**. 
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = (0 + 0) / 1000
        
    }
})
```

## Step 26
From ``||variables:Variables||``, bring ``||variables:end_time||`` to replace the first **``0``** and
 ``||variables:start_time||`` to replace the second **``0``**. 
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

## Step 27
We will now display the reaction time. From ``||basic:Basic||``, use ``||basic:show number (0)||``.
```blocks 
input.onPinPressed(TouchPin.P1, function () {
    if (start_game_timer == true) {
        end_time = input.runningTime()
        basic.showIcon(IconNames.Yes)
        basic.pause(100)
        basic.clearScreen()
        Reaction_Time = (end_time - start_time) / 1000
        basic.showNumber(0)
    }
})
```

## Step 28
From ``||variables:Variables||`` snap ``||variables:reaction_Time||`` to replace the ``0`` in ``||basic:show number (0)||``.
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

## Step 29
Click on the ``||Logic:+||`` at the end of ``||Logic:if||`` block. An additional ``||Logic:else||`` will appear.
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

## Step 30
Within ``||Logic:else||`` block, add ``||Variable:set bad_start = 0||`` block. 
From ``||logic:Logic||``, drag ``||Logic:true||`` and snap it to **``0``** in ||Variable:set bad_start||``.
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

## Step 31
Add ``||Basic:show icon||`` for displaying a bad start. You can select an X or any other symbol for this.
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