class Solution {
    hasDuplicate(nums) {
        const newSet = new Set(nums);
        return newSet.size !== nums.length;
    }
}
