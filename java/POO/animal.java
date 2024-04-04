class Animal {
    private String nome;
    private int idade;
    private String tipo;
    private double peso; //Kilos!

    //*Construtor: inicializa como quando a classe de mesmo nome é inicializada. Só pode ser do mesmo nome da classe, e não é método!
    public Animal(String nome, int idade, String tipo, Double peso){
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
        this.peso = peso;
    }

    public String getTodos(){
        String strOut = "Esse animal se chama " + this.nome + ", tem " + this.idade + " anos, é "
        + this.tipo + ", e pesa " + this.peso + "Kgs. Esses são todos os dados.";
        return strOut;
    }

    //calcular quantos gramas o animal come na vida dele.
    public String calcularConsumoAlimento() throws Exception{
        double consumoTotal;
        switch ( this.tipo.toLowerCase() ) {
            case "mamifero": {
                double mediaConsumo = 2000;
                consumoTotal = (365*idade*mediaConsumo);
                String resumoConsumo = ("Durante sua vida, " + this.nome + " consumiu " + (consumoTotal/1000) + "Kgs de alimento.");
                return resumoConsumo;
            }
            case "ave": {
                double mediaConsumo = 100;
                consumoTotal = (365*idade*mediaConsumo); 
                String resumoConsumo = ("Durante sua vida, " + this.nome + " consumiu " + (consumoTotal/1000) + "Kgs de alimento.");
                return resumoConsumo;
            }
            case "peixe": {
                double mediaConsumo = 20;
                consumoTotal = (365*idade*mediaConsumo);
                String resumoConsumo = ("Durante sua vida, " + this.nome + " consumiu " + (consumoTotal/1000) + "Kgs de alimento.");
                return resumoConsumo;
            }

            default:
                throw new Exception("Erro: tipo de animal indefinido!");
                //*break não necessário: o erro já para!
        }
    }
}