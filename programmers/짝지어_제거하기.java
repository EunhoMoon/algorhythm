import java.util.Stack;

class Solution {
    public int solution(String s) {
        Stack<String> stackChar = new Stack<>();

        for (char c : s.toCharArray()) {
            String present = String.valueOf(c);
            if (stackChar.empty() || !stackChar.peek().equals(present)) {
                stackChar.add(present);
            } else {
                stackChar.pop();
            }
        }

        return stackChar.empty() ? 1 : 0;
    }
}