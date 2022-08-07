import argparse
import signal
import os
import time
import threading
from blink1.blink1 import Blink1
from lib.blink1_decorator import B1
from lib.color import Color

FOCUS_DURATION_IN_SECONDS = 1500  # 25 minutes
SMALL_BREAK_DURATION_IN_SECONDS = 300  # 5 minutes
BIGGER_BREAK_DURATION_IN_SECONDS = 1200  # 5 minutes
NUMBER_OF_SESSIONS_BEFORE_BIGGER_BREAK = 3  # number of sessions to run before next break is the bigger one
dongle = B1(Blink1())


class LiveInfo:
    done = 0
    start_time = 0
    last_focus_datetime = 0
    last_any_break_datetime = 0
    now_type = 'FOCUS'


class Setup:
    __focus_duration_in_seconds = 0
    __small_break_duration_in_seconds = 0
    __bigger_break_duration_in_seconds = 0

    def __init__(self,
                 focus_duration: int = FOCUS_DURATION_IN_SECONDS,
                 small_break_duration: int = SMALL_BREAK_DURATION_IN_SECONDS,
                 bigger_break_duration: int = BIGGER_BREAK_DURATION_IN_SECONDS):
        self.focus_duration = focus_duration
        self.__small_break_duration_in_seconds = small_break_duration
        self.__bigger_break_duration_in_seconds = bigger_break_duration

    def get_focus_duration(self) -> int:
        return self.__focus_duration_in_seconds if self.__focus_duration_in_seconds > 0 else FOCUS_DURATION_IN_SECONDS

    def get_small_break_duration(self) -> int:
        return self.__small_break_duration_in_seconds if self.__small_break_duration_in_seconds > 0 else SMALL_BREAK_DURATION_IN_SECONDS

    def get_bigger_break_duration(self) -> int:
        return self.__bigger_break_duration_in_seconds if self.__bigger_break_duration_in_seconds > 0 else BIGGER_BREAK_DURATION_IN_SECONDS


def sigint_handler(signal, frame):
    dongle.off()
    exit(1)


def timer() -> int:
    return int(time.strftime('%Y%m%d%H%M%S'))


def notify(mask: str, *args):
    msg = mask.format(*args)
    # Uncomment if you want to show a notif on your destop from [notify-send]
    # os.system('notify-send -u normal "' + msg + '"')
    print(msg)


def focus():
    LiveInfo.now_type = 'FOCUS'
    notify("Time to focus!")
    LiveInfo.last_any_break_datetime = timer()
    dongle.fade(Color('RED').speed())


def small_break():
    LiveInfo.done += 1
    notify('Time for a small break! ({} minutes)', setup.get_small_break_duration())
    LiveInfo.last_focus_datetime = timer()
    LiveInfo.now_type = 'SMALL_BREAK'
    dongle.fade(Color('GREEN').speed())


def bigger_break():
    LiveInfo.done += 1
    notify('Time for a bigger break: {} minutes (pomo done: {})', setup.get_bigger_break_duration(), LiveInfo.done)
    LiveInfo.last_focus_datetime = timer()
    LiveInfo.now_type = 'BIGGER_BREAK'
    dongle.play_named('nightfall')


def check() -> None:
    if LiveInfo.now_type == 'FOCUS':
        if timer() >= LiveInfo.last_any_break_datetime + setup.get_focus_duration():
            if LiveInfo.done > 0 and int(LiveInfo.done) % int(NUMBER_OF_SESSIONS_BEFORE_BIGGER_BREAK) == 0:
                bigger_break()
                return
            small_break()
            return

    if LiveInfo.now_type == 'SMALL_BREAK':
        if timer() >= LiveInfo.last_focus_datetime + setup.get_small_break_duration():
            focus()
            return

    if LiveInfo.now_type == 'BIGGER_BREAK':
        if timer() >= LiveInfo.last_focus_datetime + setup.get_bigger_break_duration():
            focus()
            return


def start():
    threading.Timer(1, start).start()
    check()


signal.signal(signal.SIGINT, sigint_handler)

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--focus_duration', type=int, default=FOCUS_DURATION_IN_SECONDS, help='Focus duration in minutes')
parser.add_argument('--small_break_duration', default=SMALL_BREAK_DURATION_IN_SECONDS, help='Small breaks duration in minutes')
parser.add_argument('--bigger_break_duration',
                    default=BIGGER_BREAK_DURATION_IN_SECONDS,
                    help='Bigger breaks duration in minutes (the one that happens every N pomo sessions)', )
parser.add_argument('--max_pomo_before_big_break',
                    default=NUMBER_OF_SESSIONS_BEFORE_BIGGER_BREAK,
                    help='How many pomo sessions before next is the bigger break?'
                         ' (the one that happens every N pomo sessions)')

args = parser.parse_args()
setup = Setup(int(args.focus_duration) * 60, int(args.small_break_duration) * 60, int(args.bigger_break_duration) * 60)

LiveInfo.last_any_break_datetime = LiveInfo.start_datetime = timer()
focus()

start()
