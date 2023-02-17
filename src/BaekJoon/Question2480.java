package BaekJoon;

import java.util.Scanner;

public class Question2480 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num1 = scan.nextInt();
        int num2 = scan.nextInt();
        int num3 = scan.nextInt();

        if(num1 != num2 && num2 != num3 && num1 != num3) {
            int max;
            if(num1 > num2) {
                if(num3 > num1) max=num3;
                else max=num1;
            }
            else {
                if(num3 > num2) max=num3;
                else max=num2;
            }
            System.out.println(max *100);
        }
        else {
            if(num1 == num2 && num1 == num3){
                System.out.println(10000 + num1*1000);
            }
            else {
                if(num1 == num2 || num1 == num3){
                    System.out.println(1000 + num1*100);
                }
                else {
                    System.out.println(1000 + num2*100);
                }
            }
        }

    }
}
