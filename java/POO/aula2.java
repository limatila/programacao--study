
//import classe apenas quando de outra pasta!

public class aula2 {
    public static void main(String[] args) {
        Pessoa pess1 = new Pessoa();
        pess1.mudarNome("Átila");
        pess1.mudarDataAniversario("1602");
        pess1.mudarSexo("M");
        pess1.mudarCPF("12345678999");
        pess1.mudarNatalidade("Fortaleza");

        pess1.aumentarIdade(19);
        pess1.parabenizar();

        
        Pessoa pess2 = new Pessoa();
        pess2.mudarNome("Carlos");
        pess2.aumentarIdade(24);
        pess2.mudarDataAniversario("2202");

        pess2.parabenizar();
    }
}
