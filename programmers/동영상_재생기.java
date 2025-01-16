class Solution {
    private int videoSec;
    private int presentSec;
    private int opStartSec;
    private int opEndSec;

    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        this.videoSec = getSec(video_len);
        this.presentSec = getSec(pos);
        this.opStartSec = getSec(op_start);
        this.opEndSec = getSec(op_end);

        jumpOp();

        for (String command : commands) {
            commandControl(command);
        }

        return toStringFormat();
    }
    
    private void commandControl(String command) {
        if (command.equals("next")) {
            presentSec += 10;
            if (this.presentSec > this.videoSec)
                this.presentSec = this.videoSec;
        } else {
            this.presentSec -= 10;
            if (this.presentSec < 0)
                this.presentSec = 0;
        }
        jumpOp();
    }
    
    private int getSec(String strTime) {
        String[] strSplit = strTime.split(":");
        return Integer.parseInt(strSplit[0]) * 60 + Integer.parseInt(strSplit[1]);
    }
    
    private String toStringFormat() {
        String minStr = String.valueOf(this.presentSec / 60);
        String secStr = String.valueOf(this.presentSec % 60);

        if (minStr.length() == 1)
            minStr = "0" + minStr;
        if (secStr.length() == 1)
            secStr = "0" + secStr;

        return minStr + ":" + secStr;
    }

    private void jumpOp() {
        if (this.opStartSec <= this.presentSec & this.presentSec <= this.opEndSec) {
            this.presentSec = this.opEndSec;
        }
    }
}