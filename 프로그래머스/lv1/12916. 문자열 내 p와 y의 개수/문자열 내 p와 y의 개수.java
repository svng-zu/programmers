class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        int n = s.length();
        char c = 0;
    
        for(int i=0; i<n; i++){
            c = s.charAt(i);
            if(c == 'p' || c == 'P'){
                p += 1;
                
            }else if(c == 'y' || c == 'Y'){
                y += 1;
            
            }
        }    
        
        if(p == y) {
            answer = true;
        }
        else{
            answer = false;
        }
        

        return answer;
    }
}
