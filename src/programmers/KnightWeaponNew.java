package programmers;
/*
문제 주소 :  https://school.programmers.co.kr/learn/courses/30/lessons/136798?language=java

문제 접근 방법 & 사용 알고리즘:
    1. 1부터 number까지 약수 개수를 구해서 Array에 등록한다.
    2. Array를 돌면서 limit 을 초과하는 member를 power값으로 변경한다.
    3. 공격력 1당 1Kg 이기 때문에 Array에 있는 member 값을 전부 더한다.
----------------------------------------------------------------
    기존에 풀었던 것으로 테스트 해보니 시간 초과가 발생하여 코드를 수정해야 했습니다.
코드 변경점:
    1. 너무 많은 반복문 사용 -> 최대한 반복문 사용을 줄이게 코드 변경
    2. 약수 구하는 방법의 문제 -> number가 커지면 시간적 효율이 너무 않좋음 -> 다른 약수 구하는 방법 사용
    --> number의 약수 중 하나가 i 라 했을 때, 다른 약수는 number/i 이 되므로 하나의 약수를 알면 다른 하나의 존재가 보장
    이 코드로 정답 제출하니 무사히 정답 처리 되었습니다.
*/
public class KnightWeaponNew {
    public int divisor(int number) {
        int cnt=0;
        for(int i=1; i * i<=number; i++) {
            if(i*i == number) cnt++;
            else if(number % i == 0) cnt+=2;
        }
        return cnt;
    }
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] attack = new int[number];
        for (int i=1; i<=number; i++) {
            attack[i-1] = divisor(i);
        }

        for(int i=0; i<number; i++) {
            if(attack[i] > limit) attack[i] = power;
            answer += attack[i];
        }
        return answer;
    }
    public static void main(String[] args) {
        KnightWeaponNew knightWeapon = new KnightWeaponNew();
        System.out.println(knightWeapon.solution(5,3,2));
        System.out.println(knightWeapon.solution(10,3,2));
    }
}
