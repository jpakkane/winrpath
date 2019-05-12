#include<stdio.h>

int __declspec(dllimport) lib_func();

int main(int argc, char **argv) {
  const int number = lib_func();
  if(number == 42) {
    printf("The library returned the correct value.");
    return 0;
  } else {
    printf("The library returned an incorrect value %d", number);
    return 1;
  }
}
