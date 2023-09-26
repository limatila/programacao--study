class first{
    public static void main(String[] args){

        int a = 1;		//ALWAYS declare type of var
        System.out.println(a);

        int b = 55;

        int myIterable[] = {a, b};
		
        for(int i = 0; i<myIterable.length; i++){
            System.out.println("this variable: " + myIterable[i]); 
        };

    }
}
