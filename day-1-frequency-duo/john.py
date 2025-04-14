def main(nums):
  """
  This function takes a list of integers nums and returns a list of two integers based on the following conditions:
    - If there is one unique number occurring an even number of times, it returns that number twice.
    - If two distinct numbers occur the same number of times (and at least twice), it returns those two numbers.
    - Otherwise, it returns [1, -1].
Parameters:
   - nums (list): A list of integers.
Returns:
   - A list containing two integers based on the conditions above.
"""
    num_counts = {}

    # Count the frequency of each number in the num list
    for num in nums:
        if num not in num_counts:
            num_counts[num] = 1
        else:
            num_counts[num] += 1

    # Extract the keys (unique numbers) from the num_counts dictionary
    keys = list(num_counts.keys())

    # If there's exactly one number and it occurs an even number of times
    if len(keys) == 1 and num_counts[keys[0]] % 2 == 0:
        return [keys[0], keys[0]]

    # Otherwise, find two numbers with the same frequency (and frequency >= 2)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if num_counts[keys[i]] == num_counts[keys[j]] and num_counts[keys[i]] >= 2:
                return [keys[i], keys[j]]

    # If no valid pair is found, return [1, -1]
    return [1, -1]
