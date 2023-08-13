package com.eelbbor.boottemplate;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class MainTest {
    @Test
    public void testSomeStuff() {
        Main main = new Main();
        assertEquals("should return 0 when both numbers are equal", 0, main.compare(1, 1));
    }
}