#include <stdio.h>

#define MAX 100

int queue[MAX], front = 0, rear = 0;

void enqueue(int v) { queue[rear++] = v; }

int dequeue() { return queue[front++]; }

int isEmpty() { return front == rear; }

int main() {
    int n, start;
    int graph[MAX][MAX], visited[MAX] = {0};

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&graph[i][j]);

    printf("Enter starting vertex: ");
    scanf("%d",&start);

    enqueue(start);
    visited[start] = 1;
    printf("BFS Traversal: ");

    while(!isEmpty()) {
        int node = dequeue();
        printf("%d ", node);
        for(int i=0;i<n;i++) {
            if(graph[node][i] && !visited[i]) {
                enqueue(i);
                visited[i] = 1;
            }
        }
    }
    printf("\n");
    return 0;
}

