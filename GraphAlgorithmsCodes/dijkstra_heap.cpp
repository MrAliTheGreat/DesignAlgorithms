#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e5+5;
const int INF = 1e9;

int main()
{
    int dist[MAXN];
    bool in_set[MAXN];
    vector< pair<int,int> > adj[MAXN];
    int n,m;
    // input
	cin >> n >> m;
    for (int i = 0; i<m; i++)
	{
		int u,v,w;
		cin >> u >> v >> w;
        u--; v--;
        adj[u].push_back({v,w});
        adj[v].push_back({u,w});
	}
    // dijkstra
    int src = 0;
    for (int i = 0; i<n; i++)
        dist[i] = INF;
	dist[src] = 0; 
    // format: (dist[u],u), use greater because priority_queue is max-heap!
    // priority_queue<{type}, {container}, {compare}>
	priority_queue< pair<int,int>, vector< pair<int,int> > , greater< pair<int,int> > > heap; 
    heap.push({dist[src], src});
	while (!heap.empty())
	{
		int u = -1;
        // because a node can push with different distances
        // have push/pop at most m times (amortized analysis) 
		while (u==-1 || (in_set[u] && !heap.empty()))  
		{
            u = heap.top().second;
			heap.pop();
		}
        if (in_set[u])
            break;
		in_set[u] = true;
        for (pair<int,int> p : adj[u]) // (ind,w)
        {
            int v = p.first;
            int w = p.second;
            if (!in_set[v] && dist[v]>dist[u]+w)
            {
                dist[v] = dist[u]+w;
                heap.push({dist[v],v});
            }
        }
	}
    // output
    for (int i = 0; i<n; i++)
        cout << "dist(" << src+1 << "," << i+1 << "): " << dist[i] << endl;
}
 