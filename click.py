import time
from datetime import datetime, timedelta
import pyautogui

TARGET_TIME = "01:00:00"   # HH:MM:SS
X = 1875
Y = 239

now = datetime.now()
target = datetime.strptime(TARGET_TIME, "%H:%M:%S").replace(
    year=now.year,
    month=now.month,
    day=now.day
)

# If target time already passed today, schedule for tomorrow
if target <= now:
    target += timedelta(days=1)

print(f"Waiting until {target}...")

while datetime.now() < target:
    time.sleep(0.2)

pyautogui.click(X, Y)
print("Click done.")