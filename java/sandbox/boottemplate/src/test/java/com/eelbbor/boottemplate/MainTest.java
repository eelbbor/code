package com.eelbbor.boottemplate;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


public class MainTest {
    @Test
    public void testSomeStuff() {
        Assertions.assertEquals(0, Main.compare(1, 1), "should return 0 when both numbers are equal");
    }
}