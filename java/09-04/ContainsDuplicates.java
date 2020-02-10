class ContainsDuplicates {
  public static void main(String args[]){
    int [] array = {1,2,3,3};
    test(array);
  }

  public static boolean test(int [] array){
    HashMap <Integer, Integer> map = new HashMap <Integer, Integer>();
    for (int i = 0; i < array.length; i++){
        if (!map.containsKey(array[i])){
            map.put(array[i], map.getKey() + 1);
        } else {
            map.put(array[i], 1);
        }
    }
    for (Integer int: map.keySet()){
        if(map.get(int) >= 2){
            return true; 
        }
    }
    return false;
  }

}
