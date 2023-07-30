#include <iostream>
#include <string>
#include <vector>
using namespace std;

int N, M;
int parent[51];

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

    cin >> N >> M;
    vector<vector<int>> party(M); // 파티 참석자들의 집합 (루트노드) 저장
    
    for (int i=1; i<=N; ++i)
        parent[i] = i;
    
    int num, truth, a, b, ans = M;
    
    cin >> num;

    if (num == 0){
        cout << ans;
        return 0;
    }
    else{
        cin >> truth;
        for (int i=1; i<num; ++i){
            cin >> a;
            union_merge(truth, a);
        }
    }

    // 파티 참석자 정보 얻기
    for (int i=0; i<M; ++i){
        cin >> num;
        cin >> a;
        party[i].push_back(a);
        for (int j=1; j<num; ++j){
            cin >> b;
            union_merge(a, b);
            party[i].push_back(a);
        }
    }

    for (int i=0; i<M; ++i){
        if (find(party[i][0]) == find(truth)) ans--;
    }

    cout << ans;

    return 0;
}
