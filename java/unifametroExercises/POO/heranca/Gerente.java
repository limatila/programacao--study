class Gerente extends Funcionario{
    private String senha = "";
    private Boolean online = (Boolean) null;

    Gerente(String nome, String CPF, double salario, boolean ativo, String senha) { //O construtor DEVE ser redefinido para a nova classe
        super(nome, CPF, salario, ativo); //super recebe atributos da superclasse
        this.senha = senha;
    }
    
    private boolean autentica(String senhaInserida) throws Exception{
        if (!ativo) {
            throw new Exception("Usuário não ativo.");
        }
        
        if (senhaInserida == senha) {
            System.out.println("Correta.");
            return true;
        } else {
            System.out.println("Errado, tente novamente.");
            return false;
        }

    }

    public void logar(String senhaInsert) throws Exception{ //QUALQUER método em que um erro passar deve ser especificado que pode fazê-lo. !ATÉ na Main!
        if( autentica(senhaInsert) ){
            this.online = true;
        } else {
            throw new Exception("Login falhou! tente novamente.");
        }
    }

    public void demitirFuncionario(Funcionario funci) throws Exception{ //O tipo do arg deve ser especificado. Como é subclasse, 'Gerente' também é aceito!
        if (!online) {
            throw new Exception("O Gerente deve estar logado e autenticado.");
        }

        if (funci.ativo == true) {  //!Precisa checar se é SOMENTE funcionario.
            funci.ativo = false;
            System.out.println("Feito.");
        } else {
            System.out.println("Funcionário não é ativo.");
        }
    }

    //só outro de cargo superior deve ativar o gerente, e no caso esse não deve ter 'ativo'.
}
