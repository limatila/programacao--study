class Funcionario {
    private String nome = "";
    private String CPF = "0"; //11 numeros
    private double salario = 0;
    public Boolean ativo = (Boolean) null;

    Funcionario(String nome, String cPF2, double salario, boolean ativo){
        this.nome = nome;
        this.CPF = cPF2;
        this.salario = salario;
        this.ativo = ativo;
    }

    public void trabalha(){
        if(!ativo){ System.out.println("Funcionário não ativo. Não mais vinculado à empresa!"); 
        } else { System.out.println("Trabalhando..."); }

        
    }
}