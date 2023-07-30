#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int A, B, C;
bool check[201][201], ans[201];

struct Data{
    int a, b, c;
};

bool BFS(){
    queue<Data> myQue;
    myQue.push({0, 0, C});

    while(!myQue.empty()){
        Data now = myQue.front();
        myQue.pop();

        if (check[now.a][now.b])
            continue;

        check[now.a][now.b] = true;

        if (now.a == 0)
            ans[now.c] = true;

        // A -> B
        if (now.a > 0 && now.b < B){
            if (now.a + now.b < B)
                myQue.push({0, now.a + now.b, now.c});
            else
                myQue.push({(now.a + now.b) - B, B, now.c});
        }

        // A -> C
        if (now.a > 0 && now.c < C){
            if (now.a + now.c < C)
                myQue.push({0, now.b, now.a + now.c});
            else
                myQue.push({(now.a + now.c) - C, now.b, C});
        }

        // B -> A
        if (now.b > 0 && now.a < A){
            if (now.a + now.b < A)
                myQue.push({now.a + now.b, 0, now.c});
            else
                myQue.push({A, (now.a + now.b) - A, now.c});
        }

        // B -> C
        if (now.b > 0 && now.c < C){
            if (now.b + now.c < C)
                myQue.push({now.a, 0, now.b + now.c});
            else
                myQue.push({now.a, (now.b + now.c) - C, C});
        }

        // C -> A
        if (now.c > 0 && now.a < A){
            if (now.c + now.a < A)
                myQue.push({now.c + now.a, now.b, 0});
            else
                myQue.push({A, now.b, (now.c + now.a) - A});
        }

        // C -> B
        if (now.c > 0 && now.b < B){
            if (now.c + now.b < B)
                myQue.push({now.a, now.c + now.b, 0});
            else
                myQue.push({now.a, B, (now.c + now.b) - B});
        }
    }

    return true;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> A >> B >> C;

    BFS();

    for (int c=0; c<=C; ++c){
        if (ans[c])
            cout << c << " ";
    }
    
    return 0;
}
