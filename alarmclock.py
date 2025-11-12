class AlarmClock:
    def __init__(self):
        self.current_time = 1000
        self.positon = 'Off'
        self.alarm_time = 1100
        print(f'Time is set to {self.current_time}')

    def set_current_time(self):
        self.current_time = input('Enter the current time:')
        print(f'Current time is {self.current_time}')

    def set_alarm_time(self):
        self.alarm_time = input('Enter an alarm time:')
        print(f'Alarm will sound at {self.alarm_time}')
    
    
    def toggle_alarm(self):
        if self.current_time == self.alarm_time:
            self.positon = 'On'
            print('Alarm clock is on')
        else:
            print('Still off')
    