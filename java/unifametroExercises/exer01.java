package unifametroExercises;
import java.util.Scanner;
import java.util.Arrays;

class exer01{
    public static void main(String[] args){
        
        Scanner scanner = new Scanner(System.in); //creating scanner for futute use

        //2.
        var nome = new String("Átila");
        System.out.println("Meu Nome É: " + nome);

        //3.
        System.out.println(28*43);

        //4.
        int myNums[] = {8,100,64}; //change only this

        double soma = 0;
        double media = 0;
        int i = 0;

        while (i < myNums.length) {
            soma += myNums[i];
            i++;
        };

        media = soma/myNums.length;
        System.out.println("A média é: "+ media);
            
        //5 ou 6.
        System.out.println("numero 1: "+ myNums[0] + "; numero 2: "+ myNums[1] +";");

        //7.
        System.out.println("numero 1: "+ (myNums[2]+1) + "; numero 2: "+ (myNums[2]-1) +";");

        //8.
        var email = "atilalimade@gmail.com";
        int telefone = 32238142;

        System.out.println("nome: "+nome+ "; email: "+email+ "; telefone: " + telefone+";");

        //9.
        int num1 = 1; int num2 = 10;
        System.out.println("Soma: " + (num1 + num2));

        //11.
        System.out.println("the third rounded part of num2 is " + num2/3);

        //10.
        System.out.println("multiplying num1 * num2" + num1 * num2);

        //12.
        double nota1 = 8.6;
        double nota2 = 5.8;
        double media1 = (nota1+nota2)/2;
        System.out.println("Nova Média" + media1);

        //13.
        int divisor = 10;
        int dividendo = 73;
        double quociente = dividendo/divisor;
        int resto = dividendo%divisor;

        System.out.println("------------");
                System.out.println("divisor: "+ divisor + "\ndividendo: " + dividendo + "\nquociente: " + quociente + "\nresto: " + resto);
        System.out.println("------------");

        //14.
        double nota3 = 3.8;
        double nota4 = 9.0;
        double mediaPonderada = (nota1 + (nota2*2) + (nota3*3) + (nota4*4))/10;
        System.out.println("A Média Ponderada é: " + mediaPonderada);


        //15. select angle and show trigonometric notations
        float angulo = 30;
        double seno = Math.sin(angulo);
        double cosSeno = Math.cos(angulo);
        double tangente = Math.tan(angulo);
        double secante = 1/cosSeno;
        double coSecante = 1/seno;
        double coTangente = cosSeno/seno;

        System.out.println("--------------");
            System.out.println("Meu ângulo: " + angulo + "\nSeno dele: " + seno + "\nCosseno dele: " + cosSeno + "\nTangente dele: " + tangente + "\nSecante: " + secante
            + "\nCossecante: " + coSecante + "\nCotangente: " + coTangente);
        System.out.println("--------------");


        //16.
        double Logaritm = Math.log10(myNums[0]);
        System.out.println(Logaritm);

        //17.
        System.out.println("número: " + myNums[2]);
        System.out.println("raíz quadrada: " + (int) Math.sqrt(myNums[2])); //se possível após método, converter em Int. 
        System.out.println("elevado a 2: " + (int) Math.pow(myNums[2], 2));
    
        //18.
        double dolar = 4.93; //em 12/09/23
        double newDolar = (dolar/100) + dolar;
        var newDolarFormatted = String.format("%.2f", newDolar);
        System.out.println("o Dolar estava a " + dolar + ", sofreu um aumento e custa agora: "+ newDolarFormatted);

        //19. inverter um int?

        //20.
        double salarioMinimo = 1320;
        double valorKW = (salarioMinimo/7)/100;
        int usoEnergia = 157; //157kw/home in general in brazil
        double fatura = valorKW * usoEnergia;
        double faturaDescontada = fatura - (fatura/10);
        
        System.out.println("preço do kilawatt é: " + valorKW);

        var faturaFormatted = String.format("%.2f", (fatura)); //formatting for better visualizing 
        var descontadaFormatted = String.format("%.2f", faturaDescontada);
        System.out.println("o valor total a pagar é de " + faturaFormatted + ", e em alguns casos há um desconto, totalizando: " + descontadaFormatted);

        //21.
        System.out.println("digite seu nome: ");
        String nameScanned = scanner.nextLine();
        String duasLetras[] = {String.valueOf(nameScanned.charAt(0)), String.valueOf(nameScanned.charAt(nameScanned.length() - 1))};

        System.out.println("Olá " + nameScanned + ". Sua inicial e sua final são " + Arrays.toString(duasLetras));
        System.out.println("Suas primeiras três letras são: " + nameScanned.substring(0, 3));
        System.out.println("Logo após, a quarta letra: " + nameScanned.charAt(3));
        System.out.println("Todos menos a inicial: " + nameScanned.substring(1, nameScanned.length()));
        System.out.println("Últimas duas letras: " + nameScanned.substring(nameScanned.length() - 2, nameScanned.length()));

        //22.
        System.out.println("Insira uma base (inteiro) para um retângulo : ");
        int base = scanner.nextInt();
        System.out.println("Insira agora uma altura: ");
        int altura = scanner.nextInt();

        System.out.println("Sua área é: " + base * altura);
        System.out.println("Seu perímetro é " + (base * 2 + altura * 2));
        System.out.println("Sua diagonal é aproximadamente " + 
                            String.format("%.2f", 
                            Math.sqrt(Math.pow(base, 2) + Math.pow(altura, 2))
                                )
                            );

    }
}
