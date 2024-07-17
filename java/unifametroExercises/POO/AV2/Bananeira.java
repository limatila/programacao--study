public class Bananeira extends PlantaExotica{
    private int quantidadeFrutos; //Quantidade de cachos

    public Bananeira(String nome, int idade, double altura, String tipoFruta, int quantidadeFrutos){
        super(nome, idade, altura, tipoFruta);
        this.quantidadeFrutos = quantidadeFrutos;
    }

    //Métodos
    @Override
    public String resumir(){
        return "Bananeira:\n Nome: " + this.nome + "\n Idade: " + this.idade + 
        "\n Altura: " + this.altura + "\n Quantidade de Cachos de Banana: " + this.quantidadeFrutos +
        "\n Produção de Frutas: " + this.produzFruta();
    }

    //Getters
    public int getQuantidade(){
        return this.quantidadeFrutos;
    }

    //Setters
    public void setQuantidade(int quantidadeInserida){
        this.quantidadeFrutos = quantidadeInserida;
    }
    

}
