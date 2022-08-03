class Config:
    USE_API_REQUEST = True
    USE_OS_NOTIFICATIONS = True
    USE_SMS = True
    AVAILABLE_STATUS = [
        'available', 'ok',
        'busy',
        'alert', 'alert_mail',
        # ETC...
    ]


class Info:
    API_REQUEST_URL = 'https://blink1.local/status'
    OS_NOTIFICATIONS_BIN_PATH = '/usr/bin/notify-send'
    SMS_API_TOKEN = 'XXXX'
