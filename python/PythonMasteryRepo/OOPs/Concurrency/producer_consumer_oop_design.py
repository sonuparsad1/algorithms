"""
Title: Producer-Consumer OOP Design
Topic: Concurrency

Theory:
    Classic pattern to decouple data production from processing.
    Key Component: A thread-safe queue.
    
    Producer -> Queue -> Consumer.
    
    Uses `queue.Queue` (Thread-safe).
"""

import threading
import queue
import time
import random

class System:
    def __init__(self):
        self.queue = queue.Queue(maxsize=5)
        self.sentinel = object() # Marker to stop consumers

class Producer(threading.Thread):
    def __init__(self, system):
        super().__init__()
        self.system = system

    def run(self):
        for i in range(5):
            item = f"Item-{i}"
            print(f"Producing {item}")
            self.system.queue.put(item) # Blocks if full
            time.sleep(random.random() * 0.01)
        
        print("Producer finished")
        self.system.queue.put(self.system.sentinel)

class Consumer(threading.Thread):
    def __init__(self, system):
        super().__init__()
        self.system = system
        self.consumed = []

    def run(self):
        while True:
            item = self.system.queue.get() # Blocks if empty
            if item is self.system.sentinel:
                self.system.queue.put(item) # Putting back for other consumers (if multiple)
                break
            
            print(f"Consuming {item}")
            self.consumed.append(item)
            self.system.queue.task_done()
            time.sleep(random.random() * 0.01)

def run_tests():
    sys = System()
    p = Producer(sys)
    c = Consumer(sys)
    
    p.start()
    c.start()
    
    p.join()
    c.join()
    
    assert len(c.consumed) == 5
    print("[PASS] Producer-Consumer Pattern")

if __name__ == "__main__":
    run_tests()
