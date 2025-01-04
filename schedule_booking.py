import schedule
import time
import padel_booker
from datetime import datetime, timedelta





def job(t):
    # print "I'm working...", t
    print('running')
    padel_booker.booker()
    return

schedule.every().day.at("22:15").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute    