import time
import datetime
import pygame

# Set Alarm Function
def set_alarm(alarm_time):
    print(f"Alarm Set For {alarm_time}")
    sound_file = "C:/Users/habra/Desktop/Code_Python/music.mp3"
    is_running = True
    
    # Initialize pygame mixer outside the loop to avoid repeated initialization
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    
    while is_running:
        # Get the current time in the same format as the alarm time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}, Alarm Time: {alarm_time}")  # Debugging line
        
        # Check if the current time matches the alarm time
        if current_time==alarm_time:
            print("Time to wake up!")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running=False
        time.sleep(1)

# Main Function
if __name__ == "__main__":
    alarm_time = input("Enter Time To set Alarm For (HH:MM:SS): ")
    set_alarm(alarm_time)

