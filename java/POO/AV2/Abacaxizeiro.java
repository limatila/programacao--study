public class Abacaxizeiro extends PlantaExotica {
    double pesoAbacaxi; //Peso médio de um, em Kg

    public Abacaxizeiro(String nome, int idade, double altura, String tipoFruta, double pesoAbacaxi){
        super(nome, idade, altura, tipoFruta);
        this.pesoAbacaxi = pesoAbacaxi;
    }

    //Métodos
    @Override
    public String resumir(){
        return "Abacaxizeiro:\n Nome: " + this.nome + "\n Idade: " + this.idade + 
        "\n Altura: " + this.altura + "\n Peso Médio dos Abacaxis: " + this.pesoAbacaxi +
        "\n Produção de Frutas: " + this.produzFruta();
    }

    //Getters
    public double getPeso(){
        return this.pesoAbacaxi;
    }

    //Setters
    public void setPeso(double pesoInserido){
        this.pesoAbacaxi = pesoInserido;
    }

}
