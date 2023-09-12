class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double sum = 0;
        int n = arr.length;
        for(int i=0; i<n; i++){
            sum += arr[i];
        }
        answer = sum/n;
        return answer;
    }
}