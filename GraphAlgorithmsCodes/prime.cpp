#include <bits/stdc++.h>
#include "edge.hpp"

using namespace std;

const int MAXN = 1e5+5;

int main()
{
    vector< Edge* > adj[MAXN];
    bool f[MAXN];
    int n,m;
    // input
    cin >> n >> m;
    for (int i = 0; i<m; i++)
    {
        int u,v,w;
        cin >> u >> v >> w;
        u--; v--;
        adj[u].push_back(new Edge(u, v, w, i));
        adj[v].push_back(new Edge(v, u, w, i));
    }
    // prime 
    vector<int> mst_edges;
    int cost = 0;
    int src = 0; // arbitrary node
    auto compare = [](Edge a, Edge b)
                {
                    return !(a < b); // because convert priority_queue to min-heap
                };
    priority_queue<Edge, vector<Edge>, decltype(compare)> heap(compare);
    f[src] = true;
    for (Edge* edge: adj[src])
        heap.push(*edge);
    for (int i = 0; i<n-1; i++) // suppose graph is connected
    {
        Edge new_edge = heap.top();
        heap.pop();
        while (!(f[new_edge.u] && !f[new_edge.v])) // pop until find a edge where be between two set
        {
            heap.pop();
            new_edge = heap.top();
        }
        f[new_edge.v] = true;
        mst_edges.push_back(new_edge.ind);
        cost += new_edge.w;
        for (Edge* edge: adj[new_edge.v])
            heap.push(*edge);
    }
    // output
    cout << "MST cost: " << cost << endl;
    cout << "MST edges: " << endl;
    for (int edge: mst_edges)
        cout << edge+1 << ' ';
    cout << endl;
}