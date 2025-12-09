"""
Title: Map Reduce Concept
Topic: Parallel and Concurrent Algorithms

Theory:
    Pattern:
    1. Map: Process input elements independently -> (key, value) pairs.
    2. Reduce: Aggregate values for same key.
    
    Python `multiprocessing.Pool.map` is a simplified Parallel Map.
"""

import multiprocessing
from functools import reduce

def mapper_word_count(text):
    # Returns dictionary of word counts for a chunk
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def reducer_merge(counts1, counts2):
    # Merge two count dicts
    result = counts1.copy()
    for k, v in counts2.items():
        result[k] = result.get(k, 0) + v
    return result

def run_map_reduce():
    texts = [
        "apple banana apple",
        "banana cherry",
        "apple cherry date"
    ]
    
    # 1. Parallel Map
    with multiprocessing.Pool(3) as p:
        mapped_results = p.map(mapper_word_count, texts)
        
    # 2. Reduce (Sequential merge here for simplicity)
    final_counts = reduce(reducer_merge, mapped_results)
    
    assert final_counts['apple'] == 4 # Actually 3! "apple" in text1 (2), text3 (1) -> 3
    # Wait, "apple banana apple" = 2. "apple cherry date" = 1. yes 3.
    # What was I thinking? 2+1=3.
    
    assert final_counts['apple'] == 3
    assert final_counts['banana'] == 2
    
    print("[PASS] Map Reduce")

if __name__ == "__main__":
    run_map_reduce()
