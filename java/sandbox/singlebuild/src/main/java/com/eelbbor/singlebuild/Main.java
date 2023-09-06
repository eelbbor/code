package com.eelbbor.singlebuild;

import com.google.common.primitives.Ints;

public class Main {
    public static int compare(int a, int b) {
        return Ints.compare(a, b);
    }

    public static void main(String... args) throws Exception {
        System.out.println("Success: " + Main.compare(2, 1));
    }
}