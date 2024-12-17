import java.util.Arrays;

public class Intersection {

    public static void main(String[] args) {
        // Sample arrays
        int[] array1 = {4, 2, 7, 1, 9, 5};
        int[] array2 = {3, 7, 8, 2, 5};

        // Sort both arrays
        Arrays.sort(array1);
        Arrays.sort(array2);

        // Find the intersection of the two arrays
        int[] intersection = findIntersection(array1, array2);

        // Print the results
        System.out.println("Sorted Array 1: " + Arrays.toString(array1));
        System.out.println("Sorted Array 2: " + Arrays.toString(array2));
        System.out.println("Intersection: " + Arrays.toString(intersection));
    }

    public static int[] findIntersection(int[] arr1, int[] arr2) {
        // Initialize pointers and list for intersection
        int i = 0, j = 0;
        int[] tempIntersection = new int[Math.min(arr1.length, arr2.length)];
        int index = 0;

        // Iterate through both arrays
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] == arr2[j]) {
                // Add element to intersection
                if (index == 0 || tempIntersection[index - 1] != arr1[i]) {
                    tempIntersection[index++] = arr1[i];
                }
                i++;
                j++;
            } else if (arr1[i] < arr2[j]) {
                i++;
            } else {
                j++;
            }
        }

        // Copy intersection to exact size array
        int[] intersection = new int[index];
        System.arraycopy(tempIntersection, 0, intersection, 0, index);

        return intersection;
    }
}
