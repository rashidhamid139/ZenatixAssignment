import copy
from threading import Timer
from edgeprogram import send_data_to_server, send_buffered_data

class Timer60Seconds(object):
    BUFFER_DATA = []
    SUCCESS_POSTED = 0
    TOTAL_POSTED = 0

    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()
        self.generator = self.csv_reader(*self.args)

    def _run(self):
        self.TOTAL_POSTED += 1
        self.is_running = False
        self.start()
        self.args = next(self.generator), 
        response = self.function(*self.args, **self.kwargs)
        print("Server Response: ", response)
        if response == "SUCCESS":
            self.SUCCESS_POSTED += 1
        else:
            self.BUFFER_DATA.append(self.args[0])
        print("Inside 60 seconds Timer: ", Timer60Seconds.BUFFER_DATA)
        msg = "Total Posted values: {0},    Success Posted values: {1} Buffered Data: {2}".format(self.TOTAL_POSTED, self.SUCCESS_POSTED, self.BUFFER_DATA)
        print(msg)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run )
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

    def csv_reader(self, file):
        for row in open(file, "r"):
            row = row.split(',')[1]
            yield row

class Timer5Seconds(object):
    def __init__(self, function, *args, **kwargs):
        self._timer     = None
        self.interval   = 5
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()

        print("Inside 5 seconds Timer: ", Timer60Seconds.BUFFER_DATA)
        buffer_data = copy.deepcopy(Timer60Seconds.BUFFER_DATA)
        Timer60Seconds.BUFFER_DATA = []
        response = self.function(buffer_data, **self.kwargs)
        print("Response of Buffer data: ", response)
        Timer60Seconds.SUCCESS_POSTED += len(buffer_data) - len(response)
        if isinstance(response, list):
            Timer60Seconds.BUFFER_DATA.extend(response)



    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

from time import sleep

print("starting...")
timer = Timer5Seconds( send_buffered_data, Timer60Seconds.BUFFER_DATA) # it auto-starts, no need of rt.start()
rt = Timer60Seconds(60, send_data_to_server, "dataset.csv")
try:
    while True:
        # sleep # your long-running job goes here...
        pass
finally:
    rt.stop()
    timer.stop()