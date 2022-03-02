from signal import alarm


class Alarm_clock:

    def __init__(self):
        self.current_time='12:00'
        self.alarm_is_on=True
        self.alarm_time='6:00'
    
    def change_time(self, current_time):
        self.current_time += current_time

    def set_alarm(self, alarm_time):
        self.alarm_time == alarm_time
        
    def silence_alarm(self, alarm_is_on):
        self.alarm_is_on