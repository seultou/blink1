import sys
import os
import logging
import time
import re
from blink1.blink1 import Blink1
from smsapi.client import SmsApiPlClient
from config_info import Config, Info
from lib.color import Color
from lib.blink1_decorator import B1
from lib.action.api_request import ApiRequest
from lib.action.sms import SMS
from lib.guess_action import GuessAction
from lib.vo.status import Status



args = sys.argv[1:]
dongle = B1(Blink1())
if len(args) < 1:
    print('Status is missing!')
    dongle.off()
    dongle.close()
    exit(1)

status = sys.argv[1:][0]
reason = sys.argv[2:][0] if len(sys.argv[2:]) > 0 and len(sys.argv[2:][0].strip()) > 0 else 'no reason provided.'
logging.basicConfig(
    filename='status.log',
    level='INFO',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.info(f'Status >>> {status} | Reason >>> {reason}')
GuessAction(Status(status)).run()
if status == 'busy':
    dongle.fade(Color('RED'))
elif status == 'available' or status == 'ok':
    dongle.fade(Color('GREEN'))
elif re.search('^alert(_?)*', status):
    dongle.play_pattern(status)

    if Config.USE_OS_NOTIFICATIONS:
        os.system(Info.OS_NOTIFICATIONS_BIN_PATH + ' -u critical "Alert: ' +reason+ '"')

    if Config.USE_SMS:
        SMS(SmsApiPlClient(access_token=Info.SMS_API_TOKEN))\
            .send(to="+607080910", message=status + "! Reason: " + reason + "; datetime: " + time.asctime())

    if Config.USE_API_REQUEST:
        ApiRequest(Info.API_REQUEST_URL).post({"status":status,"reason":reason,"datetime":time.asctime()})
else:
    dongle.off()
dongle.close()
