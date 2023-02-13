package programmers;
/*
문제 주소 :  https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=java

문제 접근 방법 & 사용 알고리즘:
    1. 1부터 number까지 약수 개수를 구해서 Array에 등록한다.
    2. Array를 돌면서 limit 을 초과하는 member를 power값으로 변경한다.
    3. 공격력 1당 1Kg 이기 때문에 Array에 있는 member 값을 전부 더한다.
*/
public class KnightWeapon {
    public int divisor(int number) {
        int cnt=0;
        for(int i=1; i<=number; i++) {
            if(number % i == 0) cnt++;
        }
        return cnt;
    }
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int count = 0;
        int[] attack = new int[number];
        for (int i=1; i<=number; i++) {
            attack[i-1] = divisor(i);
        }

        for(int i=0; i<number; i++) {
            if(attack[i] > limit) attack[i] = power;
        }
        for(int i=0; i<number; i++) {
            answer += attack[i];
        }
        return answer;
    }
    public static void main(String[] args) {
        KnightWeapon knightWeapon = new KnightWeapon();
        System.out.println(knightWeapon.solution(5,3,2));
        System.out.println(knightWeapon.solution(10,3,2));
    }
}
