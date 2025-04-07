function pivotIndex(nums) {
  let totalSum = nums.reduce(
    (accumulatedVal, currentVal) => accumulatedVal + currentVal,
    0
  );
  let leftSum = 0;

  for (let i = 0; i < nums.length; i++) {
    // Right sum = totalSum - leftSum - nums[i]
    if (leftSum === totalSum - leftSum - nums[i]) {
      return i; // Found pivot index
    }
    leftSum += nums[i]; // leftsum = leftsum + num[i];
  }

  return -1; // No pivot found
}

// Test Cases
console.log(pivotIndex([1, 7, 3, 6, 5, 6])); // Output: 3
console.log(pivotIndex([1, 2, 3])); // Output: -1
console.log(pivotIndex([2, 1, -1])); // Output: 0
