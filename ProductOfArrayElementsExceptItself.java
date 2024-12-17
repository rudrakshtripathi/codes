public class ProductOfArrayElementsExceptItself {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        int[] output = productExceptSelf(nums);
        System.out.println(java.util.Arrays.toString(output));
    }

    static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];

        // calculate product of all numbers to the left of each index
        int leftProduct = 1;
        for (int i = 0; i < n; i++) {
            output[i] = leftProduct;
            leftProduct *= nums[i];
        }

        // calculate product of all numbers to the right of each index
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return output;
    }
}