import time
import sched
from datetime import datetime
from ppadb.client import Client as AdbClient
import subprocess

button = '532 2166'  # x y 1080/4095 2285/4095
count = 0
adb = subprocess.Popen(args=['adb.exe', 'start-server'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, shell=True)

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
    global count
    count += 1
    device.shell(f'input tap {button}')
    print('tap ' + str(count))
    if count == 49:
        print('축하드려요!!')
        adb.terminate()


if __name__ == '__main__':
    device, client = connect()

s = sched.scheduler(time.time, time.sleep)

print('오늘은 '+ datetime.strftime(datetime.now(), '%Y년 %m월 %d일이에요'))
print('좋은 아침입니다!! 뱅크샐러드 유전자 검사 페이지를 켜두고 대기하세요')

month = datetime.now().month
day = datetime.now().day

for i in range(49):
    s.enterabs(datetime(2022, month, day, 2, 12, 20, 30 * i).timestamp(), 1, job)

s.run()
