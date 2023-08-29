class Main{
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
        System.out.println(media);
            
        //5 ou 6.
        System.out.println("numero 1: "+ myNums[0] + "; numero 2: "+ myNums[1] +";");

        //7.
        System.out.println("numero 1: "+ (myNums[2]+1) + "; numero 2: "+ (myNums[2]-1) +";");

        //8.
        var email = "atilalimade@gmail.com";
        int telefone = 32238142;

        System.out.println("nome: "+nome+ "; email: "+email+ "; telefone: " + telefone+";");

        //9.
        int num1 = 1; int num2 = 10
        System.out.println("Soma: " + (num1 = num2));

        //10.
        

        
    }
}