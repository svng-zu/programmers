class Solution {
    public long solution(int price, int money, int count) {
        long answer = -1;
        long sum = 0;
        for(int i=1; i<= count; i++){
            sum += i;
        }
        if(money >= sum*price){
            answer = 0;
        }else if(money < sum*price){
            answer = sum*price - money;
        }

        return answer;
    }
}