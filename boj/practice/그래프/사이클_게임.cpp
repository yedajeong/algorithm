// 20040
// 유니온 파인드
#include <iostream>
using namespace std;

int n, m;
const int max_node = 500000;
int parent[max_node];

int find(int x){
    if (x != parent[x])
        parent[x] = find(parent[x]);
    return parent[x];
}

bool merge(int a, int b){
    a = find(a);
    b = find(b);
    if (a == b) return true;
    else if (a > b) parent[a] = b;
    else parent[b] = a;
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int a, b;
    cin >> n >> m;

    for(int i=0; i<n; ++i){
        parent[i] = i;
    }

    for(int i=1; i<=m; ++i){
        cin >> a >> b;
        a = find(a);
        b = find(b);

        if (merge(a, b)){
            cout << i;
            return 0;
        }
    }

    cout << 0;

    return 0;
}
