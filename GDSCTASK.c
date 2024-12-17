#include <stdio.h>
// Function to find the maximum and minimum elements in an array
void findMinMax(int arr[], int size, int *max, int *min) {
 if (size <= 0) {
 printf("Invalid array size.\n");
 return;
 }
 *max = *min = arr[0];
 for (int i = 1; i < size; i++) {
 if (arr[i] > *max) {
 *max = arr[i];
 }
 if (arr[i] < *min) {
 *min = arr[i];
 }
 }
}
int main() {
 int size;
 printf("Enter the size of the array: ");
 scanf("%d", &size);
 if (size <= 0) {
 printf("Invalid array size.\n");
 return 1;
 }
 int arr[size];
 printf("Enter %d integers:\n", size);
 for (int i = 0; i < size; i++) {
 scanf("%d", &arr[i]);
 }
 int max, min;
 findMinMax(arr, size, &max, &min);
 printf("Maximum element: %d\n", max);
 printf("Minimum element: %d\n", min);
 return 0;
}
 



int findMinMax(int arr[], int size, int *min, int *max) {
// Check if array size is zero or negative
    if (size <= 0) {
// Return -1 to indicate failure
        return -1;

}

}


void findMinMaxOptimized(int arr[], int size, int *min, int *max) {
// Early exit if array size is small
if (size <= 0) {
    return;
}
*min = *max = arr[0];
// Parallelization can be applied here
for (int i = 1; i < size; i++) {
    *min = (arr[i] < *min) ? arr[i] *min;
    *max = (arr[i] > *max) ? arr[i]: *max;
    }
}
