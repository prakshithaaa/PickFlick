import random
from datetime import datetime, timedelta

def gen_otp(ttl=60):
    otp= random.randint(0,999999)
    otp_time= datetime.now()
    exp_time= datetime.now + timedelta(seconds=ttl)
    return otp, exp_time

def time_left(expiry_time):
    remain= 

def verify_otp(correct_otp, exp_time):
    print("OTP sent:", correct_otp)

    while True:
        remain= time_left(exp_time)


otp, exp_time = gen_otp()
verify_otp(otp, exp_time)