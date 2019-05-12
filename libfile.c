#include<stdio.h>

int __declspec(dllexport) lib_func() {
  printf("The external library function was called.\n");
  return 42;
}
