

/* Esta classe deve ser abstrata pelo motivo de que 'Planta'
 * representa um conjunto muito geral de um objeto.
 * ao criar as classes filhas com nomes das plantas,
 * se dá mais ênfase de que se trata de algo específico
 * e com propósito bem definido.
 * 
 * A classe abstrata serve definir uma ideia geral que em seguida
 * será implementada especificamente.
 */

 /* Sobre o encapsulamento, todos os atributos específicos são
  * mantidos como private para evitar uma modificação crua deles,
  * e protected para os métodos declarados de classes derivadas 
  * que queiram usar os atributos da classe pai.
  * Os métodos todos estão públicos porque é esperado que o Usuário
  * utilize eles, para acessar as informações dos objetos criados. 
  * 
  * Não há nenhum método que deveria ser impossibilitado de ser usado,
  * ou que só deveria ser executado como parte de outros métodos,
  * esses tendo de serem publicos para serem executados pelo Usuário.
  */

public abstract class PlantaExotica{
    protected String nome;
    protected int idade; //meses
    protected double altura; //metros

    protected String tipoFruta; //para o método 'produzFruta()'

    public PlantaExotica(String nome, int idade, double altura, String tipoFruta){
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;
        this.tipoFruta = tipoFruta;
    }

    //Métodos
    public String produzFruta(){
        return this.tipoFruta;
    }

    public abstract String resumir();

    //Getters
    public double getAltura() {
        return altura;
    }
    public int getIdade() {
        return idade;
    }
    public String getNome() {
        return nome;
    }
    
    //Setters
    public void setAltura(double altura) {
        this.altura = altura;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setTipoFruta(String tipoInserido){
        this.tipoFruta = tipoInserido;
    }
} 