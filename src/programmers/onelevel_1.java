package programmers;
/*
문제 주소 :  https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=java

문제 접근 방법 & 사용 알고리즘:
    1. p의 길이 len을 저장합니다. 그리고 수를 비교하기 위해 문자열 p를 Long 형태로 변환합니다. (num)
    2. for문을 이용해서 문자열 t를 Long 형태로 변환한 후(diff), diff 와 num 수를 비교합니다.
    3. diff 가 더 작거나 같을 경우 answer 값을 1 늘립니다.
Long 형태로 저장하는 이유 : 문자열이 너무 길어질 경우 int로 저장하면 오류가 납니다.
*/
public class onelevel_1 {
    public int solution(String t, String p) {
        int len = p.length();
        long num = Long.parseLong(p);
        int answer = 0;

        for (int i=0; i < t.length() - len + 1; i++){
            long diff = Long.parseLong(t.substring(i,i+len));
            if (diff <= num) answer++;
        }
        return answer;
    }
    public static void main(String[] args) {
        onelevel_1 onelevel1 = new onelevel_1();
        System.out.println(onelevel1.solution("3141592", "271"));
        System.out.println(onelevel1.solution("500220839878","7"));
        System.out.println(onelevel1.solution("10203","15"));
    }
}

