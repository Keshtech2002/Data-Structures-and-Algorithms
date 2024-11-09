#include <stdio.h>

int main(){
    int a[50], size, i, pos, num;
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    printf("Enter the elements of the array: ");
    for(i=0; i<size; i++)
        {
            scanf("%d", &a[i]);
        }

    printf("Enter data to be inserted: ");
    scanf("%d", &num);
    printf("Enter the position: ");
    scanf("%d", &pos);

    //Inserting in array
    if(pos<=0 || pos>size){
        printf("Invalid position");
    }
    else{
        for(i=size-1; i>=pos-1; i--)
            {
                a[i+1] = a[i];
            }
        a[pos-1] = num;
        size++;
    }
}