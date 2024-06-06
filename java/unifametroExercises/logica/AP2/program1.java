package unifametroExercises.AP2;

import java.util.Scanner;

class questao1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String sexo = "a";
        int totalFem = 0, totalMasc = 0, i = 0;

        System.out.println("Este é um programa que conta quantas pessoas são do sexo masculino ou feminino");
        System.out.println("Insira 'vazio' no campo de sexo para parar de contar e apresentar o valor");

        System.out.println("\nComeçando...");

        while ( true ) {
            System.out.print("\nInsira o sexo da " + (i+1) + "° Pessoa(F/M)\t->");
            sexo = scanner.next().toUpperCase();
            if (sexo.contains("VAZIO")) {
                System.out.println("Saindo das inserções...");
                break;
            }

            if (sexo.charAt(0) == 'F') {
                totalFem++;
            } else if (sexo.charAt(0) == 'M') {
                totalMasc++;
            } else {
                System.out.println("Sexo mal inserido! Insira 'F' ou 'M'");
                --i;
            }

            i++;
        }

        System.out.println("O número de homens:" + totalMasc);
        System.out.println("O número de mulheres:" + totalFem);

        System.out.println("\nTerminando Programa");
        scanner.close();
    }
}
