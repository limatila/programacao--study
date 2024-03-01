
import java.text.SimpleDateFormat;
import java.util.Calendar;

class Pessoa {
    //atributos -- geralmente privados, acessados sempre por um método!
    private String Nome = "";
    private int idade = 0;
    private char sexo = 'N';
    private String dataAniversario = "";
    private String anoNascimento = "";
    private String natalidade = "";
    private String CPF = "0"; 


    //setters -- melhor usar um constructor
    public void mudarNome(String nomeInserido){ //precisa especificar que tipo é o Arg recebido.
        this.Nome = nomeInserido;
    }
    public void mudarDataAniversario(String anivInserido){ //inserir 'ddmmyyyy'
        String anoAniv = anivInserido.substring(4);
        String dia_mesAniv = anivInserido.substring(0,4);
        
        this.dataAniversario = dia_mesAniv;
        this.anoNascimento = anoAniv;
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
    public String descreverSexo(){
        return sexo == 'M' ? "Homem" : sexo == 'F' ? "Mulher" : "NULL";
    }

    public void resumir(){
        System.out.println("A pessoa referida tem nome " + this.Nome + ", tem "+ this.idade 
        + " anos de idade, e é " + descreverSexo() + ". Nasceu em " + this.natalidade
        + ". Sua data de nascimento é " + (this.dataAniversario.concat(this.anoNascimento + "."))); //! formatar melhor!
    }

    public boolean fazAniversario(){ //pode ser usado pra vários propósitos: polimorfismo.
        String dataGerada = new SimpleDateFormat("ddMM").format(Calendar.getInstance().getTime());
        return dataGerada.equals(dataAniversario);
    }
    
    public void aumentarIdade(int maisIdade){
        idade += maisIdade;
    }

    public void parabenizar(){  //abstração, uma camada maior de lógica que possui um objetivo final definido.
        if(this.fazAniversario() == true){
            aumentarIdade(1);
            System.out.println("Parabens " + this.Nome + "!!!");
        } else {
            String dataGerada2 = new SimpleDateFormat("ddMM").format(Calendar.getInstance().getTime()).substring(2, 4);
            String dataAnivReduzida = this.dataAniversario.substring(2, 4);
            int mesesFaltando = (Integer.parseInt(dataGerada2) - Integer.parseInt(dataAnivReduzida)); //*String para Int!
            System.out.println("Ainda faltam mais ou menos " + mesesFaltando + " meses para o seu aniversário, " + this.Nome + "."); //!não leva em conta os dias
        }
    }
    
    //?API: como checar o CPF?


    //*getters... nao necessario agora

};
