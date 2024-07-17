package POO;

class lampada {
    public String marca = "enel";
    public int voltagem = 20;
    public String tipo = "C";
    public String modelo = "EB23";
    public String cor = "branca";
    public int garantia = 8; //em meses
    public double preço = 8.99;

    public void ligar(){
        System.out.println("Lâmpada ligada.");
    }
    public void desligar(){
        System.out.println("Lâmpada desligada.");
    }

    public void getGarantia(){
        System.out.println("Esta lâmpada possui " + garantia + " meses de garantia.");
    }
}

public class aula1 {
    public static void main(String[] args){
        int a = 2;
        System.out.println("tenho "+ a +" bananas");

        lampada lamp = new lampada();
        lamp.desligar();
        
        lamp.getGarantia();
    }
}

