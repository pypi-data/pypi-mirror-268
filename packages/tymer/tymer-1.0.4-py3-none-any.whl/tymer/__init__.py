import time as t

class Timer:
    def __init__(self, seconds, countdown=False, integer=False):
        self.sec = seconds
        self.start_time = None
        self.run_timer = True
        self.timer = 0
        self.start_timer = True
        self.countdown = countdown
        self.integer = integer
    def start(self):
        if self.start_timer:
            self.start_time = t.time()
            self.start_timer = False
        self.current_time = t.time()
        if self.run_timer:
            if self.start_time != None:
                if not self.countdown:
                    if not self.integer:
                        self.timer = self.current_time - self.start_time
                    else:
                        self.timer = int(self.current_time - self.start_time)
                else:    
                    if not self.integer:
                        self.timer = self.sec - (self.current_time - self.start_time)
                    else:
                        self.timer = int(self.sec - (self.current_time - self.start_time))
        if not self.countdown:
            if self.timer >= self.sec:
                self.run_timer = False
                self.timer = self.sec
        else:
            if self.timer <= 0:
                self.run_timer = False
                self.timer = 0
    def stop(self):
        self.run_timer = False
        pass
    def restart(self,seconds='default'):
        self.new_time = seconds
        self.start_time = None
        self.run_timer = True
        if self.new_time != 'default':
            self.sec = self.new_time
        self.start_timer = True
        pass
    def time(self):
        return self.timer
        pass
    def __bool__(self):
        if not self.countdown:
            if self.timer != self.sec:
                return False
            else:
                return True
        else:
            if self.timer != 0:
                return False
            else:
                return True
    pass