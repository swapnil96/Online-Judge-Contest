#include <bits/stdc++.h>

constexpr int mod = 1000 * 1000 * 1000 + 7;

int Add(int a, int b) {
  a += b;
  if (a >= mod) a -= mod;
  return a;
}

int Subtract(int a, int b) {
  a -= b;
  if (a < 0) a += mod;
  return a;
}

class TestCase {
 private:
  int n, X;
  std::vector<int> answers;
  std::vector<std::vector<int>> graph;
  std::vector<int> C, K;
  std::vector<int> xs;

  std::vector<std::vector<int>> dp;

  void Dfs(int v) {
    const int c = C[v];
    const int k = K[v];
    int saved = K[v] ? dp[c][k - 1] : 0;
    for (int child : graph[v]) {
      Dfs(child);
    }
    if (k) {
      answers[v] = Subtract(dp[c][k - 1], saved);
    } else {
      answers[v] = 1;
    }
    dp[c][k] = Add(dp[c][k], answers[v]);
  }

  void Algorithm() {
    dp.resize(n);
    for (int i = 0; i < n; i++) {
      dp[i].resize(xs[i], 0);
    }
    Dfs(0);
  }

 public:
  int Run() {
    scanf("%d%d", &n, &X);
    assert(1 <= X and X <= n and n <= 500 * 1000);
    answers.resize(n);
    graph.resize(n);
    for (int i = 1; i < n; i++) {
      int p;
      scanf("%d", &p);
      assert(0 <= p and p < i);
      graph[p].push_back(i);
    }
    C.resize(n);
    xs.resize(n, 1);
    for (int v = 0; v < n; v++) {
      scanf("%d", &C[v]);
      assert(0 <= C[v] and C[v] < n);
      xs[C[v]]++;
    }
    K.resize(n);
    for (int v = 0; v < n; v++) {
      scanf("%d", &K[v]);
      assert(0 <= K[v] and K[v] < X);
      if (K[v] >= xs[C[v]]) {
        K[v] = xs[C[v]] - 1;
      }
    }
    Algorithm();
    for (int v = 0; v < n; v++) {
      printf("%d\n", answers[v]);
    }
    return n;
  }
};

int main() {
  int t;
  scanf("%d", &t);
  assert(1 <= t and t <= 100);
  int sum = 0;
  while (t--) sum += TestCase().Run();
  assert(1 <= sum and sum <= 2 * 1000 * 1000);
  return EXIT_SUCCESS;
}