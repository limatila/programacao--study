
public class Principal {
	public static void main(String[] args) {
		CalculoAritmetico calc = new CalculoAritmetico();
		try {
			calc.divisao(10, 0);
		} catch (DivisaoPorZeroExcepption e) {
			System.out.println("Teste");
			System.out.println(e.getMessage());
		}
	}
}
