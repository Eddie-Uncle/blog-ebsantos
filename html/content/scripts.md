Title: Simple Scripts!
Date: 2018-02-02 01:01
Category: Technology
Tags: Linux, Unix, OS, shell, scripts, devops
Slug: Scripts
Authors: Edson Santos

**Backup using shell script (this example weblogic domain)**

	DATA=`date +%Y-%m-%d-%H.%M`
	tar -zcvf  /repo/bpel/backup/BPEL/backup-config-"$DATA".tar.gz /domains/BPEL/config
	tar -zcvf  /repo/bpel/backup/BPEL/backup-security-"$DATA".tar.gz /domains/BPEL/servers/bwBPEL_Admin/security
	tar -zcvf  /repo/bpel/backup/BPEL/backup-ldap-"$DATA".tar.gz /domains/BPEL/servers/bwBPEL_Admin/data/ldap
	clear
	echo "Backup successfully..."
	exit

**CLEAN LOG - SCRIPT**

	[weblogic@snake001]$ cat limpa.sh
	cat /dev/null > /logs/HmlWLS/BusCloud_60101.log;
