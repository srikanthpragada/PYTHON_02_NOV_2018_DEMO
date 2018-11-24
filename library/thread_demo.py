import threading
import time


class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            # time.sleep(1)   #wait for 1 second
            print(i)
        else:
            print("The end of child")


pt = PrintThread()
pt.start()

print("Active Thread count :", threading.active_count())
# print("Main Thread  :", threading.main_thread())

# Print all threads
for t in threading.enumerate():
    print(t)

print("The end of main")
