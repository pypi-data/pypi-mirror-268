void func1() {
  // ruleid: invalid-free
  char buf[10];
  free(buf);
}

void func2() {
  // ruleid: invalid-free
  char ptr;
  free(&ptr);
}

char ptr;
free(&ptr);
