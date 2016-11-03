#include <stdio.h>
#include <string.h>

/**
 * Buffer overrun demonstration.
 * 
 * Compile with:
 *  gcc --debug -fno-stack-protector overrun.c -o overrun
 */

struct auth_status {
        char passwd[25];
        int authenticated;
};

int main(void) {
    char *correct_password = "iamagoodprogrammer";
    struct auth_status p;
    
    p.authenticated = 0;

    printf("\n Enter the password : \n");

    // this is a fixed version of the input routine
    fgets(p.passwd, 24, stdin);

    //fgets will include the newline, so we check for it and remove it
    char *newlineptr = strchr(p.passwd, '\n');
    if (newlineptr != NULL) {
	*newlineptr = '\0';
    }

    // style points set authenticated to 42: 28 = buffer + 3 (an int is 4 bytes)
    // p.passwd[28] = '*';    

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
