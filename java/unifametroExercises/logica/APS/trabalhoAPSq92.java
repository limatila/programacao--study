package APS;

import java.util.Scanner;
import java.util.Locale;

class qNoventaEum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        int matricula = 1, totalAprovM = 0, totalAprovF = 0, totalAlunos, totalAlunasF = 0;
        double nota = 0, mediaAlun, maiorMediaAlunM = 0, maiorMediaAlunF = 0;
        String sexo;

        System.out.println("Este é um programa que coleta notas de alunos, \nE faz alguns tratamentos, mostrando informações sobre a turma\n");

        System.out.print("Insira o número de alunos na turma\t=>");
        totalAlunos = scanner.nextInt();

        System.out.println("");
        System.out.println("Começando coleta de dados...");

        while ( matricula <= totalAlunos ) {
            System.out.println("A matrícula atual é a " + matricula + "°.");
            //coleta:
            System.out.print("Insira o sexo do(a) aluno(a) (M/F)\t=>");
            sexo = scanner.next().toUpperCase();

            for( int i = 0; i < 3; i++ ){
                System.out.print("Insira a " + (i+1) + "° Nota\t=>");
                nota += scanner.nextDouble();
            };
            mediaAlun = nota/3; //media atual

            //tratamento:
            if (sexo.charAt(0) == 'M') {
                if ( mediaAlun > maiorMediaAlunM ) {
                    maiorMediaAlunM = mediaAlun;
                }
            } else if (sexo.charAt(0) == 'F') {
                if ( mediaAlun > maiorMediaAlunF ) {
                    maiorMediaAlunF = mediaAlun;
                }

                totalAlunasF++;
            } else {
                System.out.println("Sexo mal inserido, recomeçando cadastro do aluno...");
                matricula -= 1;
            };

            if (sexo.charAt(0) == 'F') {
                if(mediaAlun > 7){
                    totalAprovF++;
                }
            } else if (sexo.charAt(0) == 'M') {
                if(mediaAlun > 7){
                    totalAprovM++;
                }
            } else {
                System.out.println("Sexo mal inserido, recomeçando cadastro do aluno...");
                matricula -= 1;
            };

            System.out.println("Média da matricula:" + String.format("%.2f", mediaAlun));

            mediaAlun = 0; nota = 0; //resetando
            matricula++; //pular para o próximo na lista
        };
        System.out.println("");
        System.out.println("Concluindo...");

        double alunasPercent = ( (totalAlunasF * 100.0) / totalAlunos );
        double alunasPercentAprov = ( (totalAprovF * 100.0) / totalAlunasF);

        System.out.println("A maior média feminina: " + String.format("%.1f", maiorMediaAlunF));
        System.out.println("A maior média masculina: " + String.format("%.1f", maiorMediaAlunM));
        System.out.println("O percentual de mulheres na turma: " + String.format("%.2f", alunasPercent) + "%"); //!
        System.out.println("Quantidade de alunos aprovados: " + (totalAprovF + totalAprovM));
        System.out.println("O percentual de alunas aprovadas dentre as outras: " + String.format("%.2f", alunasPercentAprov) + "%"); //!

        System.out.println("");
        scanner.close();
        System.out.println("Terminando o programa...");
    }
}
