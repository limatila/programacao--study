class Livro{
    private String titulo = "";
    private String autor = "";
    private int anoPublicado = 0;

    //constructor
    public Livro(String titulo, String autor, int anoPublicado){
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicado = anoPublicado;
    }

    //methods
    public void mostrarDetalhes(){
        System.out.println("\nTítulo: " + this.titulo +
                           "\nAutor: " + this.autor +
                           "\nAno de Publicação: " + this.anoPublicado);
    }
}

public class biblioteca{
    public static void main(String[] args) {
        Livro livro1 = new Livro("O Ceifador", "Neal Shusterman", 2016);
        livro1.mostrarDetalhes();
        
        Livro livro2 = new Livro("Percy Jackson", "Rick Riordan", 2005);
        livro2.mostrarDetalhes();

        Livro livro3 = new Livro("Maus", "Art Spiegelman", 1986);
        livro3.mostrarDetalhes();


        System.out.println("\nEND OF CODE");
    }
}