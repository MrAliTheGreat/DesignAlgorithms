#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e5+5;
const int INF = 1e9;

int main()
{
    int dist[MAXN],parent[MAXN];
    bool in_set[MAXN];
    vector< pair<int,int> > adj[MAXN]; // adjacency list: (ind,weight)
    int n,m;
    // input
    cin >> n >> m;
    for (int i = 0; i<m; i++)
    {
        int u,v,w;
        cin >> u >> v >> w;
        u--; v--; // use 0-base index
        adj[u].push_back({v,w});
        adj[v].push_back({u,w});
    }
    // dijkstra
    int src = 0;
    for (int i = 0; i<n; i++)
        dist[i] = INF;
    dist[src] = 0;
    set< pair<int,int> > s; // (dist[u],u)
    s.insert(make_pair(dist[src],src));
    while (!s.empty())
    {
        int u = s.begin()->second;
        in_set[u] = true;
        s.erase(s.begin());
        for (pair<int,int> p : adj[u]) // (ind,w)
        {
            int v = p.first;
            int w = p.second;
            if (!in_set[v] && dist[v]>dist[u]+w)
            {
                s.erase({dist[v],v}); // erase previous distance
                dist[v] = dist[u]+w;
                parent[v] = u; // use for find shortest path
                s.insert({dist[v],v}); // insert new distance
            }
        }
    }
    // output: find shortest path between src to dst
    int dst = n-1;
    if (dist[dst]==INF) {
        cout << "no path!";
        return 0;
    }
    vector<int> path;
    int cuurent_node = dst;
    while (cuurent_node!=src)
    {
        path.push_back(cuurent_node);
        cuurent_node = parent[cuurent_node];
    }
    path.push_back(src);
    reverse(path.begin(), path.end());
    cout << "path from " << src+1 << " to " << dst+1 << ":" << endl;
    for (int node: path)
        cout << node+1 << ' ';
    cout << endl;
}