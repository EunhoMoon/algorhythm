import java.util.*;

class Friend {
    private final String name;
    private final Map<String, Integer> sendList = new HashMap<>();
    private int totalSend = 0;
    private int totalRecieve = 0;
    private int expectedGift = 0; 

    public Friend(String name, String[] friends) {
        this.name = name;
        this.initFirends(friends);
    }

    private void initFirends(String[] friends) {
        for (String friendName : friends) {
            if (!friendName.equals(this.name)) this.sendList.put(friendName, 0);
        }
    }

    public void sendGift(String reciever) {
        this.totalSend++;
        this.sendList.put(reciever, this.sendList.getOrDefault(reciever, 0) + 1);
    }

    public void recieveGift() {
        this.totalRecieve++;
    }

    public int getGiftIndex() {
        return this.totalSend - this.totalRecieve;
    }

    public int getExpectGift(Map<String, Friend> given) {
        for (String friendName : this.sendList.keySet()) {
            int count = this.sendList.get(friendName);
            Friend reciever = given.get(friendName);

            if (canExpected(count, reciever)) this.expectedGift++;
        }

        return this.expectedGift;
    }

    private boolean canExpected(int count, Friend reciever) {
        return count > reciever.sendList.get(this.name) ||
        (count == reciever.sendList.get(this.name) & this.getGiftIndex() > reciever.getGiftIndex());
    }
}

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;

        Map<String, Friend> given = new HashMap<>();

        for (String friend : friends) {
            Friend newFriend = new Friend(friend, friends);
            given.put(friend, newFriend);
        }

        for (String gift : gifts) {
            String[] splitGift = gift.split(" ");
            String sender = splitGift[0];
            String reciever = splitGift[1];

            given.get(sender).sendGift(reciever);
            given.get(reciever).recieveGift();
        }

        for (String friendName : given.keySet()) {
            answer = Math.max(answer, given.get(friendName).getExpectGift(given));
        }

        return answer;
    }
}