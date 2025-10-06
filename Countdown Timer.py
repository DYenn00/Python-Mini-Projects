import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

print("Countdown Timer Started!")
countdown(15)
print(" Ding! Ding! It's time for a break!")
countdown(5)
print("Back to work!")
