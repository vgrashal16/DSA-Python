class Solution {
    public static boolean Palindrome(String s){
        StringBuilder reversed = new StringBuilder();

        for (int i = s.length()-1; i >= 0; i--){
            reversed.append(s.charAt(i));
        }

        return (reversed.toString().equals(s));
    }

    public boolean isPalindrome(String s) {
        s = s.trim();
        s = s.replaceAll("[^A-Za-z0-9]", "");
        s = s.toLowerCase();
        return Palindrome(s);
    }
}