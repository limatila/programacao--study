package unifametroExercises;

import java.util.Locale;
import java.util.Scanner;

class calculateEnergyBill {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);//use points in decimals

        //*exer 52 from repetition schema, with some changes
        int clientId, clientType; //1- residential, 2- comercial, 3- industrial, will have greater price with the greater number
        double baseKmhCurrency, adjustedKmhCurrency, clientKmh, paymentTotal = 0, totalKmhUsage = 0;
        String clientName, clientResume = "", clientTypeString = "";

        System.out.println("This is a program to calculate information about client's energy bills\n");
        

        System.out.print("Input the number of clients to be analyzed\t->");
        int totalClients = scanner.nextInt();

        System.out.print("Input the current KMH value for the period\t->");
        baseKmhCurrency = scanner.nextDouble();
        adjustedKmhCurrency = baseKmhCurrency;

        for(int i = 0; i < totalClients; ++i){
            System.out.println("Starting the " + (i+1) + "° client");

            //colecting
            System.out.print("Enter the client name\t->");
            clientName = scanner.next();
            System.out.print("Enter the type of account(1-3)\t->");
            clientType = scanner.nextInt();
            switch (clientType) { //deciding type of kmh
                case 1:
                    clientTypeString = "residential";
                    break;
                case 2:
                    clientTypeString = "comercial";
                    adjustedKmhCurrency = ( baseKmhCurrency + 0.20 );
                    break;
                case 3:
                    clientTypeString = "industrial";
                    adjustedKmhCurrency = ( baseKmhCurrency + 0.60 );
                    break;
            
                default:
                    System.out.println("Client type inputed incorrectly, use only 1-3. Restarting client");
                    --i;
                    break;
            }

            System.out.print("Enter the KWH used in the given period\t->");
            clientKmh = scanner.nextDouble();

            //analyzing
            double clientPaymentTotal = ( clientKmh * adjustedKmhCurrency );

            paymentTotal += clientPaymentTotal;
            totalKmhUsage += clientKmh;

            clientResume += ("\nThe " + (i+1) + "° Client on the name of " + clientName + 
                            " on the type of account \'"+ clientTypeString +
                            "\' has to pay a total of $" + String.format("%.2f", clientPaymentTotal));
        }


        System.out.println( clientResume );
        double mediaKmhUsage = totalKmhUsage/totalClients;
        System.out.println( "The average usage of energy for this period is: " + String.format("%.2f", mediaKmhUsage) );
        System.out.println( "The total amount payed in the period was of " + String.format("%.3f", paymentTotal) );

        System.out.println("\nFinishing program...");
    }
}