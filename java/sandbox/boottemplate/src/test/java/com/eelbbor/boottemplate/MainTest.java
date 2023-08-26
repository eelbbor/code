package com.eelbbor.boottemplate;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;



public class MainTest {
    @Test
    public void testSomeStuff() {
        Main main = new Main();
        Assertions.assertEquals(0, main.compare(1, 1), "should return 0 when both numbers are equal");
    }
}