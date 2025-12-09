"""
Title: Concurrent Futures (ThreadPool & ProcessPool)
Topic: Concurrency

Theory:
    High-level API for async execution (`concurrent.futures`).
    - `ThreadPoolExecutor`: For threads.
    - `ProcessPoolExecutor`: For processes.
    
    Pattern:
    `future = executor.submit(func, args)`
    `result = future.result()`
"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def square(n):
    return n * n

def run_tests():
    # 1. Thread Pool
    print("--- Thread Pool ---")
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square, [1, 2, 3]))
        assert results == [1, 4, 9]

    # 2. Process Pool
    print("--- Process Pool ---")
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(square, n): n for n in [4, 5, 6]}
        
        for future in as_completed(futures):
            res = future.result()
            print(f"Result: {res}")
            assert res in [16, 25, 36]
    
    print("[PASS] Concurrent Futures")

if __name__ == "__main__":
    run_tests()
