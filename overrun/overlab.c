#include <stdio.h>
#include <string.h>

/**
 * Buffer overrun demonstration.
 * 
 * Compile with:
 *  gcc --debug -fno-stack-protector overrun.c -o overrun
 */

struct auth_status {
        int authenticated;
        char passwd[25];
};

int main(void) {
    char *correct_password = "iamagoodprogrammer";
    struct auth_status p;
    
    p.authenticated = 0;

    printf("\n Enter the password : \n");
    gets(p.passwd);
    
    if (!strcmp(p.passwd, correct_password)) {
        p.authenticated = 1;
    } 
    
    if (p.authenticated) {
       /* Now Give root or admin rights to user*/
        printf ("\n Administrator privileges given to the user \n");
        return 0;
    }

    return -1;
}
