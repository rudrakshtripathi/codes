public class Maxarray {
    public static void main(String[] args) {
        int[] arr= {1,2,3,4,5,66,7,98,58,68,210,75,052,2454};
        maxval(arr);
        System.out.println(maxval(arr));
    }
    static int maxval(int[] arr){
       int maxx=arr[0];
        for (int i = 0; i < arr.length; i++) {
            if(arr[i]>maxx){
                maxx=arr[i];
            }   
        }
        return maxx;
    }
}
