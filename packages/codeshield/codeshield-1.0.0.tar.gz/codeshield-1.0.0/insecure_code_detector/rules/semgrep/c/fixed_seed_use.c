#include <stdio.h>
#include <stdlib.h>

int main() {
  unsigned int seed;
  // ruleid: fixed-seed-usage
  seed = 10;
  srand(seed);
  printf("Random value: %d\n", rand());

  FILE* urandom = fopen("/dev/urandom", "r");
  // ok: fixed-seed-usage
  unsigned int rngSeed;
  fread(&rngSeed, sizeof(rngSeed), 1, urandom);
  fclose(urandom);
  srand(rngSeed);
  printf("Random value: %d\n", rand());
  return 0;
}
