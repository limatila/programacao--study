package unifametroExercises.AP2;

import java.util.Locale;
import java.util.Scanner;

class questao2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US); //favor inserir decimais com '.'

        int totalMasc = 0, totalFem = 0;
        double altura, totalAlturaFem = 0, maiorAltura = 0, menorAltura = 10000000;
        String sexo;

        for(int i = 0; i < 5; i++){
            System.out.print("\nInsira o sexo da " + (i+1) + "° Pessoa\t=>");
            sexo = scanner.next().toUpperCase();
            
            System.out.print("Insira a altura da mesma\t=>");
            altura = scanner.nextDouble();
            
            if (sexo.charAt(0) == 'F') {
                totalFem++;
                totalAlturaFem += altura;
            } else if (sexo.charAt(0) == 'M') {
                totalMasc++;
            } else {
                System.out.println("Sexo mal inserido! Insira 'F' ou 'M'");
                --i;
            }
            
            if (altura > maiorAltura) {
                maiorAltura = altura;
            }
            if (altura < menorAltura) {
                menorAltura = altura;
            }
        }

        double mediaAlturaFem = ( totalAlturaFem/totalFem );

        System.out.println("\nA menor altura do grupo inserido é: " + menorAltura + ", E a maior altura é: " + maiorAltura);
        System.out.println("A média das alturas das mulheres: " + String.format("%.2f", mediaAlturaFem));
        System.out.println("O número de homens presentes no grupo é de:" + totalMasc);

        scanner.close();
    }
}
