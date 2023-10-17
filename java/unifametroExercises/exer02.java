package unifametroExercises;

import java.util.Scanner;
import java.util.function.ToIntFunction;

class exer02{
    public static void main (String[] args){
        
        Scanner scanner = new Scanner(System.in);

        //1.
        System.out.println("Insira um número inteiro: ");
        int numInserted = scanner.nextInt();
        System.out.println("Iterando..");
        
        for(int i = 0; i<= numInserted; i++){ //numInserted = delimitador.
            System.out.println(i);
        }


        //2.
        System.out.println("Iterando somente em pares...");
        
        for(int i = 0; i <= numInserted; i++){ //numInserted = delimitador.
            if(i%2 == 0){
                System.out.println(i);
            }
        }

        
        //3.
        System.out.println("Iterando adicionando um por um até o num limite...");

        int soma = 0;
        for(int i = 0; soma <= numInserted; i++){
            soma += i;
            System.out.println(soma);
        }


        //4.
        System.out.println("Uma tabuada do num inserido:");

        for(int i = 1; i <= 10; i++){
            int multip = numInserted * i;
            System.out.println(numInserted + " vezes " + i + " = " + multip);
        }

        //*.
	    int counter = 5;
        while (counter <= 15){
            if(counter % 2 != 0){
                System.out.println("Iterando ímpares: " + counter);
            }
            counter++;
        }


        //5.
        System.out.println("Iterando divisíveis por 4:");
        for(int i = 0; i <= numInserted; i++){
            if(i % 4 == 0){
                System.out.println(i);
            }
        }

        //6.
        System.out.println("Apresentando potências de 3 de 0 a 10");

        int base = 5;
        int total = base;
        int i = 1;
        int expoente = 3;

        while(i <= expoente){
            total = total * base;
            
            System.out.println(total);
            i++;
        }

        //7.
    }
}