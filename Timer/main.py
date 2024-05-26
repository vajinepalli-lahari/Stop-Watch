import time
class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = None
        self.paused = False
        self.paused_time = 0
    
    def start(self):
        self.start_time = time.time()
        while True:
            if self.paused:
                time.sleep(1)
                continue
            elapsed_time = time.time() - self.start_time - self.paused_time
            remaining_time = max(self.duration - elapsed_time, 0)
            minutes, seconds = divmod(int(remaining_time), 60)
            print(f"Time Remaining: {minutes:02d}:{seconds:02d}", end='\r')
            if remaining_time == 0:
                break
            time.sleep(1)
    
    def pause(self):
        if self.paused:
            return
        self.paused = True
        self.pause_start_time = time.time()
    
    def resume(self):
        if not self.paused:
            return
        self.paused = False
        self.paused_time += time.time() - self.pause_start_time
    
    def reset(self):
        self.start_time = None
        self.paused = False
        self.paused_time = 0
duration = 10
timer = CountdownTimer(duration)
timer.start()