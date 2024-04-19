int func(int n) {
  char buf[100];
  // ruleid: write-to-stack-buffer
  memcpy(buf, src, n);
  return n;
}

void func2() {
  char buf[100];
  int n = func();
  if (n < 100) {
    // ok: write-to-stack-buffer
    memcpy(buf, src, n);
  }
}

int func3(int n) {
  char buf[100];
  // ok: write-to-stack-buffer
  memcpy(buf, "hello", n);
  return n;
}

int func4(char* buf, char* src, int n) {
  // ok: write-to-stack-buffer
  memcpy(buf, src, n);
  return n;
}
