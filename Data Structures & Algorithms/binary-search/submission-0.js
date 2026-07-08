class Solution {
    search(nums, target) {
    let leftVal = 0;
    let rightVal = nums.length - 1;
    

    while (leftVal <= rightVal) {
        let midVal = Math.floor((leftVal + rightVal) / 2);
        if (nums[midVal] > target) {
            rightVal = midVal - 1;
        } else if (nums[midVal] < target) {
            leftVal = midVal + 1;
        } else {
            return midVal;
        }
    }
    return -1;
    }
}
