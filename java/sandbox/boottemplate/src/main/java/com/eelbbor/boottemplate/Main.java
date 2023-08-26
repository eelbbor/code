package com.eelbbor.boottemplate;

import com.google.common.primitives.Ints;

public class Main {
    public static int compare(int a, int b) {
        return Ints.compare(a, b);
    }

    public static void main(String... args) throws Exception {
        Main app = new Main();
        System.out.println("Success: " + app.compare(2, 1));
    }
}