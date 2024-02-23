
import java.text.SimpleDateFormat;
import java.util.Calendar;

class Pessoa {
    private String Nome = "";
    private int idade = 0;
    private char sexo = 'N';
    private String dataAniversario = "";
    private String natalidade = "";
    private String CPF = "0"; 

    //setters
    public void mudarNome(String nomeInserido){
        this.Nome = nomeInserido;
    }
    public void mudarDataAniversario(String anivInserido){
        this.dataAniversario = anivInserido;
    }
    public void mudarNatalidade(String cidadeInserida){
        this.natalidade = cidadeInserida;
    }
    public void mudarCPF(String cpfInserido){
        this.CPF = cpfInserido;
    }
    public void mudarSexo(String sexoInserido){
        this.sexo = sexoInserido.toUpperCase().charAt(0);
    }


    //funcionais
    public boolean fazAniversario(){
        String dataGerada = new SimpleDateFormat("ddMM").format(Calendar.getInstance().getTime());
        return dataGerada == dataAniversario;
    }
    
    public void aumentarIdade(int maisIdade){
        idade += maisIdade;
    }

    public void parabenizar(){
        if(fazAniversario() == true){
            aumentarIdade(1);
            System.out.println("Parabens " + this.Nome + "!!!");
        } else {
            String dataGerada2 = new SimpleDateFormat("ddMM").format(Calendar.getInstance().getTime()).substring(2, 4);
            String dataAnivReduzida = this.dataAniversario.substring(2, 4);
            int mesesFaltando = (Integer.parseInt(dataGerada2) - Integer.parseInt(dataAnivReduzida));
            System.out.println("Ainda faltam " + mesesFaltando + " meses para o seu aniversário, " + this.Nome + ".");
        }
    }
    
    //?API: como checar o CPF?


    //*getters... nao necessario agora

};
