public class diaDeEmpresa {
    public static void main(String[] args) throws Exception {
        //Superclasse
        Funcionario pess1 = new Funcionario("Atila", "99999999999", 1250, 
                                            true);
        Funcionario pess2 = new Funcionario("Marcela", "12375395120", 4560.87, 
                                            true);

        //Subclasse
        Gerente manager_1 = new Gerente("Adoniran", "11111111111", 8937.20,
                                        true, "327589ac");


        System.out.println(pess1.ativo);
        System.out.println(pess2.ativo);

        System.out.println("");
        manager_1.logar("327589ac");
        manager_1.demitirFuncionario(pess1);
        
        pess1.trabalha();
    }
}
