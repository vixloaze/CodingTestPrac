package programmers;
/*
문제 주소 : https://school.programmers.co.kr/learn/courses/30/lessons/82612

문제 접근 방법 & 사용 알고리즘:
    1. 반복문 통해서 놀이기구 탈 때마다 총 요금(sum)에 더한다.
    2. 총 요금이 가지고 있는 돈보다 클 경우(돈이 부족한 경우)
    -> sum에서 가지고 있는 돈 빼고 그것을 return 한다.
*/
public class Mian {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long sum = 0;

        for(int i=1; i<=count; i++){
            sum = sum + price*i;
        }

        if(sum>money){
            answer = sum - money;
            return answer;
        }
        else{
            return 0;
        }
    }
    public static void main(String[] args){
        Mian mian = new Mian();
        System.out.println(mian.solution(3,20,4));
    }
}
