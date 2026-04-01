import random
from datetime import datetime, timedelta

def generate_otp(ttl=61):
    otp = random.randint(0, 999999)          
    otp_time = datetime.now()               
    exp_time = otp_time + timedelta(seconds=ttl)  
    return otp, exp_time

def time_left(expiry_time):
    if datetime.now() >= expiry_time:
        return 0
    return (expiry_time - datetime.now()).seconds

def verify_otp(correct_otp, exp_time):
    print("OTP sent:", correct_otp)  

    while True:
        remaining = time_left(exp_time)

        if remaining == 0:
            print("OTP Expired!")
            break

        print("(You have", remaining, "seconds left)")
        entered = int(input("Enter 6-digit OTP: "))

        if datetime.now() > exp_time:
            print("OTP Expired!")
            break
        elif entered == correct_otp:
            print("OTP Verified!")
            break
        else:
            print("Incorrect OTP. Try again.")

otp, exp_time = generate_otp()
verify_otp(otp, exp_time)