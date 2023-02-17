package BaekJoon;

import java.util.Scanner;

/*
문제 주소 :  https://www.acmicpc.net/problem/2753

문제 접근 방법 & 사용 알고리즘:
    1. 조건문을 사용해서 x 가 양수인지 판별
    1-2. y가 양수인지 음수인지에 따라 1,4사분면 판별
    2. x가 음수인지 판별
    2-1. y가 양수인지 음수인지에 따라 2,3사분면 판별
*/
public class Question14681 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int x = scan.nextInt();
        int y = scan.nextInt();

        if(x > 0) {
            if (y > 0) System.out.println("1");
            else if (y < 0) System.out.println("4");
        }
        else if(x<0) {
            if (y > 0) System.out.println("2");
            else if (y < 0) System.out.println("3");
        }
    }
}
