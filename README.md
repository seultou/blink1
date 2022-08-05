# blink1
Script using blink(1) dongle and can make some actions regarding a given status

### Usage
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


