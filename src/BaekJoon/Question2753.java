package BaekJoon;

import java.util.Scanner;

/*
문제 주소 :  https://www.acmicpc.net/problem/2753

문제 접근 방법 & 사용 알고리즘:
    1. 조건문을 사용해서 윤년을 판별한다.
*/
public class Question2753 {
    public static void main(String[] arg) {
        Scanner scan = new Scanner(System.in);
        int year = scan.nextInt();

        if((year % 4 == 0 && year % 100 != 0) || year % 400 ==0) {
            System.out.println("1");
        }
        else System.out.println("0");
    }
}
