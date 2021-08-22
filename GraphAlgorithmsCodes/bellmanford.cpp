#include <bits/stdc++.h>
#include "edge.hpp"

using namespace std;

const int MAXN = 1e3+5;
const int MAXE = 1e3+5;
const int INF = 1e9;

int main()
{
    vector<Edge*> edges;
    int dist[MAXN];
    int n,m;
    // input
    cin >> n >> m;
    for (int i = 0; i<m; i++)
    {
        int u,v,w;
        cin >> u >> v >> w;
        edges.push_back(new Edge(u,v,w));
    }
    // bellmanford
    int src = 0;
    for (int i = 0; i<n; i++)
        dist[i] = INF;
    dist[src] = 0;
    for (int i = 0; i<n-1; i++)
        for (int j = 0; j<m; j++) // relax all edges
            if (dist[edges[j]->u] + edges[j]->w < dist[edges[j]->v]) 
                dist[edges[j]->v] = dist[edges[j]->u] + edges[j]->w;
    // check negative cycle
    for (int i = 0; i<m; i++)
        if (dist[edges[i]->u] + edges[i]->w < dist[edges[i]->v])
        {
            cout << "Negative cycle detected!" << endl;
            return 0;
        } 
    // output
    for (int i = 0; i<n; i++)
        cout << "dist(" << src+1 << "," << i+1 << "): " << dist[i] << endl;
}