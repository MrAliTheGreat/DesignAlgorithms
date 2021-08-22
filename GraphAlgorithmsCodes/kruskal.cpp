#include <bits/stdc++.h>
#include "edge.hpp"

using namespace std;

const int MAXN = 1e5+5;
const int MAXE = 1e5+5;

bool compare_edges(Edge* a,Edge* b)
{
    return (*a < *b);
}

vector<Edge*> edges;
int parent[MAXN];
int component_size[MAXN]; // has correct value only for root of components
vector<int> mst_edges;

int get_root(int u)
{
    return (parent[u]==u ? u : get_root(parent[u]));
    // optimize!, reduce complexity:
    // return (parent[u]==u ? u : parent[u] = get_root(parent[u]));
}

void merge(int u, int v)
{
	int u_root = get_root(u);
	int v_root = get_root(v);
	if (component_size[u_root]>component_size[v_root]) 
        swap(u_root, u_root); 
	parent[u_root] = v_root;
	component_size[v_root] += component_size[u_root];
}

int main()
{
    int n,m;
    // input
    cin >> n >> m;
    for (int i = 0; i<m; i++)
    {
        int u,v,w;
        cin >> u >> v >> w;
        edges.push_back(new Edge(u,v,w,i));
    }
    // kruskal
    for (int i = 0; i<n; i++)
    {
        parent[i] = i;
        component_size[i] = 1;
    }
    sort(edges.begin(), edges.end(), compare_edges);
    int cost = 0;
    for (int i = 0; i<m; i++)
    {
        if (get_root(edges[i]->u) == get_root(edges[i]->v)) // exist in same component
            continue;
        mst_edges.push_back(edges[i]->ind);
        cost += edges[i]->w;
        merge(edges[i]->u, edges[i]->v);
    }
    // output
    cout << "MST cost: " << cost << endl;
    cout << "MST edges: " << endl;
    for (int edge: mst_edges)
        cout << edge+1 << ' ';
    cout << endl;
}