public class mapping{
    Map<Integer, String> map = new HashMap<Integer, String>();
    map.put(1, "Átila");
    map.put(5, "Gabu");
    map.put(6, "Well");
    
    public static void main(String[] args){
        for(int i = 0; i < map.size; i++){
            if(this.map.get(i) == null){ continue; }
            System.out.println(this.map.get(i));
        }
        
    }
    
}