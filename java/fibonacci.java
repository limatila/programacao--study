class Program{
    public static void main(String[] args){
    
    int fib[] = {1, 1};
    
    for (var i = 0; i<10; i++) {
        int x = fib[i] + fib[i+1];
        fib.append(x); //will not append? find the right method.

    };
    
    System.out.println(fib);

    }
}