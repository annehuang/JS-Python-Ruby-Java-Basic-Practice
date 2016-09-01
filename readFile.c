// a simple program to read a file into memory and print it out to stdout

#include <stdio.h>
#include <string.h>
#include <fcntl.h>

int main(int argc, char** argv){
  char buf[4096];

  // read whole file into memory
  int read_fd = open("filename", O_RDONLY, 0);

  read(read_fd, buf, 4096);

  printf("%s\n", buf);

  return 0;
}
