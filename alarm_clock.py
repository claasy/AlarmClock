class Alarm_Clock:
    def __init__(self):
        self.current_time='12:00'
        self.alarm_time='6:00'
        self.alarm_is_off=True
    
    def change_time(self, new_time):
        self.current_time = new_time
        print(self.current_time)
    def set_alarm(self, alarm_time):
        self.alarm_time = alarm_time
        print(self.alarm_time)  
    def toggle_alarm(self):
        if self.alarm_is_off==True:
            self.alarm_is_off=False
        else:
            self.alarm_is_off=True