package com.company;

import java.awt.*;
import java.awt.event.InputEvent;

public class Main {

    public static void main(String[] args) throws AWTException, InterruptedException {
        while (true) {
            click(600, 700);
            Thread.sleep(1000);
        }
    }

    public static void click(int x, int y) throws AWTException{
        Robot bot = new Robot();
        bot.mouseMove(x, y);
        bot.mousePress(InputEvent.BUTTON1_MASK);
        bot.mouseRelease(InputEvent.BUTTON1_MASK);
    }
}
