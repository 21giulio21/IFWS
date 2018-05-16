package com.company;

import java.awt.*;
import java.awt.event.InputEvent;

public class Main {

    public static void main(String[] args) throws AWTException {

        for(int i= 0; i < 10000; i++) {
            Robot robot = new Robot();

            robot.mousePress(InputEvent.BUTTON1_MASK);
            robot.delay(200);
            robot.mouseRelease(InputEvent.BUTTON1_MASK);
            robot.delay(200);
        }

    }
}
