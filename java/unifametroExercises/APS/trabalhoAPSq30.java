package APS;

import java.util.Scanner;
import java.util.Locale;

class qtrinta {
    public static void main(String[] args) {
        //q 30.
        Scanner scanner = new Scanner(System.in);

        String nome = "", sexo, msgAceito = "Próxima criança...";
        int numFilhos, idadeInput,
            bebes = 0,
            preAdolescentesM = 0, preAdolescentesF = 0; //bebes: menos de 5; preAdolescentes: {5, 12};
        double valorBola = 1.45, valorCarrinho = 2.50, valorBoneca = 3.00, valorTotal; //preços dos brinquedos
        //menores de 5 recebem Bola; maiores recebem Carrinho ou Boneca (M/F)

        System.out.println("O programa a seguir irá calcular quanto deverá ser investido para a campanha de Natal.");
        System.out.println("Insira 'vazio' no campo 'nome' para terminar a execução!");
	System.out.println("");

        while ( nome != "VAZIO" ){

            System.out.print("Insira o nome do funcionário\t=>");
            nome = scanner.next().toUpperCase();
            if (nome.contains("VAZIO")) {
                break;
            }
            System.out.print("Insira o número de filhos com menos de 12 anos\t=>");
            numFilhos = scanner.nextInt();
	    System.out.println("");

            for(int i = 0; i < numFilhos; i++){
                
                System.out.print("Insira a idade da "+ (i+1) +"° criança(até 12 anos)\t=>");
                idadeInput = scanner.nextInt();
                
                if(idadeInput < 5){
                    bebes++;
                    System.out.println(msgAceito);
                } else if(idadeInput >= 5 && idadeInput <= 12){
                    System.out.print("Insira o sexo da criança(M/F)\t=>");
                    sexo = scanner.next().toUpperCase();
                    if (sexo.charAt(0) == 'M'){
                        preAdolescentesM++;
                    } else if (sexo.charAt(0) == 'F'){
                        preAdolescentesF++;
                    } else {
                        System.out.println("Sexo mal inserido, digite novamente os dados...");
                        i -= 1;
                    }  
                    System.out.println(msgAceito);
                } else {
                    System.err.println("Idade mal inserida, digite novamente os dados..."); 
                    i -= 1;
                }
            }
            
            System.out.println("\nPróximo funcionário...:");
        }

        valorTotal = (bebes*valorBola + preAdolescentesM*valorCarrinho + preAdolescentesF*valorBoneca);
	System.out.println("");
        System.out.println("O valor total investido deve ser de R$" + String.format("%.2f", valorTotal));
        
        System.out.println("Terminando o programa...");
    }
}