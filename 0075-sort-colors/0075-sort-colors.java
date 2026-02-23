class Solution {
    public void sortColors(int[] arr) {
        int i = 0, low = 0, high = arr.length - 1;

        while (i <= high){
            if (arr[i] == 0){
                int temp = arr[low];
                arr[low] = arr[i];
                arr[i] = temp;
                low++; i++;
            }
            else if (arr[i]==2){
                int temp = arr[high];
                arr[high] = arr[i];
                arr[i] = temp;
                high--;
            }
            else{
                i++;
            }
        }
    }
}