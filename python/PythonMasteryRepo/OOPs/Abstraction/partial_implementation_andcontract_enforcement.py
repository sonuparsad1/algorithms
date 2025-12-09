"""
Title: Partial Implementation and Contract Enforcement
Topic: Abstraction

Theory:
    ABCs can provide partial implementation.
    This is known as the "Template Method Pattern" (not to be confused with C++ Templates).
    
    The Base class controls the algorithm structure, but delegates specific steps to subclasses.
"""

from abc import ABC, abstractmethod

class DataProcessor(ABC):
    
    def process_pipeline(self, data):
        """The Template Method: Defines the skeleton."""
        data = self.read_data(data)
        data = self.clean_data(data)
        result = self.analyze_data(data)
        self.save_result(result)
        return result

    @abstractmethod
    def read_data(self, source):
        pass

    def clean_data(self, data):
        """Hook method with default implementation."""
        print("Default cleaning (strip whitespace)")
        return data.strip() if isinstance(data, str) else data

    @abstractmethod
    def analyze_data(self, data):
        pass

    @abstractmethod
    def save_result(self, result):
        pass


class TextProcessor(DataProcessor):
    def read_data(self, source):
        return f"  {source}  "

    def analyze_data(self, data):
        return len(data)

    def save_result(self, result):
        print(f"Saved count: {result}")


def run_tests():
    p = TextProcessor()
    # flow: read("Raw") -> "  Raw  " -> clean -> "Raw" -> analyze -> 3 -> save
    res = p.process_pipeline("Raw")
    assert res == 3 # Length of "Raw"
    
    print("[PASS] Partial implementation / Template method")

if __name__ == "__main__":
    run_tests()
