class FindMinMax {
  public static void main(String args[]){
    int [] A = {2, 5, 1, 3};
    test(A);
  }

  public static int[] test(int [] A){
    //I will initialize an array of length 2 to hold the min and max value
    int [] minMax = new int[2];

    //the item stored at index 0 is the min, and index 1 is max
    minMax[0] = A[0];
    minMax[1] = A[1];

    //iterate through the array, comparing each item to min and max
    for(int i = 1; i < A.length; i++){
      if(A[i] < minMax[0]){
        minMax[0] = A[i];
      }
      if(A[i] > minMax[1]){
        minMax[1] = A[i];
      }
    }
    // System.out.println(minMax.toString());
    for(int element: minMax){
      System.out.print(element + " ");
    }
    System.out.println();
    return minMax;
  }
}