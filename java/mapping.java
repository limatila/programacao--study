import java.util.HashMap;
import java.util.Map;

public class mapping{
    public static void main(String[] args){
        Map<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "Átila");
        map.put(5, "Gabu");
        map.put(6, "Well");

        for(int i = 0; i < 7; i++){
            if(map.get(i) == null){ continue; } //Complexier then forEach style
            System.out.println(map.get(i));
        }
        
    }
    
}