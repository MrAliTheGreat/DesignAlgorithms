#include <bits/stdc++.h>

using namespace std;

const int MAXN = 505;
const int INF = 1e9;

int main()
{
    int dist[MAXN][MAXN];
    int n;
    // input
    cin >> n;
    for (int i = 0; i<n; i++)
        for (int j = 0; j<n; j++)
        {
            int w;
            cin >> w;
            dist[i][j] = w;
            if (w == 0)
                dist[i][j] = INF;
        }
    // floydwarshall
    for (int k = 0; k<n; k++)
        for (int i = 0; i<n; i++)
            for (int j = 0; j<n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])  
                    dist[i][j] = dist[i][k] + dist[k][j];
    // output
    for (int i = 0; i<n; i++)
        for (int j = i+1; j<n; j++)
            cout << "dist(" << i+1 << "," << j+1 << "): " << dist[i][j] << endl;
}