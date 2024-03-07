class Apolice{
    private String nomePessoa;
    private int idadePessoa;
    private double valorPremio;

    public Apolice(String nomePessoa, int idadePessoa, double valorPremio){
        this.nomePessoa = nomePessoa;
        this.idadePessoa = idadePessoa;
        this.valorPremio = valorPremio;
    }

    public void imprimir(){ //resumo
        System.out.println("\nO nome do segurado é: " + this.nomePessoa +
                           "\nA idade do segurado é: " + this.idadePessoa +
                           "\nO valor-prêmio da apólice é: " + this.valorPremio);
    }

    public void calcularPremioApolice(){
            if(this.idadePessoa >= 18 && this.idadePessoa <= 25){
                this.valorPremio += (this.valorPremio/100)*20;
            } else if (this.idadePessoa >= 26 && this.idadePessoa <= 36){
                this.valorPremio += (this.valorPremio/100)*15;
            } else if (this.idadePessoa > 36){
                this.valorPremio += (this.valorPremio/100)*10;
            }
    }

    public void oferecerDesconto(String cidade){
        switch ( cidade.toLowerCase() ) {
            case "curitiba":
                this.valorPremio -= (this.valorPremio/100)*20;
                break;

            case "rio de janeiro":
                this.valorPremio -= (this.valorPremio/100)*15;
                break;
            
            case "são paulo":
                this.valorPremio -= (this.valorPremio/100)*10;
                break;

            case "belo horizonte":
                this.valorPremio -= (this.valorPremio/100)*5;
                break;
        }
    }
}




public class seguro { //ApoliceTeste no pdf
    public static void main(String[] args) {
        Apolice pess1 = new Apolice("Átila", 19, 3500);
        Apolice pess2 = new Apolice("Joana", 29, 14600);

        pess1.calcularPremioApolice();
        pess2.oferecerDesconto("Rio de Janeiro");

        pess1.imprimir(); System.out.println("");
        pess2.imprimir();

    }
}
