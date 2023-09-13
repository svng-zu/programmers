class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        int cnt = 0;
        for(int c = left; c <= right; c++){
            cnt = 0;
            for(int i =1; i<=c; i++){
                if(c % i == 0){
                    cnt ++;
                }
            }
            if(cnt % 2 == 0){
                answer += c;
        
            }else if(cnt % 2 == 1){
                answer -= c; 
            }            
        }
        return answer;
    }
}