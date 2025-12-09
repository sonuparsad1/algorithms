"""
Title: Tower of Hanoi
Topic: Algorithms Basics

Theory:
    Classic puzzle. Move n disks from Source to Destination using Auxiliary rod.
    Rules:
    1. Only one disk at a time.
    2. No larger disk on top of smaller disk.
    
    Complexity: O(2^n).
"""

def tower_of_hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, target, moves)
    moves.append(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source, moves)

def run_tests():
    moves = []
    tower_of_hanoi(3, 'A', 'C', 'B', moves)
    """
    Expected for 3:
    1 A->C
    2 A->B
    1 C->B
    3 A->C
    1 B->A
    2 B->C
    1 A->C
    """
    assert len(moves) == 7 # 2^3 - 1
    assert moves[0] == "Move disk 1 from A to C"
    assert moves[-1] == "Move disk 1 from A to C" # Actually depends on sequence, but disk 1 does land C last? 
    # Logic: Last move is disk 1 from A to C? No. The biggest disk moves A->C in middle.
    
    print(f"Total moves for 3 disks: {len(moves)}")
    print("[PASS] Tower of Hanoi")

if __name__ == "__main__":
    run_tests()
