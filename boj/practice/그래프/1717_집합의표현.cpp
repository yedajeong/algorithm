#include <iostream>
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

    int cal, a, b;
    cin >> N >> M;

    for (int i=1; i<=N; ++i)
        parent[i] = i;

    for (int i=0; i<M; ++i){
        cin >> cal >> a >> b;

        if (cal){
            if (find(a) == find(b))
                cout << "YES\n";
            else
                cout << "NO\n";
        }
        
        else{
            union_merge(a, b);
        }
    }

    return 0;
}
