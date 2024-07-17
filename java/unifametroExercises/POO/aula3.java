import java.text.SimpleDateFormat;
import java.util.Calendar;

class Aluno{
    private String nome;
    private int idade;
    private String curso;
    private int anoIngresso;
    private int qtdDisciplinasAprov;

    public Aluno(String nome, int idade, String curso, int anoIngresso, int qtdDisciplinasAprov){
        this.nome = nome;
        this.idade = idade;
        this.curso = curso;
        this.anoIngresso = anoIngresso;
        this.qtdDisciplinasAprov = qtdDisciplinasAprov;
    }

    public void tempoIngressado(){
        int anoAtual = Integer.parseInt(new SimpleDateFormat("YYYY").format(Calendar.getInstance().getTime()));
        int tempoTotal = anoAtual - this.anoIngresso;
        System.out.println(tempoTotal);
    }
}

public class aula3 {
    public static void main(String[] args) throws Exception {
        Animal Dog = new Animal("Loki", 6, "mamifero", 6.1);
        System.out.println(Dog.calcularConsumoAlimento());
        System.out.println(Dog.getTodos());

        System.out.println("");
        Animal Eagle = new Animal("Careca", 6, "avE", 5.2);
        System.out.println(Eagle.calcularConsumoAlimento());

        System.out.println("");
        Animal Glofish = new Animal("Yli", 1, "peixe", 0.6);
        System.out.println(Glofish.calcularConsumoAlimento());

        System.out.println("");
        Animal Humano = new Animal("Átila", 19, "Mamifero", 77.5);
        System.out.println(Humano.calcularConsumoAlimento());

        System.out.println("\n\nAlunos-------------------");
        Aluno aluno1 = new Aluno("Matheus", 19, "medicina", 2022, 16);
        Aluno aluno2 = new Aluno("Alceu", 51, "SMD", 2023, 5);

        
    }
}
