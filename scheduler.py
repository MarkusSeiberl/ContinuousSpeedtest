import schedule
import speedtest
import time

def job_speedtest():
    speedtest.startSpeedTest()

schedule.every().hour.do(job_speedtest)

while True:
    schedule.run_pending()
    time.sleep(1)