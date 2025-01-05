import schedule
import time
import padel_booker
from datetime import datetime, timedelta


def job(t):

    print('running')
    padel_booker.booker()
    return

schedule.every().thursday.at("00:01").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) 