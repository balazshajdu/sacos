import datetime
#import time
import tkinter
#from concurrent.futures import ThreadPoolExecutor

#datetime
current_date_time_refresh_rate = 100
def display_date_time():
    current_date_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    current_date_time_label['text'] = current_date_time
    current_date_time_label.pack()
    root.after(current_date_time_refresh_rate, display_date_time)

#tkinter setup
root = tkinter.Tk()
root.title("Space Asset Communication System")
root.geometry("800x600")
root.config(bg="#26242f")
current_date_time_label = tkinter.Label(root)

display_date_time()

root.mainloop()


#userInput = input()


#
#def worker():
#    print("Hi {input}!")
#
#def displayTime():
#    while(1):
#        CurrentDateTime = datetime.datetime.now()
#        print(CurrentDateTime)
#        time.sleep(1)
#
# Create a thread pool with 2 workers
#with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit two tasks to run in parallel
#    executor.submit(displayTime)
#    executor.submit(worker)



#print("Hello Wide World!")