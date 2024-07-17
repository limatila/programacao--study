package unifametroExercises;

import java.util.Scanner;
import java.util.Locale;

public class calculateHotelBill {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        int clientCount, clientDays;
        double clientPaymentTotal, basePayment = 30.00, adjustedPayment = basePayment, paymentSum = 0;
        String nome, paymentResume = "";

        System.out.println("Este é um programa que faz o cálculo de contas de turitas de uma pousada.");
        System.out.println("\nComeçando...");

        System.out.print("Informe o número de turistas alocados\t->");
        clientCount = scanner.nextInt();

        for(int i = 0; i < clientCount; i++){
            System.out.print("Insira o nome do " + (i+1) + "° Cliente\t->");
            nome = scanner.next();

            System.out.print("Insira a quantidade de dias contratados no lote de desejo\t->");
            clientDays = scanner.nextInt();

            if (clientDays > 20) { //maior que 10, 8reais a mais, maior que 20, 23reais a mais
                adjustedPayment += 15.00;
            } 
            if (clientDays > 10) {
                adjustedPayment += 8.00;
            }

            clientPaymentTotal = ( clientDays*adjustedPayment );
            paymentResume += ( "\nO cliente "+ nome + " sobe número de conta "+ (i+1) + " deve pagar R$" + String.format("%.2f", clientPaymentTotal) );

            paymentSum += clientPaymentTotal; //adicionando total ganho
            adjustedPayment = basePayment; //resetando
        }

        System.out.println( paymentResume );
        System.out.println( "O total ganho foi de R$" + String.format("%.2f", paymentSum) );
        
        System.out.println("Programa terminando...");
        scanner.close();
    }
}
