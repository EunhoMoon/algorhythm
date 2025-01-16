import java.util.Arrays;
import java.util.Collections;

class Solution {
    private int answer = -1;
    private String[][] park;
    private int[] mats;

    public int solution(int[] mats, String[][] park) {
        Arrays.sort(Arrays.stream(mats).boxed().toArray(), Collections.reverseOrder());
        this.park = park;
        this.mats = mats;

        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[i].length; j++) {
                if (park[i][j].equals("-1")) getAnswer(i, j);
            }
        }

        return answer;
    }

    private void getAnswer(int x, int y) {
        for (int mat : mats) {
            boolean isPossible = true;

            for (int i = 0; i < mat; i++) {
                for (int j = 0; j < mat; j ++) {
                    int nx = x + i;
                    int ny = y + j;

                    if (isValidCoord(nx, ny)) {
                        isPossible = false;
                        break;
                    }
                }
            }

            if (isPossible) {
                this.answer = Math.max(this.answer, mat);
            }
        }
    }

    private boolean isValidCoord(int nx, int ny) {
        return (nx >= park.length || ny >= park[0].length) || !park[nx][ny].equals("-1");
    }
}