from pyrh import Robinhood
from dotenv import load_dotenv
import os, time, SendEmail
from timeloop import Timeloop
from datetime import timedelta

load_dotenv()

tl = Timeloop()
rh = Robinhood()
rh.login(username=os.getenv('ROBINHOOD_USERNAME'), password=os.getenv('ROBINHOOD_PASSWORD'), challenge_type='sms')


@tl.job(interval=timedelta(seconds=45))
def sendEmailAboutNews():
    t = time.localtime()

    if t.tm_hour == 15 and t.tm_min == 30:
        SendEmail.sendEmail(rh.adjusted_equity_previous_close(), rh.equity())


if __name__ == "__main__":
    tl.start(block=True)
