# MultiThreading  = is used to perform multiple tasks concurrently (Multi-Tasking) , its good for I/O bound Tasks like reading files or fetching data from  API's
import threading
import time


def walk_the_dog(first,last):
    time.sleep(8)  # Suppose 8 seconds taken for walk
    print(f"You completed the walk with {first} {last} ")

def take_out_trash():
    time.sleep(2)
    print("You Took Out Trash ")
    
def get_mail():
    time.sleep(4)
    print("You got the Mail from Mailbox")
    
    
chore1=threading.Thread(target=walk_the_dog,args=("Scooby","Doo"))
chore2=threading.Thread(target=take_out_trash)
chore3=threading.Thread(target=get_mail)


# Starts Threading 
chore1.start()
chore2.start()
chore3.start()

# Join to print soemthing after every thread executes
chore1.join()
chore2.join()
chore3.join()

print("All Chores are Completed ")