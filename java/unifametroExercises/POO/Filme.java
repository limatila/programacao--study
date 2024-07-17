class Filme {
    private String titulo = "";
    private double tempo = 0; //minutos

    //setters
    public void setTitulo(String novoTitulo){
        this.titulo = novoTitulo;
    }
    public void setTempo(double novoTempo){
        this.tempo = novoTempo;
    }

    //constructor
    Filme(String titulo, double tempo){
        this.titulo = titulo;
        this.tempo = tempo;

        System.out.println("Construtor de filme concluído.");
    }

    //getters
    public String getTitulo(){
        return this.titulo;
    }
    public double getTempo(){
        return this.tempo;
    }

    public double tempoEmHoras(){
        int horas = (int) this.tempo/60;
        int minutos 
        
        return int
    }

    public static void main(String[] args) {
        Filme filme1 = new Filme("Mary and Max", 100);

        System.out.println(filme1.tempoEmHoras());
    }
}