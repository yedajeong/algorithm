#include <iostream>
#include <string>
using namespace std;

int N, M;
int parent[1000001];

int find(int n){
    if (parent[n] == n)
        return n;
    else
        return parent[n] = find(parent[n]);
}

void union_merge(int a, int b){
    a = find(a);
    b = find(b);

    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;
    cin >> M;

    int a, b;
    int city[N+1][N+1];
    bool connect, ans = true;

    for (int i=1; i<=N; ++i)
        parent[i] = i;

    for (int i=1; i<=N; ++i){
        for (int j=1; j<=N; ++j){
            cin >> connect;
            city[i][j] = connect;

            if (connect)
                union_merge(i, j);
        }
    }
    
    cin >> a;
    for (int i=1; i<M; ++i){
        cin >> b;
        if (find(a) != find(b)){
            ans = false;
            cout << "NO\n";
            break;
        }
    }

    if (ans)
        cout << "YES\n";

    return 0;
}
