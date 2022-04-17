import time
import sched
from datetime import datetime
from ppadb.client import Client as AdbClient

button = '532 2166'  # x y 1080/4095 2285/4095


def connect():
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client


def job():
    device.shell(f'input tap {button}')
    print('tap')


if __name__ == '__main__':
    device, client = connect()

s = sched.scheduler(time.time, time.sleep)
date = int(input('오늘 날짜를 입력하세요:\n'))
for i in range(49):
    # s.enterabs(datetime(2022, 4, 17, 9, 59, 59, 999750 + 50 * (i)).timestamp(), 1, job)
    s.enterabs(datetime(2022, 4, date, 10, 0, 0, 50 * i).timestamp(), 1, job)

s.run()
