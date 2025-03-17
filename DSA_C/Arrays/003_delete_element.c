#include <stdio.h>

int main(){
    int a[50], size, i, pos;
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    printf("Enter the elements of the array: ");
    for(i=0; i<size; i++)
        {
            scanf("%d", &a[i]);
        }

    printf("Enter the position: ");
    scanf("%d", &pos);
    if (pos<=0 || pos>size){
        printf("Invalid position");
    }
    else{
        for(i=pos-1; i<size-1; i++)
            {
                a[i] = a[i+1];
            }
        size--;

        // Traverse and print each element of the array
        printf("The elements of the array are: ");
        for(i=0; i<size; i++)
            {
                printf("%d ", a[i]);
            }
    }
    
}