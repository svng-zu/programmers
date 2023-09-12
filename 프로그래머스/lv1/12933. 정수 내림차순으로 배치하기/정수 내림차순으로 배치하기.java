import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        int a = 0;
        int length = ((int) Math.log10(n)+1);
        int[] arr= {};
        arr = new int[length];
        
        for(int i=0; i<length; i++){
            a = (int)(n%10);
            n/=10;
            arr[i] = a;
        }
        Integer[] arr1 = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(arr1, Collections.reverseOrder());
        for(int i=0; i<length; i++){
            answer += Math.pow(10, (length-1-i)) * arr1[i];
        }
        //Math.pow(밑, 지수)
        return answer;
    }
}