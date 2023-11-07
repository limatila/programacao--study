package unifametroExercises;

import java.util.Scanner;

public class mortalityAnalyzer {
    public static void main(String[] args) {
        //48.

        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantas crianças analisadas no periodo\t=> ");
        int periodQuantity = scanner.nextInt(), deadQuantity = 0,
                deadMasculine = 0, deadFeminine = 0;
        String sexo = "";

        while (sexo != "vazio") {
            // asking which sex
            System.out.print("Qual o sexo da criança morta\t=> ");
            sexo = scanner.next().toLowerCase();
            if (sexo == "vazio") {
                System.out.println("Stopping insertions...");
                break;
            }

            System.out.print("Quantos meses a criança viveu\t=> ");
            int numMonthsLived = scanner.nextInt();

            if (sexo.charAt(0) == 'm') {
                deadMasculine++;
                deadQuantity++; // counting total of deaths
            } else if (sexo.charAt(0) == 'f') {
                deadFeminine++;
                deadQuantity++; // counting total of deaths
            } else {
                System.out.println("Sexo mal inserido, morte não contada.");
            }
        }

        double mascDeadPorcentage = (deadMasculine / deadQuantity);
        double femDeadPorcentage = (deadFeminine / deadQuantity);

        System.out.println("A porcentagem de crianças meninos mortas foi " + mascDeadPorcentage + "%");
        System.out.println("A porcentagem de crianças meninas mortas foi " + femDeadPorcentage + "%");

    }
}
