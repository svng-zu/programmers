class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int n = s.length();
        int sum = 0;
        for(int i=0;i<n;i++){        
            if(sum >= 0 ){
                if(s.charAt(i) == '('){
                    sum += 1;
                }else if(s.charAt(i) == ')'){
                    sum -= 1;
                }
             answer = false;
            }
        }
        if(sum == 0){
            answer = true;  // ())(() 반례 확인 필요
        }
        else if(sum > 0 || sum < 0){
            answer = false;
        }
        
        return answer;
    }
}