#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int adj[MAX][MAX], visited[MAX], stack[MAX], top = -1, n;

void push(int v) { stack[++top] = v; }

void dfs(int v) {
    visited[v] = 1;
    for (int i = 0; i < n; i++)
        if (adj[v][i] && !visited[i])
            dfs(i);
    push(v);
}

int main() {
    int edges, u, v;
    printf("Enter number of vertices: ");
    scanf("%d", &n);
    printf("Enter number of edges: ");
    scanf("%d", &edges);
    printf("Enter edges (u v) for each directed edge u -> v:\n");
    for (int i = 0; i < edges; i++) {
        scanf("%d %d", &u, &v);
        adj[u][v] = 1;
    }

    for (int i = 0; i < n; i++)
        if (!visited[i])
            dfs(i);
    printf("Topological Sort: ");
    for (int i = top; i >= 0; i--)
        printf("%d ", stack[i]);
    printf("\n");

    return 0;
}

