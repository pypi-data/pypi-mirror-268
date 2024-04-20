import datetime

class Clock():
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = datetime.datetime.now()

    def end(self):
        self.end_time = datetime.datetime.now()
        self.delta_t = self.end_time - self.start_time
    
    def show(self):
        print('The program runs for ',self.delta_t,' microsecond')

