"""
Title: Async/Await OOP Patterns
Topic: Concurrency

Theory:
    `asyncio` allows writing single-threaded concurrent code using coroutines.
    Classes can have `async` methods.
    
    `__aiter__` and `__anext__`: Async Iterators.
    `__aenter__` and `__aexit__`: Async Context Managers.

    Pitfall: Blocking the event loop (e.g., using `time.sleep` instead of `asyncio.sleep`).
"""

import asyncio

class AsyncFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    async def fetch(self, endpoint):
        """Simulate Network Request"""
        print(f"Fetching {endpoint}...")
        await asyncio.sleep(0.1) # Non-blocking sleep
        return f"Data from {endpoint}"

    async def fetch_all(self, endpoints):
        # Gather multiple tasks concurrently
        tasks = [self.fetch(ep) for ep in endpoints]
        return await asyncio.gather(*tasks)

class AsyncResource:
    async def __aenter__(self):
        print("Async acquiring...")
        await asyncio.sleep(0.01)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Async releasing...")
        await asyncio.sleep(0.01)

def run_tests():
    async def main():
        # 1. Async Methods
        f = AsyncFetcher("http://api.com")
        results = await f.fetch_all(["/users", "/posts", "/comments"])
        assert len(results) == 3
        print("Fetch results:", results)

        # 2. Async Context Manager
        async with AsyncResource() as res:
            print("Inside async context")

    # Run the event loop
    asyncio.run(main()) 
    print("[PASS] Async OOP Patterns")

if __name__ == "__main__":
    run_tests()
