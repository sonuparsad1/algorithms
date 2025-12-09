"""
Title: Multiprocessing Basics
Topic: Concurrency

Theory:
    Processes have separate memory spaces. Ideal for CPU bound tasks.
    They bypass the GIL.
    
    Communication:
    Use `Queue` or `Pipe` to share data between processes (Pickle-based).
"""

import multiprocessing
import time

def cpu_bound_task(n):
    return sum(i * i for i in range(n))

class WorkerProcess(multiprocessing.Process):
    def __init__(self, n, queue):
        super().__init__()
        self.n = n
        self.queue = queue

    def run(self):
        """Method called when p.start() runs."""
        res = cpu_bound_task(self.n)
        self.queue.put(res)

def run_tests():
    # Only run multiprocessing in main block on Windows!
    queue = multiprocessing.Queue()
    
    p = WorkerProcess(1000, queue)
    p.start()
    p.join()
    
    result = queue.get()
    assert result > 0
    print(f"Result from process: {result}")
    
    print("[PASS] Multiprocessing")

if __name__ == "__main__":
    # Essential for Windows
    run_tests()
