package unifametroExercises;

import java.time.LocalDateTime;
import java.util.Scanner;

public class getAges {
    public static void main(String[] args) {

        //exer 27.

        Scanner scanner = new Scanner(System.in);

        String nome, maiorNome = "", menorNome = "";
        int anoNascimento, menorAno = 10000, maiorAno = 0, i = 0, maiorIdade = 0;
        char resp = 'S';

        while (resp == 'S'){ //* if it goes "N", will stop
            // collecting data
            System.out.println("Digite um nome:");
            nome = scanner.next();
            System.out.println("Digite o ano de nascimento:");
            anoNascimento = scanner.nextInt();

            // analyzing
            if (anoNascimento > maiorAno) {
                maiorAno = anoNascimento;
                maiorNome = nome;
            }
            if (anoNascimento < menorAno) {
                menorAno = anoNascimento;
                menorNome = nome;
            }
            int anoAtual = LocalDateTime.now().getYear();//get current year from local time

            maiorIdade = (anoAtual - maiorAno) + 1;

            System.out.println("Deseja continuar?:");
            resp = scanner.next().toUpperCase().charAt(0);
            
            //contando quantas vezes
            i++;
        }

        System.out.println("");
        System.out.println("A pessoa com maior ano é " + maiorNome);
        System.out.println("A pessoa com menor ano é " + menorNome);

        System.out.println("A maior idade é " + maiorIdade);

        System.out.println("");
        System.out.println(i + " Pessoas inseridas");
    }
}