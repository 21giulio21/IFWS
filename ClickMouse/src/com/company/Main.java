import java.awt.*;
import java.awt.event.InputEvent;

public class Main {

    public static void main(String[] args) throws AWTException, InterruptedException {

        Robot robot = new Robot();

        Thread.sleep(3000);
        for(int i= 0; i < 10000; i++) {


            robot.mousePress(InputEvent.BUTTON1_MASK);
            robot.delay(50);
            robot.mouseRelease(InputEvent.BUTTON1_MASK);
            robot.delay(50);
        }

    }
}
