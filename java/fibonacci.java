import java.util.Arrays;

class fibonacci {
    public static void main(String[] args) {

        int fib[] = { 1, 1 };

        for (var i = 0; i < 10; i++) {
            int newV = fib[i] + fib[i + 1];

            fib = Arrays.copyOf(fib, fib.length + 1); // ceate copy, resize slots
            fib[fib.length - 1] = newV;               // assign the new value to the last slot

        };

        System.out.println(Arrays.toString(fib));

    }
}