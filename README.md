# blink1

### Status usage
Script using blink(1) dongle and can make some actions regarding a given status
```
/usr/bin/python3 status.py (available|ok|busy|alert|off) "Any reason (optional)"
```
Basically, `/usr/bin/python3 status.py alert "Something went wrong!"` will activate some actions de/activated in `congig.py`
Possible actions would be

    - Desktop notifications
    - Simple API call to any server (URL to be set within [config.py])
    - Send an SMS to any number

|                            | HTML                                                        |
|----------------------------|-------------------------------------------------------------|
| available, ok              | Green light on dongle                                       |
| busy                       | Red light on dongle                                         |
| alert, alert_mail, alert_* | It blinks red/white and may call **possible actions** above |
| off                        | It stops dongle (actually fades to black)                   |

#

### Pomodoro usage
Script using blink(1) dongle and will run pomodoro sessions
```
/usr/bin/python3 pomodoro.py --focus_duration=XX --small_break_duration=XX --bigger_break_duration=XX --bigger_break_duration=XX
```
(or use option `-h` to display the help info)

    Durations set from terminal are to be set in [minutes] for your convenience 

Arguments are optional, they are hard set within by default within `pomodoro.py`.
Hereunder are the constants to be modified if needed: 
    
    FOCUS_DURATION_IN_SECONDS = 1500  # 25 minutes
    SMALL_BREAK_DURATION_IN_SECONDS = 300  # 5 minutes
    BIGGER_BREAK_DURATION_IN_SECONDS = 1200  # 5 minutes
    MAX_POMO_BEFORE_BIG_BREAK = 3  # number of pomo to run before we have a (20 minutes) break


Bigger break calls a pattern called `nightfall` via `dongle.play_named('nightfall')` but you can call `dongle.off()` if you prefer...

