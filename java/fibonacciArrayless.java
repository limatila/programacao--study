import java.util.Scanner;

public class fibonacciArrayless {
    public static void main(String[] args) {
        int last = 0, current = 1, next, maxIteration;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Insert the number of iterations to generate:");
        maxIteration = scanner.nextInt();

        int i = 0;
        while (i < maxIteration) {
            //presentation
            System.out.print(current + ", ");

            //logic
            next = current + last;
            last = current; 
            current = next; //1, 2, 3, 5, 8, 13, 21

            i++;
        }

        scanner.close();
    }
}
