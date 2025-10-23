#include <stdio.h>

int main() {
    int arr[100], n, i, pos, value;

    // Step 1: Input number of elements
    printf("Enter number of elements: ");
    scanf("%d", &n);

    // Step 2: Input array elements
    printf("Enter %d elements:\n", n);
    for(i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // Step 3: Traverse (Display)
    printf("\nArray elements: ");
    for(i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Step 4: Insert an element
    printf("\nEnter position to insert (0 to %d): ", n);
    scanf("%d", &pos);
    printf("Enter value to insert: ");
    scanf("%d", &value);

    if(pos >= 0 && pos <= n) {
        for(i = n; i > pos; i--) {
            arr[i] = arr[i - 1];
        }
        arr[pos] = value;
        n++;
    } else {
        printf("Invalid position for insertion.\n");
    }

    // Step 5: Display after insertion
    printf("\nArray after insertion: ");
    for(i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Step 6: Delete an element
    printf("\nEnter position to delete (0 to %d): ", n - 1);
    scanf("%d", &pos);

    if(pos >= 0 && pos < n) {
        for(i = pos; i < n - 1; i++) {
            arr[i] = arr[i + 1];
        }
        n--;
    } else {
        printf("Invalid position for deletion.\n");
    }

    // Step 7: Display after deletion
    printf("\nArray after deletion: ");
    for(i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Step 8: Search for a value
    printf("\nEnter value to search: ");
    scanf("%d", &value);
    int found = 0;
    for(i = 0; i < n; i++) {
        if(arr[i] == value) {
            printf("Value found at index %d\n", i);
            found = 1;
            break;
        }
    }
    if(!found) {
        printf("Value not found in the array.\n");
    }

    return 0;
}

