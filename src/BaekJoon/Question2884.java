package BaekJoon;
import java.util.Scanner;
/*
문제 주소 :  https://www.acmicpc.net/problem/2884

문제 접근 방법 & 사용 알고리즘:
    1. 0시 일 경우
        1-1. 45분 이전일 경우 23시로 바꾸고 분 계산
        1-2. 45분 이후일 경우 시는 그대로 분 계산
    2. 나머지 경우
        2-1. 45분 이전일 경우 23시로 바꾸고 분 계산
        2-2. 45분 이후일 경우 시는 그대로 분 계산
*/
public class Question2884 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int hour = scan.nextInt();
        int min = scan.nextInt();

        if(hour == 0) {
            if(min <45) {
                hour = 23;
                min = 60 - (45-min);
                System.out.println(hour + " "+ min);
            }
            else if (min>=45) {
                min -= 45;
                System.out.println(hour + " "+ min);
            }
        }
        else {
            if(min <45) {
                hour -= 1;
                min = 60 - (45-min);
                System.out.println(hour + " "+ min);
            }
            else if (min>=45) {
                min -= 45;
                System.out.println(hour + " "+ min);
            }
        }
    }
}
