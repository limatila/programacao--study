package unifametroExercises;

import java.util.Scanner;

public class mortalityAnalyzer {
    public static void main(String[] args) {
        //48.

        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantas crianças nascidas no periodo amostral\t=> ");
        double periodQuantity = scanner.nextInt(), deadMasculine = 0, deadFeminine = 0;
        int totalGreaterThen_twoY = 0, currentMonthLived;
        String sex = "";

        while (sex != "vazio") {
            // asking which sex
            System.out.print("Qual o sexo da criança morta\t=> ");
            sex = scanner.next().toLowerCase();
            if (sex.contains("vazio")) {
                System.out.println("Stopping insertions...");
                break;
            }

            System.out.print("Quantos meses a criança viveu\t=> ");
            currentMonthLived = scanner.nextInt();
            if(currentMonthLived > 24){ totalGreaterThen_twoY++; };

            if (sex.charAt(0) == 'm') {
                deadMasculine++;
            } else if (sex.charAt(0) == 'f') {
                deadFeminine++;
            } else {
                System.out.println("Sexo mal inserido, morte não contada.");
            }
        }

        double mascDeadPorcentage = (deadMasculine / periodQuantity)*100.0;
        double femDeadPorcentage = (deadFeminine / periodQuantity)*100.0;

        System.out.println("A porcentagem de crianças meninos mortas foi " + mascDeadPorcentage + "%");
        System.out.println("A porcentagem de crianças meninas mortas foi " + femDeadPorcentage + "%");
        System.out.println("O total de crianças com mais de 24 meses que morreram foi " + totalGreaterThen_twoY);

    }
}
