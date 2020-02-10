import java.util.Arrays;



class FindNew {
    public static void main(String args[]){
        String s = "atacbe";
        String t = "eabatcd";
        System.out.println(findNew(s, t));
    }

    public static char findNew(String s, String t){
        char [] orig = s.toCharArray();
        char [] shuffled = t.toCharArray();
        Arrays.sort(orig);
        Arrays.sort(shuffled);

        for(int i = 0; i < orig.length; i++){
            if(orig[i] != shuffled[i]){
                return shuffled[i];
            }
        }
        return shuffled[shuffled.length - 1];
    }
}