#include <stdio.h>
#include <string.h>

// practice with pointers

void foo(char* buf)
{
        char * pbuf = "1234\0";
        printf("%s\n", pbuf);
        strncpy(buf, pbuf, 5);
}

int main(int argc, char** argv){
        char buf[5];
        foo(buf);
        printf("%s\n", buf);
}
~
