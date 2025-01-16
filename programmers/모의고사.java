import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int maxResult = 0;

        List<GaveUpMath> gaveUpPersons = List.of(
                new One(answers),
                new Two(answers),
                new Three(answers)
            );

        for (GaveUpMath person : gaveUpPersons) {
            maxResult = Math.max(maxResult, person.getScore());
        }

        for (GaveUpMath person : gaveUpPersons) {
            if (person.getScore() == maxResult)
                answer.add(person.getId());
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

class GaveUpMath {
    private final int[] sheet;

    private int id;

    private int score;

    public GaveUpMath(int id, int[] sheet, int[] answers) {
        this.id = id;
        this.sheet = sheet;

        grade(answers);
    }

    public int getId() {
        return this.id;
    }

    public int getScore() {
        return this.score;
    }

    public void grade(int[] answers) {
        Queue<Integer> answerQueue = new LinkedList<>();

        for (int answer : answers) {
            answerQueue.add(answer);
        }

        int index = 0;
        int result = 0;

        while (!answerQueue.isEmpty()) {
            int answer = answerQueue.poll();

            if (this.sheet[index] == answer)
                result++;

            index++;

            if (index == sheet.length)
                index = 0;
        }

        this.score = result;
    }
}

class One extends GaveUpMath {
    public One(int[] answers) {
        super(1, new int[] { 1, 2, 3, 4, 5 }, answers);
    }
}

class Two extends GaveUpMath {
    public Two(int[] answers) {
        super(2, new int[] { 2, 1, 2, 3, 2, 4, 2, 5 }, answers);
    }
}

class Three extends GaveUpMath {
    public Three(int[] answers) {
        super(3, new int[] { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 }, answers);
    }
}