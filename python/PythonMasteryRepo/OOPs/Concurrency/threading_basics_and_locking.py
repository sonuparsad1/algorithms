"""
Title: Threading Basics and Locking
Topic: Concurrency

Theory:
    Threads share the same memory space. Ideal for I/O bound tasks.
    
    GIL (Global Interpreter Lock): 
    Python threads cannot run CPU-bound bytecodes in parallel (mostly).
    Only one thread executes Python bytecode at a time.
    
    Race Conditions:
    Must use Locks (`threading.Lock`) when modifying shared state.
"""

import threading
import time

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            # Critical Section
            local = self.balance
            time.sleep(0.001) # Force context switch risk
            self.balance = local + amount

def worker(account):
    for _ in range(100):
        account.deposit(1)

def run_tests():
    acc = BankAccount()
    threads = []
    
    # Create 10 threads
    for _ in range(10):
        t = threading.Thread(target=worker, args=(acc,))
        threads.append(t)
        t.start()
    
    # Wait for all
    for t in threads:
        t.join()
        
    print(f"Final Balance: {acc.balance}")
    # Should be 10 * 100 = 1000
    assert acc.balance == 1000
    
    print("[PASS] Threading and Locking")

if __name__ == "__main__":
    run_tests()
