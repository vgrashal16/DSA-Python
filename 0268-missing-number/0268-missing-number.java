class Solution {
    public int missingNumber(int[] arr) {
        int current_sum = 0;
        int n = arr.length;
        for (int i = 0; i< arr.length; i++){
            current_sum += arr[i];
        }

        int actual_sum = (n * (n + 1)/2);
        
        return actual_sum-current_sum;
    }
}