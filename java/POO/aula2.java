
//import classe apenas quando de outra pasta!

public class aula2 {
    public static void main(String[] args) {
        Pessoa pess1 = new Pessoa();
        pess1.mudarNome("Átila");
        pess1.mudarDataAniversario("16012005");
        pess1.mudarSexo("M");
        pess1.mudarCPF("12345678999");
        pess1.mudarNatalidade("Fortaleza");

        pess1.aumentarIdade(19);
        pess1.parabenizar();

        
        Pessoa pess2 = new Pessoa();
        pess2.mudarNome("Carlos");
        pess2.aumentarIdade(24);
        pess2.mudarDataAniversario("23022005"); //teste com a data atual!

        pess2.parabenizar();

        
        Pessoa pess_ultimo = new Pessoa();
        pess_ultimo.mudarNome("Nana");
        pess_ultimo.mudarDataAniversario("30122002");
        pess_ultimo.mudarNatalidade("Fortaleza");
        pess_ultimo.mudarSexo("F");
        pess_ultimo.aumentarIdade(20);


        System.out.println("");
        pess1.resumir();
        pess_ultimo.resumir();
    }
}
