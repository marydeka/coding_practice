//It's better to use an ArrayList for this problem, but I wanted to try it
//using an array, too. But using [i - 1] to take care of the 0th element feels clunky.
//Maybe another option is setting the first element (0th) to null. 

class FizzBuzz {
  public static void main(String args[]){
    int n = 20;
    test(n);
  }

  public static String [] test(int n){
    String [] results = new String [n];
    for(int i = 1; i <= n; i++){
      if (i % 3 == 0 && i % 5 == 0){
        results[i - 1] = "fizzbuzz";
      } else if (i % 3 == 0){
        results[i - 1] = "fizz";
      } else if (i % 5 == 0){
        results[i - 1] = "buzz";
      } else{
        results[i - 1] = Integer.toString(i);
      }
    }
    for(int i = 0; i < n; i++){
      System.out.println(results[i]);
    }
    return results;
  }
}