import java.lang.Math;
import java.util.HashMap;

class FindMatch {
    public static void main(String args[]){
        int [] nums = {1,2,3,1};
        int k = 3;
        System.out.println(findMatch(nums, k));
    }

    public static boolean findMatch(int [] nums, int k){
        //System.out.println("entered function");
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            //System.out.println(i);
            if(map.containsKey(nums[i]) && i - map.get(nums[i]) <= k){
                return true;
            } else{
                map.put(nums[i], i);
            }
        }
        return false;
    }
}