#include<stdio.h>
int main()
{
int arr[100];
int n,i,pos;
printf("enter number of elents(<=100): ");
scanf("%d",&n);
printf("enter %d elements: \n",n);
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}
printf("enter position to delete(1 to %d):",n);
scanf("%d",&pos);
if(pos<1||pos>n)
{
printf("invalid position!\n");
}
else
{
for(i=pos-1;i<n-1;i++)
{
arr[i]=arr[i+1];
}
n--;
printf("array after deletion: ");
for(i=0;i<n;i++)
{
printf("%d",arr[i]);
}
return 0;
}
}

