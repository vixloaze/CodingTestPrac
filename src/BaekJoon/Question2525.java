package BaekJoon;

import java.util.Scanner;

/*
문제 주소 :  https://www.acmicpc.net/problem/2884

문제 접근 방법 & 사용 알고리즘:
    1. 차례대로 시, 분, 걸리는 시간을 입력
    2. 걸리는 시간을 60으로 나눈 몫을 시에, 나머지를 분에 더한다.
    3. 60분이 넘어갈 경우 1시간 증가
    4. 24시가 넘어갈 경우 0시로 바꾸도록 24를 뺀다.
*/
public class Question2525 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int hour = scan.nextInt();
        int min = scan.nextInt();
        int after = scan.nextInt();

        hour += after / 60;
        min += after % 60;

        if(min >= 60) {
            hour += 1;
            min -= 60;
        }
        if(hour >= 24){
            hour -=24;
        }
        System.out.println(hour + " " + min);
    }
}
