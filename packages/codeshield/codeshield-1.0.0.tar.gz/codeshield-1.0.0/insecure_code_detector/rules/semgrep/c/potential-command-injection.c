void test_1(char* cmd) {
  // ruleid: potential-command-injection
  system(cmd);
}

void test_2() {
  // ok: potential-command-injection
  system("ls");
}

void test_3() {
  // ok: potential-command-injection
  char* cmd = "ls";
  system(cmd);
}

void test_4() {
  // ok: potential-command-injection
  system(F_CLEAR);
}
