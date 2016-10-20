# This is a secret document

* Alice and bob should be able to access this
* Eve should not

Try changing the permissions on this file using chmod and see what happens.

chmod [permissions] secret_document.txt

## Permissions

| Value | Meaning          | Symbolic |
| ----- | ---------------- | -------- |
|   0   | No permissions   |          |
|   1   | Execute          |     x    |
|   2   | write only       |     w    |
|   4   | read only        |     r    |
| ----- | ---------------- | -------- |

You can add them together to get blocks,

ie. read and write
read (4) + write (2) = 6
read (4) + write (2) + execute (1) = 7

## Symbolic

### "classes" used for symbolic mode
Permissions can be thought of as being grouped into 3 classes:

* User (u) - the owner of the file
* Group (g) - the group assigned to the file
* Other (o) - everyone else

[note]: you can see all 3 classes using the class "all" (a)

### operations for symbolic permissions
* add (+) - You can use + to add permissions (anything not mentioned is left the same)
* remove (-) - You can use - to remove permissions (anything not mentioned is left the same)
* set (=) - You can use = to set exact permissions (anything not mentioned is disallowed)

### examples
Remove everyone's write access from a file

chmod a-w filename.txt

Give the owner read write access, and set the group to have read only access and take away write access from everyone else.

chmod u+rw,g-w,o=r filename.txt

If you use + or -, permissions you don't mention will remain the same, so if 
user had execute permissions set on in the example above, it will still be set. 
As we used "=" for other, other's permissions will be set to "read only".

```bash
alice@ce708:~$ ls -l
total 4
-rwxrwxrwx 1 alice alice 1407 Oct 14 11:58 secret_document.txt
alice@ce708:~$ chmod u+rw,g-w,o=r secret_document.txt 
alice@ce708:~$ ls -l
total 4
-rwxr-xr-- 1 alice alice 1407 Oct 14 11:58 secret_document.txt
```

## Changing the group
You can use the chgrp command to change the owner of a document

```bash
alice@ce708:~$ ls -l
total 4
-rwxr-xr-- 1 alice alice 1681 Oct 14 12:23 secret_document.txt
alice@ce708:~$ chgrp csee secret_document.txt 
alice@ce708:~$ ls -l
total 4
-rwxr-xr-- 1 alice csee 1681 Oct 14 12:23 secret_document.txt
```

## Changing the owner
You can also change the owner of a file, however, only root can do this.

su -c "chmod bob secret_document.txt"

```bash
alice@ce708:~$ ls -l
total 4
-rwxr-xr-- 1 alice csee 2105 Oct 14 12:26 secret_document.txt
alice@ce708:~$ chown bob secret_document.txt 
chown: changing ownership of ‘secret_document.txt’: Operation not permitted
alice@ce708:~$ su
Password: 
root@ce708:/home/alice# chown bob secret_document.txt 
root@ce708:/home/alice# ls -l
total 4
-rwxr-xr-- 1 bob csee 2105 Oct 14 12:26 secret_document.txt
root@ce708:/home/alice# 
```

