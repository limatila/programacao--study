
public class CalculoAritmetico {
	public int divisao(int a, int b) throws DivisaoPorZeroExcepption{
		if (b == 0) { //estava aqui o erro...lesadaaaa
	            throw new DivisaoPorZeroExcepption();
	        }
	    return a / b;
	}
}
