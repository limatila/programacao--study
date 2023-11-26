package APS;

import java.util.Locale;
import java.util.Scanner;

class qSessentaEum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US); //use '.' to decimals

        int totalAprov = 0, totalAlunTurma, totalTurmas, totalAlun = 0, iterationTurma = 1, iterationAlun = 1;
        double mediaTurma, notaFinalAlun = 0, notaTotalTurma = 0;
        String resumeMedias = "";

        System.out.println("Este é um programa que coleta notas finais de alunos de turmas diferentes.");
        System.out.println("Depois de coletar, apresentará a média de desempenho por turma, e a porcentagem de alunos aprovados.");
        System.out.println("Começando programa...");

        System.out.println("");
        System.out.print("Insira o número de turmas do período letivo\t=>");
        totalTurmas = scanner.nextInt();

        //coletando
        while (iterationTurma <= totalTurmas) {
            System.out.println("");
            System.out.println("Começando a turma " + iterationTurma);
            System.out.print("Insira o número de alunos desta turma\t=>");
            totalAlunTurma = scanner.nextInt();
            totalAlun += totalAlunTurma;

            while (iterationAlun <= totalAlunTurma) {
                System.out.print( "Digite a nota do " + iterationAlun + "° Aluno\t=>" );
                notaFinalAlun = scanner.nextDouble();

                if (notaFinalAlun >= 7) {
                    totalAprov++;
                }

                notaTotalTurma += notaFinalAlun;

                iterationAlun++;
            }
            
            //guardando media
            mediaTurma = ( notaTotalTurma/totalAlunTurma );
            resumeMedias = resumeMedias.concat("\nA média da " + iterationTurma + "° Turma foi de: " + String.format("%.2f", mediaTurma));
            
            mediaTurma = 0; notaTotalTurma = 0; iterationAlun = 1;//resetando, mais fácil num 'for'
            iterationTurma++;
        };

        //apresentando
        System.out.println(resumeMedias);
        System.out.println("A porcentagem de alunos aprovados foi de aproximadamente " + ( ( totalAprov * 100 ) / totalAlun ) + "%");

        System.out.println("");
        System.out.println("Programa terminando...");
        scanner.close();
    }
}