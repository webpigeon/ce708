# Useful Linux Commands
Here are some basic commands for when you are using linux. I'm only giving some very basic examples but you can do a lot more with them.

## File Management

| Command | Usage | Example | Description |
| ------- | ----- | ------- | ----------- |
| cp      | cp [from] [to] | cp myfile myfile_copy | Create a copy of a file |
| mv      | mv [from] [to] | mv myfile /home/bob/myfile | Move (or rename) a file |
| touch   | touch [file]   | touch myfile | Create a new (empty) file or update the modified file on an existing file |
| nano    | nano [file]    | nano myFile | edit a file (can also be used to create new files) |
| cat     | cat [file] [file] | cat myFile otherFile | concatenate files together and output the result (can be used with one file to print the contents of that file) |
| head    | head [file] | head myFile | Print the first few (default 10) lines of a file |
| tail    | tail [file] | tail myFile | Print the last few (default 10) lines of a file |

## User Management

| Command | Usage | Example | Description |
| ------- | ----- | ------- | ----------- |
| su      | su [username] | su bob | switch to a different user account |
| whoami  | whoami | whoami | print the current user |
| groups  | groups | groups | print the groups the current user is in |

## System management

| Command | Usage | Example | Description |
| ------- | ----- | ------- | ----------- |
| kill | kill [pid] | kill 1234 | Kill the process with the ID [1234] |
| killall | killall [name] | killall firefox | Kill all processes called "firefox" |
| top | top | top | Task manager for the command line |
| htop | htop | htop | A pretty version of top (might not always be installed) |

