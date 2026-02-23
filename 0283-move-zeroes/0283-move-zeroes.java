class Solution {
    public void moveZeroes(int[] arr) {
        int left = 0;

        for (int i = 0; i< arr.length; i++){
            if (arr[i] == 0){
                left = i;
                break;
            }
        }

        int i = left, right = left;
        while ( i < arr.length){
            if (arr[i] == 0){
                right++;
            }
            else{
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left ++; right ++; 
            }
            i++;
        }
    }
}