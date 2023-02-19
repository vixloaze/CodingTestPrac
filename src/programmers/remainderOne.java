package programmers;
/*
문제 주소 : https://school.programmers.co.kr/learn/courses/30/lessons/87389

문제 접근 방법 & 사용 알고리즘:
    1. 반복문 통해서 나머지가 1인 i 값 찾으면 break 하면 끝
*/
public class remainderOne {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<n; i++){
            if (n % i == 1) {
                answer = i;
                break;
            }
        }
        return answer;
    }
    public static void main(String[] args){
        remainderOne remainderOne = new remainderOne();
        System.out.println(remainderOne.solution(10));
        System.out.println(remainderOne.solution(12));
    }
}
