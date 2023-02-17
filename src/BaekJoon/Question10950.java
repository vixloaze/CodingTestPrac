package BaekJoon;

import java.util.Scanner;

/*
문제 주소 :  https://www.acmicpc.net/problem/2739

문제 접근 방법 & 사용 알고리즘:
    덧셈이니 작성하지 않는다.
*/
public class Question10950 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        for(int i=0; i<T; i++){
            int a = scan.nextInt();
            int b = scan.nextInt();
            System.out.println(a+b);
        }
    }
}
