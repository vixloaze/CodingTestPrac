package programmers;

import java.util.Arrays;

/*
문제 주소 :  https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=java

문제 접근 방법 & 사용 알고리즘:
    1. 배열을 내림차순으로 정렬
    2. 문제 예시로 내림차순 정리하면 [3,3,2,2,1,1,1] 이다.
    3. 여기서 m개씩 박스에 담고, 위 배열에서 4개씩 자른다. (m=4)
    4. 그러면 [3,3,2,2] 가 되고 나머지는 [1,1,1] 이다. 뒤 배열을 4개 못채웠으므로 버린다.
    5. 그래서, 아래의 while문 및 if문에서 index에 m을 더했을 때 초과하는 경우는 while문에서 빠져나온다.
    6. 개수가 되는 경우는 맨 마지막 인덱스에 있는 값이 최소값이므로 그 점수에 m을 곱한다.

    재풀이가 필요하다. 고칠 부분이 많다.
*/
public class fruitsend {

    public int solution(int k, int m, int[] score) {
        int answer = 0;

        Arrays.sort(score);

        int[] tScore = new int[score.length];

        // 배열 역순으로 정리하기
        for(int i=0; i< score.length; i++) {
            tScore[i] = score[score.length -1 - i];
        }

        int index = 0;
        // 배열에서 크기만큼 잘라서 계산하기
        while (true) {
            // 인덱스에 m을 더해서 초과하는 경우 break
            if (index >= tScore.length || index + m >tScore.length) {
                break;
            }

            // 개수가 되는 경우 맨 마지막 인덱스에 있는 값이 사과 점수의 최소값 * m
            answer += tScore[index + m - 1] * m;

            index += m;
        }

        return answer;
    }
    public static void main(String[] args) {
        fruitsend fruitsend1 = new fruitsend();
        int[] score1, score2;
        score1 = new int[]{1, 2, 3, 1, 2, 3, 1};
        score2 = new int[]{4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2};
        System.out.println(fruitsend1.solution(3,4,score1));
        System.out.println(fruitsend1.solution(4,3,score2));
    }
}
