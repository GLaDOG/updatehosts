import schedule
import time
import datetime
from autoupdatehosts import auto

def job():
    print "i'm working at ", datetime.datetime.now()

schedule.every().day.at("5:00").do(auto)
schedule.every().day.at("5:01").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)