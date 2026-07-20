class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = {};
        // creates an array of empty arrays
        const buckets = Array.from({ length: nums.length + 1}, () => []);

        // build the map of frequencies
        for (const num of nums) {
            freq[num] = (freq[num] || 0) + 1;
        }

        // put nums into buckets based on frequency
        for (const num in freq) {
            const count = freq[num];
            buckets[count].push(Number(num));
        }

        // iterate backward through buckets
        const result = [];
        for (let i = buckets.length - 1; i >= 0; i--) {
            if (buckets[i].length > 0) {
                result.push(...buckets[i]);
                if (result.length === k) {
                    return result;
                }
            }
        }


    }
}
