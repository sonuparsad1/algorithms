"""
Title: Behavioral Patterns (Observer, Strategy, Command, State)
Topic: Design Patterns

Theory:
    Focus on communication between objects.
    
    1. Observer: One-to-many dependency. Notifies dependents of state change.
    2. Strategy: Encapsulate algorithms and make them interchangeable.
    3. Command: Encapsulate a request as an object.
    4. State: Allow object to alter behavior when internal state changes.
"""

from abc import ABC, abstractmethod

# ==========================================
# 1. Observer
# ==========================================

class Observer:
    def update(self, msg): pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, obs):
        self._observers.append(obs)
    
    def notify(self, msg):
        for o in self._observers:
            o.update(msg)

class LogObserver(Observer):
    def __init__(self):
        self.log = []
    def update(self, msg):
        self.log.append(msg)

# ==========================================
# 2. Strategy
# ==========================================

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data): pass

class QuickSort(SortStrategy):
    def sort(self, data): return sorted(data) # Pseudo

class ReverseSort(SortStrategy):
    def sort(self, data): return sorted(data, reverse=True)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data)

# ==========================================
# 3. State
# ==========================================

class State(ABC):
    @abstractmethod
    def handle(self): pass

class RedLight(State):
    def handle(self): return "STOP"

class GreenLight(State):
    def handle(self): return "GO"

class TrafficLight:
    def __init__(self):
        self.state = RedLight()
    
    def change(self):
        if isinstance(self.state, RedLight):
            self.state = GreenLight()
        else:
            self.state = RedLight()
    
    def signal(self):
        return self.state.handle()

def run_tests():
    # Observer
    sub = Subject()
    obs = LogObserver()
    sub.attach(obs)
    sub.notify("Event 1")
    assert obs.log == ["Event 1"]
    
    # Strategy
    s = Sorter(ReverseSort())
    assert s.sort_data([1,2,3]) == [3,2,1]
    
    # State
    t = TrafficLight()
    assert t.signal() == "STOP"
    t.change()
    assert t.signal() == "GO"
    
    print("[PASS] Behavioral Patterns")

if __name__ == "__main__":
    run_tests()
