import java.util.Arrays;
class Solution {
    public int[] solution(int[] arr) {
    int[] answer = {};
    if(arr.length==1){
        answer = new int[1];
        answer[0] = -1;
    }else{
        answer = new int[arr.length-1];
        int min = arr[0];
            
        for(int i=0; i<arr.length; i++){
            min = Math.min(min, arr[i]);
        }
        int index = 0;
        for(int i=0; i<arr.length; i++){
            if(min == arr[i]){
                continue; // 특정 인덱스의 값을 넣지 않는 방법
            }
            answer[index] = arr[i];
            index++; // for 문 하나로, 두 인덱스값이 다른 배열 처리
            }
        }
        return answer;
    }
}