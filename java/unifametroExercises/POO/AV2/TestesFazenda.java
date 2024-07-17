// Sem unit test no momento
public class TestesFazenda {
    public static void main (String []args){
        Bananeira banana = new Bananeira("Bananeira prateada", 18, 2.5, "Produzindo bananas prateadas", 10);
        Abacaxizeiro abacaxi = new Abacaxizeiro("Abacaxizeiro Dourado", 24, 1.8, "Está produzindo abacaxis dourados maduros", 5.5);

        System.out.println(banana.resumir());
        System.out.println(abacaxi.resumir());
    }
}
