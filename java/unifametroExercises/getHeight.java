import java.util.Scanner;

public class getHeight {
  public static void main(String[] args) {
    
    Scanner scanner = new Scanner(System.in);

    int countMasc = 0, countFem = 0;
    double altura, maiorAltura = 0, 
    soma = 0, mediaAlturas;

    System.out.println("Quantas pessoas você quer comparar?: ");
    int numPessoas = scanner.nextInt();
    
    for(int i = 0; i < numPessoas; i++){
        
        System.out.println("Digite o seu sexo: ");
        char sexo = scanner.next().toUpperCase().charAt(0);
        System.out.println("Invalid, put a colon to separate!");
        
        
        System.out.println("Digite sua altura: ");
        altura = scanner.nextDouble();

        //counting genres
        if(sexo == 'F'){
            countFem++;
        } else if(sexo == 'M'){
            countMasc++;
        } else {
            System.out.println("ERROR: invalid type.");
            break;
        }

        //deciding the greater
        if (altura >= maiorAltura) {
            maiorAltura = altura;
        } else {
            System.out.println("");
            System.out.println(maiorAltura + " wins!");
        }

        //getting the sum
        soma += altura;   
    }
    //getting the average Height
    mediaAlturas = soma/numPessoas;

    System.out.println("A maior altura: " + String.format("%,2f", maiorAltura));
    System.out.println("O número de homens: " + countMasc);
    System.out.println("A média das alturas: " + String.format("%.2f", mediaAlturas));
  
  }
}
