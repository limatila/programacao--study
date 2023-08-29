class exer01{
    public static void main(String[] args){

        //2.
        var nome = new String("Átila");
        System.out.println("Meu Nome É: " + nome);

        //3.
        System.out.println(28*43);

        //4.
        int myNums[] = {8,100,7}; //change only this

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

        //15.
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
    }
}