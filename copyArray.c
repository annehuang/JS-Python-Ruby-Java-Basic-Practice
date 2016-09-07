#include <stdio.h>
#include <string.h>

// practice with pointers

void foo(char* buf)
{
        char * pbuf = "1234\0";
        printf("%s\n", pbuf);
        strncpy(buf, pbuf, 5);
}

void unsignedFoo(unsigned char * buf){
        unsigned char * pbuf = "1234";
        printf("%s\n", (char *) pbuf);
        memcpy(buf, pbuf, 4);
}

int main(int argc, char** argv){
        char buf[5];
        foo(buf);
        printf("%s\n", buf);
        
        char buf2[4];
        unsignedfoo(buf2);
        printf("%s\n", buf2);
}
~
