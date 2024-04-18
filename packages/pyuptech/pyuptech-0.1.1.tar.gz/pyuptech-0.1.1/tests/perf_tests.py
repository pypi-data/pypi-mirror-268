import unittest
from time import sleep, perf_counter_ns


class PerfTestCase(unittest.TestCase):

    def sample_freq_test(self, func):
        """Test the performance and frequency of the provided function.

        Args:
            func (Callable): The function to be tested.
        """
        res = []
        ms = 10000  # Assuming you want to measure for 10 seconds
        sleep(5)  # Allow some warm-up time before starting measurement
        end = perf_counter_ns() + ms * 1000000
        while perf_counter_ns() < end:
            res.append(tuple(list(func())))

        deduped_res = set(res)
        print(f"Result list length: {len(res)}")
        print(f"Average interval (including duplicates): {ms / len(res)}ms")
        print(f"Deduplicated result count: {len(deduped_res)}")
        print(f"Average actual interval: {ms / len(deduped_res)}ms")

    def test_function_performance(self):
        # Replace this with your actual function
        def dummy_func():
            return [1, 2, 3]

        self.sample_freq_test(dummy_func)


if __name__ == "__main__":
    unittest.main()
