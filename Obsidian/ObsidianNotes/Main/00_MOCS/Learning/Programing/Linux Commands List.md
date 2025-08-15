---
updated_date: <% tp.file.creation_date('DD/MM/YYYY') %>
tags:
  - programming/bash
---
## Linux Commands List

The commands from the downloadable cheat sheet are listed below. If you're looking for the must-know commands only and a shorter cheat sheet, check out [Linux Commands All Users Should Know](https://phoenixnap.com/kb/linux-commands).

### Hardware Information Commands

Hardware information commands help provide insight into various hardware devices on the system. Use these commands to check [hardware](https://phoenixnap.com/glossary/what-is-hardware) information and see hardware device statuses.

|Command|Description|
|---|---|
|**`lscpu`**|See [CPU](https://phoenixnap.com/glossary/cpu-definition) information.|
|**`lsblk`**|See information about [block devices](https://phoenixnap.com/glossary/block-device).|
|**`lspci -tv`**|[Show PCI devices](https://phoenixnap.com/kb/lspci-command) (graphics card, network card, etc.) in a tree-like diagram.|
|**`lsusb -tv`**|Display USB devices in a tree-like diagram.|
|**`lshw`**|List hardware configuration information.|
|**`cat /proc/cpuinfo`**|Show detailed CPU information.|
|**`cat /proc/meminfo`**|View detailed system memory information.|
|**`cat /proc/mounts`**|See mounted [file systems](https://phoenixnap.com/kb/linux-file-system).|
|**`free -h`**|Display [free and used memory](https://phoenixnap.com/kb/free-linux-command).|
|**`sudo dmidecode`**|Show hardware information from the [BIOS](https://phoenixnap.com/glossary/basic-input-output-system-bios).|
|**`hdparm -i /dev/[device_name]`**|Display disk data information.|
|**`hdparm -tT /dev/[device_name]`**|Conduct a read speed test on the device/disk.|
|**`badblocks -s /dev/[device_name]`**|Test for unreadable blocks on the device/disk.|
|**`fsck /dev/[device_name]`**|[Run a disk check](https://phoenixnap.com/kb/fsck-command-linux) on an unmounted disk or partition.|

### Searching Commands

Linux offers various commands to search for files, directories, and text. Use these commands to search for files and directories on the system and filter the search using various patterns.

|Command|Description|
|---|---|
|**`find [path] -name [search_pattern]`**|[Find files and directories](https://phoenixnap.com/kb/guide-linux-find-command) that match the specified pattern in a specified location.|
|**`find [path] -size [+100M]`**|See files and directories larger than a specified size in a directory.|
|**`grep [search_pattern] [file_name]`**|[Search for a specific pattern](https://phoenixnap.com/kb/grep-multiple-strings) in a [file](https://phoenixnap.com/glossary/what-is-a-file) with [grep](https://phoenixnap.com/kb/grep-command-linux-unix-examples).|
|**`grep -r [search_pattern] [directory_name]`**|Recursively search for a pattern in a directory.|
|**`locate [name]`**|[Locate all files and directories](https://phoenixnap.com/kb/locate-command-in-linux) related to a particular name.|
|**`which [command]`**|[Search the command path](https://phoenixnap.com/kb/which-command-linux) in the **`$PATH`** environment variable.|
|**`whereis [command]`**|Use the [whereis command](https://phoenixnap.com/kb/whereis-command-linux) to find the source, binary, and manual page for a command.|
|**`awk '[search_pattern] {print $0}' [file_name]`**|[Print all lines matching a pattern](https://phoenixnap.com/kb/awk-command-in-linux) in a file. See also the [gawk command](https://phoenixnap.com/kb/gawk-linux), the [GNU](https://phoenixnap.com/glossary/what-is-gnu) version of **`awk`**.|
|**`sed 's/[old_text]/[new_text]/' [file_name]`**|[Find and replace text](https://phoenixnap.com/kb/sed-replace) in a specified file.|

**Note:** Some commands are not recommended to use. Learn about them in our list of [dangerous Linux commands](https://phoenixnap.com/kb/dangerous-linux-terminal-commands).

### File Commands

File commands help with file and directory management on the system. Create, delete, move, and modify files and directories from the terminal using the commands in the following table.

|Command|Description|
|---|---|
|**`mkdir [directory_name]`**|[Create a new directory](https://phoenixnap.com/kb/create-directory-linux-mkdir-command).|
|**`rm [file_name]`**|[Remove a file](https://phoenixnap.com/kb/how-to-remove-files-directories-linux-command-line).|
|**`rm -r [directory_name]`**|Remove a directory recursively.|
|**`rm -rf [directory_name]`**|Recursively remove a directory without requiring confirmation.|
|**`cp [source_file] [destination_file]`**|[Copy the contents of one file](https://phoenixnap.com/kb/how-to-copy-files-directories-linux) to another file using the [cp command](https://phoenixnap.com/kb/cp-command).|
|**`cp -r [source_directory] [destination_directory]`**|Recursively copy a directory to a second directory.|
|**`mv [source_file] [destination_file]`**|[Move or rename files](https://phoenixnap.com/kb/mv-command-linux) or directories.|
|**`ln -s [path]/[file_name] [link_name]`**|[Create a symbolic link](https://phoenixnap.com/kb/symbolic-link-linux) to a file.|
|**`touch [file_name]`**|Create a new file using [touch](https://phoenixnap.com/kb/touch-command-in-linux).|
|**`cat [file_name]`**|[Show the contents of a file](https://phoenixnap.com/kb/linux-cat-command).|
|**`cat [source_file] >> [destination_file]`**|Append file contents to another file.|
|**`head [file_name]`**|Show the first ten lines of a file.|
|**`tail [file_name]`**|Show the last ten lines of a file with the [tail command](https://phoenixnap.com/kb/linux-tail).|
|**`more [file_name]`**|Display contents of a file page by page.|
|**`less [file_name]`**|Show the contents of a file with navigation using the [less command](https://phoenixnap.com/kb/less-command-in-linux).|
|**`nano [file_name]`**|Open or create a file using the [nano text editor](https://phoenixnap.com/kb/use-nano-text-editor-commands-linux).|
|**`vi [file_name]`**  <br>**`vim [file_name]`**|Open or create a file using the [Vi/Vim text editor](https://phoenixnap.com/kb/vim-commands-cheat-sheet).|
|**`gpg -c [file_name]`**|Encrypt a file.|
|**`gpg [file_name].gpg`**|Decrypt an encrypted _.gpg_ file.|
|**`wc -w [file_name]`**|Show the number of words, lines, and bytes in a file using [wc](https://phoenixnap.com/kb/wc-linux).|
|**`ls \| xargs wc`**|List the number of lines/words/characters in each file in a directory with the [xargs command](https://phoenixnap.com/kb/xargs-command).|
|**`cut -d [delimiter] [file_name]`**|[Cut a section of a file](https://phoenixnap.com/kb/linux-cut) and print the result to standard output.|
|**`[data] \| cut -d [delimiter]`**|Cut a section of piped data and print the result to standard output.|
|**`shred -u [file_name]`**|[Overwrite a file](https://phoenixnap.com/kb/shred-linux) to prevent its recovery, then delete it.|
|**`diff [first_file] [second_file]`**|[Compare two files](https://phoenixnap.com/kb/linux-diff) and display differences.|
|**`source [file_name]`**|[Read and execute the file content](https://phoenixnap.com/kb/linux-source-command) in the current shell.|
|**`[command] \| tee [file_name] >/dev/null`**|[Store the command output in a file](https://phoenixnap.com/kb/linux-tee) and skip the terminal output.|

**Note:** Want to read more about file creation? Check out our article about [how to create a file in Linux using the command line](https://phoenixnap.com/kb/how-to-create-a-file-in-linux).

And if you want to find out how to determine the type of a file and its data, read the [Linux file command](https://phoenixnap.com/kb/linux-file-command) article.

### Directory Navigation Commands

Directory navigation commands provide shortcuts to navigate to the desired location quickly. Below are several crucial shortcuts to remember when navigating directories in Linux through the terminal.

|Directory Navigation Commands|Description|
|---|---|
|**`ls`**|[List files and directories](https://phoenixnap.com/kb/linux-ls-commands) in the current directory.|
|**`ls -a`**|List all files and directories in the current directory ([shows hidden files](https://phoenixnap.com/kb/show-hidden-files-linux)).|
|**`ls -l`**|List files and directories in long format.|
|**`pwd`**|[Show the directory](https://phoenixnap.com/kb/pwd-linux) you are currently working in.|
|**`cd`**  <br>**`cd ~`**|[Change directory](https://phoenixnap.com/kb/linux-cd-command) to **`$HOME`**.|
|**`cd ..`**|Move up one directory level.|
|**`cd -`**|Change to the previous directory.|
|**`cd [directory_path]`**|Change location to a specified directory.|
|**`dirs`**|Show current directory stack.|

### File Compression Commands

Archive and compress files to save space on your system and organize your data. There are various compression formats available on Linux, and the table below shows the most commonly used file compression commands.

|Command|Description|
|---|---|
|**`tar cf [archive.tar] [file/directory]`**|Archive an existing file or directory.|
|**`tar xf [archive.tar]`**|[Extract an archived file](https://phoenixnap.com/kb/extract-tar-gz-files-linux-command-line#htoc-using-tar-utility).|
|**`tar czf [archive.tar.gz]`**|Create a _.gz_ compressed tar archive.|
|**`gzip [file_name]`**  <br>**`gunzip [file_name.gz]`**|[Compress](https://phoenixnap.com/glossary/file-compression) or decompress _.gz_ files.|
|**`bzip2 [file_name]`**  <br>**`bunzip2 [file_name.bz2]`**|Compress or [decompress .bz2 files](https://phoenixnap.com/kb/bz2-unzip).|

**Note:** For a more comprehensive overview of how to use **`tar`** refer to our guide [tar Command in Linux With Examples](https://phoenixnap.com/kb/tar-command-in-linux). See also how to [unzip tar.bz2 files](https://phoenixnap.com/kb/tar-bz2-unzip).

### File Transfer Commands

Depending on the transfer method and protocol, Linux has various file transfer commands. Use these commands to quickly transfer files between two remote machines or to download files from web servers.

|Command|Description|
|---|---|
|**`scp [source_file] [user]@[remote_host]:[destination_path]`**|Copy a file to a server directory securely using the [Linux scp command](https://phoenixnap.com/kb/linux-scp-command).|
|**`rsync -a [source_directory] [user]@[remote_host]:[destination_directory]`**|Synchronize the contents of a directory with a backup directory using the [rsync command](https://phoenixnap.com/kb/rsync-command-linux-examples).|
|**`wget [link]`**|Download files from [FTP](https://phoenixnap.com/glossary/what-is-ftp) or web servers via the [wget command](https://phoenixnap.com/kb/wget-command-with-examples).|
|**`curl -O [link]`**|Transfer data to or from a server with various protocols using the [curl command](https://phoenixnap.com/kb/curl-command).|
|**`ftp [remote_host]`**|Transfer files between local and remote systems interactively using FTP.|
|**`sftp [user]@[remote_host]`**|Securely transfer between local and remote hosts using [SFTP](https://phoenixnap.com/kb/what-is-sftp).|

### User and Group Commands

Linux is a multiuser system, and there are various commands to add, modify, remove, and manage users and groups. The table below outlines the critical user and group commands.

|Command|Description|
|---|---|
|**`id`**|See details about the active users.|
|**`last`**|Show the last system logins.|
|**`who`**|Display who is currently logged into the system with the [who command](https://phoenixnap.com/kb/linux-who-command).|
|**`w`**|Show which users are logged in and their activity with the [w command](https://phoenixnap.com/kb/w-command-in-linux).|
|**`finger [user_name]`**|Show user information.|
|**`sudo useradd [user_name]`**|Create a new user account.|
|**`sudo adduser [user_name]`**|Create a new user account through the [adduser command](https://phoenixnap.com/kb/linux-adduser) interface.|
|**`sudo userdel [user_name]`**|Delete a user account.|
|**`sudo usermod -aG [group_name] [user_name]`**|[Modify user information](https://phoenixnap.com/kb/usermod-linux) ([add a user to a group](https://phoenixnap.com/kb/add-user-to-linux-group)).|
|**`passwd`**  <br>**`sudo passwd [user_name]`**|Change the current user's password or another user's password with the [passwd command](https://phoenixnap.com/kb/passwd-command-in-linux).|
|**`sudo groupadd [group_name]`**|Add a new group.|
|**`sudo groupdel [group_name]`**|Delete a group.|
|**`sudo groupmod -n [new_name] [old_name]`**|Modify a user group (change group name).|
|**`sudo [command]`**|Temporarily elevate user privileges to superuser or root using the [sudo command](https://phoenixnap.com/kb/linux-sudo-command).|
|**`su - [user_name]`**|[Switch the user account](https://phoenixnap.com/kb/su-command-linux-examples) or become a superuser.|
|**`chgrp [group_name] [file/directory]`**|[Change file or directory group](https://phoenixnap.com/kb/chgrp-command).|

### Package Installation Commands

Specific package manager commands vary between different [Linux distributions](https://phoenixnap.com/glossary/what-is-a-linux-distribution). Choose the commands that match your specific distribution.

#### Debian and Ubuntu-Based Distributions

Debian and Ubuntu-based distributions use the **`apt-get`**, **`apt`**, and **`dpkg`** commands to manage packages. Below are crucial commands necessary to install packages on these systems.

|Command|Description|
|---|---|
|**`sudo apt-get install [package_name]`**|Install an APT package using the [apt-get package utility](https://phoenixnap.com/kb/how-to-use-apt-get-commands).|
|**`sudo apt install [package_name]`**|Install an APT package using a [newer APT package manager](https://phoenixnap.com/kb/apt-linux).|
|**`apt search [keyword]`**|Search for a package in the APT repositories.|
|**`apt list`**|List packages installed with APT.|
|**`apt show [package_name]`**|Show information about a package.|
|**`sudo dpkg -i [package_name.deb]`**|Install a _.deb_ package with the Debian package manager ([dpkg command](https://phoenixnap.com/kb/dpkg-command)).|
|**`sudo dpkg -l`**|List packages installed with dpkg.|

#### Red Hat-Based Distributions (CentOS, Fedora)

Red Hat-based distributions, including CentOS and Fedora, use the **`yum`**, **`dnf`**, and **`rpm`** commands for package installation. The table below provides the syntax for each option.

|Command|Description|
|---|---|
|**`sudo yum install [package_name]`**|Install a package using the YUM package manager.|
|**`yum search [keyword]`**|Find a package in the YUM repositories based on the provided keyword.|
|**`yum list installed`**|[List all packages installed with YUM](https://phoenixnap.com/kb/how-to-list-installed-packages-on-centos).|
|**`yum info [package_name]`**|Show package information for a package.|
|**`sudo dnf install [package_name]`**|Install a package using the DNF package manager.|
|**`sudo rpm -i [package_name.rpm]`**|Install a [_.rpm_ package](https://phoenixnap.com/kb/rpm-command-in-linux) from a local file.|

**Note:** See our detailed comparison between [RPM vs. YUM](https://phoenixnap.com/kb/rpm-vs-yum).

#### Universal Linux Packages

Universal Linux packages are distribution-independent package collections. The two most popular options that come preinstalled on many systems are **`snap`** and **`flatpak`** commands. Alternatively, most [programs](https://phoenixnap.com/glossary/what-is-a-program) offer the option to install from source. The table below shows the syntax for each listed option.

|Command|Description|
|---|---|
|**`tar zxvf [file_name.tar.gz]`**  <br>**`cd [extracted_directory]`**  <br>**`./configure make`**  <br>**`make install`**|Install software from [source code](https://phoenixnap.com/glossary/what-is-source-code).|
|**`sudo snap install [package_name]`**|Install a [Snap](https://phoenixnap.com/kb/install-snap-ubuntu) package.|
|**`sudo snap find [keyword]`**|Search for a package in the Snap store.|
|**`sudo snap list`**|List installed Snap packages.|
|**`flatpak install [package_name]`**|Install a Flatpak package.|
|**`flatpak search [keyword]`**|Search for a Flatpak application in repositories.|
|**`flatpak list`**|List installed Flatpack packages.|

**Note:** Check out our comparison between three popular distribution-independent package formats: [Flatpak vs. Snap vs. Appimage](https://phoenixnap.com/kb/flatpak-vs-snap-vs-appimage).

### Process Related Commands

Every application and command in Linux creates a process. The table below shows various process-related commands to help manage Linux processes.

|Command|Description|
|---|---|
|**`ps`**|[List active processes](https://phoenixnap.com/kb/list-processes-linux).|
|**`pstree`**|Show processes in a tree-like diagram.|
|**`pmap`**|Display a memory usage map of processes.|
|**`top`**|See [all running processes](https://phoenixnap.com/kb/top-command-in-linux).|
|**`htop`**|Interactive and colorful process viewer.|
|**`kill [process_id]`**|[Terminate a Linux process](https://phoenixnap.com/kb/how-to-kill-a-process-in-linux) under a given ID.|
|**`pkill [process_name]`**|Terminate a process under a specific name.|
|**`killall [label]`**|Terminate all processes with a given label.|
|**`prgrep [keyword]`**|List processes based on the provided keyword.|
|**`pidof [process_name]`**|Show the PID of a process.|
|**`bg`**|List and resume stopped jobs in the background.|
|**`fg`**|Bring the most recently suspended job to the foreground.|
|**`fg [job]`**|Bring a particular job to the foreground.|
|**`lsof`**|List files opened by running processes with [lsof command](https://phoenixnap.com/kb/lsof-command).|
|**`trap "[commands]" [signal]`**|[Catch a system error signal](https://phoenixnap.com/kb/bash-trap-command) in a shell script. Executes provided commands when the signal is caught.|
|**`wait`**|[Pause the terminal or a Bash script](https://phoenixnap.com/kb/bash-wait-command) until a running process is completed.|
|**`nohup [command] &`**|[Run a Linux process](https://phoenixnap.com/kb/linux-nohup) in the background.|
|||

**Note:** If you want to learn more about shell jobs, how to terminate jobs or keep them running after you log off, check out our article on [how to use disown command](https://phoenixnap.com/kb/disown-command-linux).

### System Management and Information Commands

Use the terminal to manage the system directly. The commands show how to view basic system information, change options, and reboot or restart the system.

|Command|Description|
|---|---|
|**`uname -r`**|Show system information via [uname command](https://phoenixnap.com/kb/uname-linux).|
|**`uname -a`**|See [kernel release information](https://phoenixnap.com/kb/check-linux-kernel-version).|
|**`uptime`**|[Display system uptime](https://phoenixnap.com/kb/linux-uptime), including the load average.|
|**`hostname`**|View system hostname.|
|**`hostname -i`**|Show the [IP address](https://phoenixnap.com/glossary/what-is-an-ip-address) of the system.|
|**`last reboot`**|List system reboot history.|
|**`date`**|See [current time and date](https://phoenixnap.com/kb/linux-date-command).|
|**`timedatectl`**|Query and change the [system clock](https://phoenixnap.com/kb/how-to-set-or-change-timezone-date-time-ubuntu).|
|**`cal`**|Show current calendar (month and day).|
|**`w`**|[List logged-in users](https://phoenixnap.com/kb/w-command-in-linux).|
|**`whoami`**|[See which user you are using](https://phoenixnap.com/kb/whoami-linux).|
|**`finger [user_name]`**|Show information about a particular user.|
|**`ulimit [flags] [limit]`**|[View or limit](https://phoenixnap.com/kb/ulimit-linux-command) system resource amounts.|
|**`shutdown [hh:mm]`**|[Schedule a system shutdown](https://phoenixnap.com/kb/linux-shutdown-command).|
|**`shutdown now`**|Shut down the system immediately.|
|**`modprobe [module_name]`**|[Add a new kernel module](https://phoenixnap.com/kb/modprobe-command).|
|**`dmesg`**|[Show bootup messages](https://phoenixnap.com/kb/dmesg-linux).|

### Disk Usage Commands

Disk usage commands provide insight into disk space status. You can use the **`df`** and **`du`** commands to [check disk space in Linux](https://phoenixnap.com/kb/linux-check-disk-space). Common disk usage commands are outlined in the table below.

|Command|Description|
|---|---|
|**`df -h`**|Check free and used space on mounted systems.|
|**`df -i`**|Show free inodes on mounted file systems.|
|**`fdisk -l`**|Display disk partitions, sizes, and types with the command.|
|**`du -ah`**|See [disk usage for all files and directories](https://phoenixnap.com/kb/show-linux-directory-size).|
|**`du -sh`**|Show disk usage of the current directory.|
|**`mount`**|Show currently mounted file systems.|
|**`findmnt`**|Display target mount point for all file systems.|
|**`mount [device_path] [mount_point]`**|[Mount a device](https://phoenixnap.com/kb/linux-mount-command).|

### SSH Login Commands

[SSH](https://phoenixnap.com/kb/what-is-ssh) commands enable connecting to a remote host using the SSH protocol. Other commands use this protocol for copying and transferring files between two systems.

See the table below for common SSH commands. For a detailed explanation of SSH Linux Commands, refer to our [SSH Commands in Linux](https://phoenixnap.com/kb/linux-ssh-commands) tutorial.

|Command|Description|
|---|---|
|**`ssh [user_name]@[remote_host]`**|[Connect to a remote host](https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows) as a user via SSH.|
|**`ssh [host]`**|Securely connect to a host via [SSH default port 22](https://phoenixnap.com/kb/change-ssh-port).|
|**`ssh -p [port] [user_name]@[remote_host]`**|Connect to the host using a particular port.|
|**`ssh-keygen`**|[Generate SSH key pairs](https://phoenixnap.com/kb/generate-setup-ssh-key-ubuntu).|
|**`sudo service sshd start`**|Start SSH server [daemon](https://phoenixnap.com/glossary/what-is-a-daemon).|
|**`scp [file_name] [user_name]@[remote_host]:[remote_path]`**|[Securely copy files](https://phoenixnap.com/kb/linux-scp-command) between local and remote systems via SSH.|
|**`sftp [user_name]@[remote_host]`**|Interactive file transfer over encrypted SSH session using [SFTP](https://phoenixnap.com/kb/what-is-sftp) protocol.|
|**`telnet [host]`**|Connect to the host via [Telnet](https://phoenixnap.com/glossary/what-is-telnet) default port 23.|

### File Permission Commands

File permission commands control user permissions over files and directories. Use these commands to change and manage the owner, group, and user permissions on the system.

|Command|Description|
|---|---|
|**`chmod 777 [file_name]`**|Assign read, write, and execute [file permission](https://phoenixnap.com/kb/linux-file-permissions) to everyone (**`rwxrwxrwx`**).|
|**`chmod 755 [file_name]`**|Give read, write, and execute permission to owner, and read and execute permission to group and others (**`rwxr-xr-x`**).|
|**`chmod 766 [file_name]`**|Assign full permission to the owner, and read and write permission to the group and others (**`rwxrw-rw-`**).|
|**`chown [user_name] [file_name]`**|Change the ownership of a file with [chown command](https://phoenixnap.com/kb/linux-chown-command-with-examples).|
|**`chown [user_name]:[group_name] [file_name]`**|Change the owner and group ownership of a file.|

**Note**: To recursively change file permissions inside multiple directories, see our [chmod recursive](https://phoenixnap.com/kb/chmod-recursive) guide.

### Network Commands

The table below shows a brief list of common Linux network commands. For a more comprehensive list, check out our [Linux Network Commands Cheat Sheet](https://phoenixnap.com/kb/linux-network-commands).

|Description|Command|
|---|---|
|**`ip addr show`**|[List IP addresses](https://phoenixnap.com/kb/linux-ip-command-examples) and network interfaces.|
|**`ip address add [IP_address]`**|Assign an IP address to interface **eth0**.|
|**`ifconfig`**|Display IP addresses of all network interfaces.|
|**`ping [remote_host]`**|[Ping](https://phoenixnap.com/glossary/what-is-ping) remote host.|
|**`netstat -pnltu`**|See active (listening) ports with the [netstat command](https://phoenixnap.com/kb/netstat-command).|
|**`netstat -tuln`**|Show [TCP](https://phoenixnap.com/glossary/transmission-control-protocol-tcp) and [UDP](https://phoenixnap.com/glossary/what-is-udp) ports and their programs.|
|**`whois [domain_name]`**|Display more information about a [domain](https://phoenixnap.com/glossary/what-is-a-domain).|
|**`dig [domain_name]`**|Show [DNS](https://phoenixnap.com/kb/what-is-domain-name-system) information about a domain using the [dig command](https://phoenixnap.com/kb/linux-dig-command-examples).|
|**`dig -x [domain_name]`**|Do a reverse DNS lookup on the domain.|
|**`dig -x [IP_address]`**|Do a [reverse DNS lookup](https://phoenixnap.com/kb/reverse-dns-lookup) of an IP address.|
|**`host [domain_name]`**|Perform an IP lookup for a domain.|
|**`hostname -I`**|Show the local IP address.|
|**`nslookup [domain_name]`**|Receive [information about an internet domain](https://phoenixnap.com/kb/nslookup-command).|

### Variable Commands

Shell variables are a convenient way to store critical data in a reusable format. Below are commands to create, view, and remove variables in the shell.

|Command|Description|
|---|---|
|**`let "[variable_name]=[value]"`**|[Assign an integer value](https://phoenixnap.com/kb/bash-let) to a variable.|
|**`export [variable_name]`**|[Export a Bash variable](https://phoenixnap.com/kb/bash-export-variable).|
|**`declare [variable-name]= "[value]"`**|[Declare a Bash variable](https://phoenixnap.com/kb/bash-declare).|
|**`set`**|List the names of [all the shell variables and functions](https://phoenixnap.com/kb/linux-set).|
|**`unset [variable_name]`**|Remove an environment variable.|
|**`echo $[variable-name]`**|[Display the value](https://phoenixnap.com/kb/echo-command-linux) of a variable.|

### Shell Command Management

Several Linux commands enable managing command execution flow. Schedule commands or create shorter names for lengthy commands.

|Command|Description|
|---|---|
|**`alias [alias-name]='[command]'`**|[Create an alias](https://phoenixnap.com/kb/linux-alias-command) for a command.|
|**`watch -n [interval-in-seconds] [command]`**|[Set a custom interval](https://phoenixnap.com/kb/linux-watch-command) to run a user-defined command.|
|**`sleep [time-interval] && [command]`**|[Postpone the execution](https://phoenixnap.com/kb/linux-sleep) of a command.|
|**`at [hh:mm]`**|Create a job to be executed at a certain time (**Ctrl+D** to exit prompt after you type in the command).|
|**`man [command]`**|[Display a built-in manual](https://phoenixnap.com/kb/linux-man) for a command.|
|**`history`**|Print the [command history](https://phoenixnap.com/kb/linux-history-command) used in the terminal.|

**Note:** Also check out our [Bash commands cheat sheet](https://phoenixnap.com/kb/bash-commands).

### Linux Shell Keyboard Shortcuts

The Linux shell contains several keyboard shortcuts that are important to know. The commands help control the terminal behavior in specific situations. The table below outlines the most important shortcuts.

| Shortcut         | Description                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Ctrl** + **C** | Kill process running in the terminal.                                                                                    |
| **Ctrl** + **Z** | Stop the current process. The process can be resumed in the foreground with **`fg`** or in the background with **`bg`**. |
| **Ctrl** + **W** | Cut one word before the cursor and add it to the clipboard.                                                              |
| **Ctrl** + **U** | Cut part of the line before the cursor and add it to the clipboard.                                                      |
| **Ctrl** + **K** | Cut part of the line after the cursor and add it to the clipboard.                                                       |
| **Ctrl** + **Y** | Paste from clipboard.                                                                                                    |
| **Ctrl** + **R** | Recall the last command that matches the provided characters.                                                            |
| **Ctrl** + **O** | Run the previously recalled command.                                                                                     |
| **Ctrl** + **G** | Exit command history without running a command.                                                                          |
| **`clear`**      | [Clear the terminal screen](https://phoenixnap.com/kb/clear-terminal).                                                   |
| **`!!`**         | Run the last command again.                                                                                              |
| **`exit`**       | Log out of the current session.                                                                                          |

### Saving Dir

| **`pushd .`** | Uses the saved Dir    |
| ------------- | --------------------- |
| **`popd`**    | Saves the current DIr |
![ ](https://www.youtube.com/watch?v=NSt0MTM-BHQ)

Conclusion

The more you use Linux commands, the better you will get at remembering them. Do not stress about memorizing their syntax; use our cheat sheet.

Whenever in doubt, refer to this helpful guide for the most common Linux commands.