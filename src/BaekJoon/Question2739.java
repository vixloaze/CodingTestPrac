package BaekJoon;

import java.util.Scanner;
/*
문제 주소 :  https://www.acmicpc.net/problem/2739

문제 접근 방법 & 사용 알고리즘:
    구구단이니 작성하지 않는다.
*/
public class Question2739 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for(int i=1; i<=9; i++) {
            System.out.println(n+" * "+i+" = "+n*i);
        }
    }
}
