# IN THIS TOTURIAL YOU WILL LEARN HOW Hackers Can Take Sudo Passwords from Linux & MacOS Computers ON SAME NETWORK 


How Sudo Is Supposed to Work
Let's use the following whoami and id commands as an example. If we enter whoami into a terminal, it will return the current username.

~$ whoami

tokyoneon

With the id command, it will return the user's uid (-u), a unique identifier assigned to each user on the system. By default, in Debian and Ubuntu systems, a normal user (non-root user) is assigned the uid of 1000 (shown below). Similarly, in macOS, a normal user is assigned the 501 uid.

~$ id -u

1000

When prepended, sudo elevates and executes the provided command with root (uid 0) privileges. This is all standard and normal behavior for sudo and Unix systems.

~$ sudo id -u

0

The type command can be used to identify how the supplied command is interpreted by the shell.

~$ type sudo

sudo is /usr/bin/sudo

In this case, sudo is interpreted as /usr/bin/sudo. This is also standard behavior. When someone executes the sudo command (e.g., sudo whoami), they're essentially doing the following.

~$ /usr/bin/sudo /usr/bin/whoami

root
