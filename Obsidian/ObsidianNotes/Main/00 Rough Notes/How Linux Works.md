---
created:
  - 2025-03-25 21:46
aliases:
  - "Book: How Linux Works"
tags:
  - BookType/
  - BookType/linux
  - BookType/bash
---
---
id: How
created_date: 2025-03-25
updated_date: 2025-03-25
type: book
year: 
author: Brian Ward
link:

# 📚 How Linux Works
- **🏷️Tags** :   #03-2025 #book #book/current 




## ❓ Questions
---
- mknod function whats it do? 
	- pg 56
- 

## 🔗 Related links---
[[Books#^c3d91b| How Linux Works PDF]]

## 📝 Notes
---



### Chapter 1 "The Big Picture"
- [CH 1 Link](obsidian://open?vault=ObsidianNotes&file=Main%2F01%20Source%20Material%2FBooks%2Foperating_systems%2FHow%20Linux%20Works%20What%20Every%20Superuser%20Should%20Know%203rd%20Edition%20by%20Brian%20Ward.pdf#page=27)
- linux abstraction layers
	- User Processes
		- GUI
		- Servers
		- Shell
	- Linux kernel
		- System Calls
		- Process Management
		- Memory Management
		- Devices Drivers
	- Hardware 
		- Cpu
		- Ram 
		- Disk 
		- Network Parts
	
### Chapter 2 "Basic Commands and Directories"
-  [CH 2 Link](obsidian://open?vault=ObsidianNotes&file=Main%2F01%20Source%20Material%2FBooks%2Foperating_systems%2FHow%20Linux%20Works%20What%20Every%20Superuser%20Should%20Know%203rd%20Edition%20by%20Brian%20Ward.pdf#page=37)
- Bourne Shell
	- /bin/sh = Bourne Shell
- Commands
	- [[Linux Commands List]]
- Moving In CLI
	- CTRL-B Move the cursor left
	- CTRL-F Move the cursor right 
	- CTRL-P View the previous command (or move the cursor up)
	- CTRL-N View the next command (or move the cursor down) 
	- CTRL-A Move the cursor to the beginning of the line 
	- CTRL-E Move the cursor to the end of the line
	- CTRL-W Erase the preceding word 
	- CTRL-U Erase from cursor to beginning of line 
	- CTRL-K Erase from cursor to end of line 
	- CTRL-Y Paste erased text (for example, from CTRL-U)
- Background Processes
	- Stop Process
		- Press CTL-Z
	- Start Process
		- Enter: fg
			- "foreground
- Find
	- $find dir - name *file* -print
- Man Sections
	1. User Commands
	2. Kernel system calls
	3. Higher-Level unix Programing Library Documentation
	4. Device Interface and Driver information
	5. File description
	6. Games
	7. File formats, conventions and encoding (ACSII, suffixes, and so on)
	8. System commands and Servers

### Chapter 3 "Devices"
- Device Files
	- Block devices
		- Programs access data from a block device in fixed chunks. The sda1 in
			the preceding example is a disk device, a type of block device. Disks can
			be easily split up into blocks of data. Because a block device’s total size
			is fixed and easy to index, processes have quick random access to any
			block in the device with the help of the kernel.
	- Character device
		- Character devices work with data streams. You can only read characters
			from or write characters to character devices, as previously demonstrated
			with /dev/null. Character devices don’t have a size; when you read from or
			write to one, the kernel usually performs a read or write operation on it.
			Printers directly attached to your computer are represented by character
			devices. It’s important to note that during character device interaction,
			the kernel cannot back up and reexamine the data stream after it has
			passed data to a device or process.
	- Pipe device
		- Named pipes are like character devices, with another process at the other
			end of the I/O stream instead of a kernel driver.
	- Socket deviceImportant dd options
		- Sockets are special-purpose interfaces that are frequently used for
			interprocess communication. They’re often found outside of the /dev
			directory. Socket files represent Unix domain sockets; you’ll learn more
			about those in Chapter 10.
- dd and devices
	- if=file
		- The input file. The default is the standard input.
	- of=file
		- The output file. The default is the standard output.
	- bs=size 
		- The block size. dd reads and writes this many bytes of data at a
	- 
- udev
	- Hard disk
		- sd*
			- sd == scisi disk
		- partitions 
			- sd*1,2,3...
		- lsscsi
			- list script devices
- 
	- 
	- devtmpfs