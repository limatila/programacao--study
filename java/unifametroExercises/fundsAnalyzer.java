import java.util.Locale;
import java.util.Scanner;

class fundsAnalyzer {
    public static void main(String[] args) {
        //develop a way to calculate which account has suficient funds in taxation
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US); //*specifying locale to select which double separator is used

        int id = 0;
        double balanceMinimumFunds, availableFunds, resultBalance;
        boolean isAvailable;

        System.out.println("This is a program to analyze which account has funds or not.");
        System.out.println("Input 'id' blank to stop the program.");

        System.out.println("");
        System.out.print("What is the minimun balance permitted?\t-> ");
        balanceMinimumFunds = scanner.nextDouble();
        System.out.println("");

        while ( true ) {
            System.out.print("Insert the account id\t-> ");
            id = scanner.nextInt();
            if ( id == 0 ) { break; } //if 0 inputted, exits.

            System.out.print("Input the total available funds of it\t-> ");
            availableFunds = scanner.nextDouble();

            resultBalance = availableFunds - balanceMinimumFunds;
            isAvailable = resultBalance >= 0;           //directly returns to variable the statement

            System.out.print("The account on id " + id + " has resulted in the balance of " 
                            + String.format("%.2f", resultBalance)
                            + " ");
            if ( isAvailable == false) {
                System.out.println("- NOT AVAILABLE");
            } else { System.out.println(""); }
        }

        System.out.println("Finishing...");
    }
}