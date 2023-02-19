package programmers;

import java.util.Stack;

/*
문제 주소 : https://school.programmers.co.kr/learn/courses/30/lessons/133502

문제 접근 방법 & 사용 알고리즘:
    1. 스택을 생성하고 배열 주는 것을 스택에 push한다.
    2. 스택 크기가 4 이상일 때 스택이 1231이 연달아 들어가 있는 경우 answer 값 증가 후, pop을 통해 삭제
*/
public class Hamburger {
    public int solution(int[] ingredient) {
        int answer = 0;
        Stack<Integer> al = new Stack<>();

        for(int in : ingredient) {
            al.push(in);

            if (al.size() >= 4) {
                if (al.get(al.size() - 4) == 1
                        && al.get(al.size() - 3) == 2
                        && al.get(al.size() - 2) == 3
                        && al.get(al.size() - 1) == 1) {
                    answer++;
                    al.pop();
                    al.pop();
                    al.pop();
                    al.pop();
                }
            }
        }
        return answer;
    }
    public static void main(String[] args) {
        Hamburger hamburger = new Hamburger();
        int[] am1 = new int[]{2,1,1,2,3,1,2,3,1};
        int[] am2 = new int[]{1, 3, 2, 1, 2, 1, 3, 1, 2};
        System.out.println(hamburger.solution(am1));
        System.out.println(hamburger.solution(am2));
    }
}
