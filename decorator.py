import time


class Stopwatch:
    avg_time = 0

    def __init__(self, num_runs=1):
        self.num_runs = num_runs

    def __call__(self, func):
        def decorated(*args):
            for i in range(self.num_runs):
                start_time = time.time()
                res = func(*args)
                self.avg_time += time.time() - start_time
            print(f"Cреднее время выполнение при {self.num_runs} итерациях: {round(self.calc_avg_time(), 2)} секунд")
            return res

        return decorated

    def calc_avg_time(self):
        self.avg_time /= self.num_runs
        return self.avg_time


class StopwatchTwo(Stopwatch):
    def __str__(self, func):
        def decorated(*args):
            for i in range(self.num_runs):
                start_time = time.time()
                res = func(*args)
                self.avg_time += time.time() - start_time
            print(f"Cреднее время выполнение при {self.num_runs} итерациях: {round(self.calc_avg_time(), 2)} секунд")
            return res

        return decorated
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self