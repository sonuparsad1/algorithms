"""
Title: Multiprocessing vs Threading
Topic: Parallel and Concurrent Algorithms

Theory:
    Key Differences:
    - Threading: Shared memory, lower overhead, limited by GIL (CPU bound), good for I/O.
    - Multiprocessing: Separate memory, higher overhead, bypasses GIL, good for CPU bound.
"""

import time
import threading
import multiprocessing

def cpu_bound(n):
    while n > 0:
        n -= 1

def run_comparison():
    COUNT = 10000000
    
    # Serial
    start = time.time()
    cpu_bound(COUNT)
    cpu_bound(COUNT)
    print(f"Serial time: {time.time() - start:.4f}")
    
    # Threading (Won't improve speed much due to GIL)
    start = time.time()
    t1 = threading.Thread(target=cpu_bound, args=(COUNT,))
    t2 = threading.Thread(target=cpu_bound, args=(COUNT,))
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"Threading time: {time.time() - start:.4f} (Often similar to serial)")
    
    # Multiprocessing (Should be faster ~2x ideally)
    if __name__ == "__main__": 
        # Only run MP logic if main
        start = time.time()
        p1 = multiprocessing.Process(target=cpu_bound, args=(COUNT,))
        p2 = multiprocessing.Process(target=cpu_bound, args=(COUNT,))
        p1.start(); p2.start()
        p1.join(); p2.join()
        print(f"Multiprocessing time: {time.time() - start:.4f} (Better)")

if __name__ == "__main__":
    # Note: MP requires if __name__ == "__main__"
    run_comparison()
