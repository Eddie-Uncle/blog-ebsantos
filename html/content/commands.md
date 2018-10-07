Title: Linux Hacks and Command Line!
Date: 2018-07-22 01:20
Category: Technology
Tags: Linux, OS, sysadmin, devops, curl, wget, Certificates, Keytool, SoapUI, Shell, Script, Git
Slug: Linuxcommand
Authors: Edson Santos


# Linux Command Line Resource Kit


**SYSTEMCTL (RedHat/CentOS) usage** 

To enable or disable services automatically on CentOS or RedHat Flavors.

	systemctl disable httpd
	systemctl enable docker
	systemctl status kubelet

*Hostnamectl*

	hostnamectl command : Control the system hostname.

*nmtui*
	
	nmtui command : Control the system hostname and other network settings using text user interface (NMTUI).

*`*
	
	nmcli command : Exhibits information about your network device
	nmcli device show 
	nmcli dev status
	nmcli con up <profile_name>
		Example: nmcli con up 5G (previously created with nmtui)
	
*timedatectl*

	timedatectl command: Exhibits information about timezone and date of the system.	
	
*Kill other user session*

sudo pkill -9 -u username	

Find below fewer examples about it:

<a href="https://www.cyberciti.biz/faq/howto-kill-unix-linux-user-session/" target="_blank">User Management Session</a>
	
*Link to change the timezone* (CentOS)

<a href="https://linuxacademy.com/blog/linux/changing-the-time-zone-in-linux-command-line/" target="_blank">Linux Academy Changing the timezone in your system</a>

#Security

**SELINUX APACHE**

	semanage port -l | grep http
	semanage port -a -t http_port_t -p tcp 80
	
**Working with Native CENTOS 7 Firewall**
	
	sudo firewall-cmd --zone=public --add-service=http --permanent
	sudo firewall-cmd --zone-public --add-port=8080/tcp --permanent
	sudo firewall-cmd --zone=public --list-services
	rpm qa | grep firewalld

		
#Files handling
**LSOF usage and examples**


	echo "OpenSockets="$(/usr/sbin/lsof | grep -i weblogic | wc -l) > 	results.txt
 
	/usr/sbin/lsof | grep -i weblogic

	/usr/sbin/lsof | grep -i weblogic | grep -i deleted
	and then kill stuck pid's!

	/usr/sbin/lsof  | grep weblogic | awk '{ print $3 }' | sort -u
	
**How to check too many open files**

	lsof -u weblogic | wc -l

	[root@ares ~]# cat /proc/sys/fs/file-max
	65536

	/usr/sbin/lsof | grep weblogic | awk '{ print $2 }' | sort -u


**AWK and CUT usage**

	ps -ef | grep java | awk ‘{ print $2 }’ | sort -u | xargs kill -9
	
	ps - ef | grep java | cut -d " " -f2 | xargs kill -9
	
	ps -ef | grep weblogic | awk '{ print $2 }' | sort -u | xargs kill -9
	
	kill -9 $(ps auwwwx | grep -i -E "jboss|weblogic|websphere" | grep -v grep | awk '{ print $2 }')
	
**SED**

	sed -i 's/10.13.0.87/10.13.0.193/g' *.xml
	sed -i ’s/8080/8080/g' *.xml
	sed -i 's/server01:10110/server02:60101/g' appconfig.properties

**FOR LOOP USAGE**

	for x in `cat name_file`;do echo $x;done
 
	for x in `cat name_file`;do ssh -q $x;done
	
	for i in `cat file.txt` ; do ping -c1 $i 2>&1 | tee >> ping-	output.txt; done
	
	(Creating serveral files at a glance)
	
	for i in {1..9}; do touch  kubn40${i}.sh; done
	usage: for i in {range..}; do command filename$${i}.txt; done
	for i in {1..9}; do cat kubn410.sh >>  kubn40${i}.sh; done
	
	
	
**GREP USAGE** 
 
	grep <search> <file> | awk '{print $1}' >> <new_file_output>.txt
	
	example: grep -ir Carrefour *.sh | awk '{print $1}' >> search.txt
	
	

**DU Usage**

	du -sk * | sort -n

	du -sh /logs/* | sort -nr | grep G

**FIND Usage**

       find . -size +50M
       find / -type f -name "index.php"
       find / -type f -name "*.log" -size +1M
       find / -type f -name "*.log" -size +1M | xargs rm -rf {} \;
      

**Quick GREP and Tailing Logs (examples)**

	tail -f *.out | grep "Socket read timed out" | wc -l
	tail -f *.out | grep "Socket read timed out" --color
	tail -f *.out | grep "error" --color

	cat bwbpelsp02_01-yyyy-MM-dd-HH-mm.log | grep "Socket read timed	out" | wc -l

	tail -f *.out | egrep -i 'ERR|ORA-|OVERL|SUSPEN'
	tail -f *.out | egrep -i 'STUCK'

**THREAD COUNT BY USER**
 
		ps -uweblogic -lf | wc -l
		ps -uapache -lf | wc -l
		ps -unginx -lf | wc -l

**Verify and count a specific java class**

	grep com.yourcompany.product.exception.ServiceException log.out | wc -l 
	result = 11466

**DMESG** (old fashion)

	[root@bwsubacat04 sitecontent]# dmesg | grep file-max
	VFS: file-max limit 65536 reached
	VFS: file-max limit 65536 reached


**ENCODE LINUX**

	echo $LANG


**LIMITS - SO LINUX (CENTOS 6)**

	LIMITS
	echo '###WEBLOGIC###' >> /etc/security/limits.conf
	echo 'weblogic  soft nproc 20000' >> /etc/security/limits.conf
	echo 'weblogic  hard nproc 20000' >> /etc/security/limits.conf
	echo 'weblogic  soft nofile 65536' >> /etc/security/limits.conf
	echo 'weblogic  hard nofile 65536' >> /etc/security/limits.conf
	echo 'weblogic  soft memlock 16384000' >> /etc/security/limits.conf
	echo 'weblogic  hard memlock 16384000' >> /etc/security/limits.conf

**IFCONFIG MTU**

	ifconfig ib0 | grep MTU; ifconfig ib1 | grep MTU; ifconfig bond0 | grep MTU

**CHECK - LDAP USER**

	getent passwd | grep <user>

**mpstat – Processors Statistics**

	Using mpstat command without any option, will display the Global Average Activities by All CPUs.


**Basic example sudores file** (there are better practices, in this case these users are allowed to excecute as root without password - General overview)

	SUDOERS
	weblogic ALL=(ALL) NOPASSWD: /bin/vi /etc/hosts
	fmwadmin ALL=(ALL) NOPASSWD: /bin/vi /etc/hosts


**CRONTAB**

crontab -l (Exhibits the current crontab created)

crontab -e (Create a crontab under running user)

	# Example of job definition:
	# .---------------- minute (0 - 59)
	# |  .------------- hour (0 - 23)
	# |  |  .---------- day of month (1 - 31)
	# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
	# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR 					sun,mon,tue,wed,thu,fri,sat
	# |  |  |  |  |
	# *  *  *  *  * user-name command to be executed

**Tee usage (similar to echo)**

	tee /etc/yum.repos.d/docker.repo <<-EOF

	
**Obtain PID specific application**

	ps aux | awk -v app='Apache' '$0 ~ app { print $1 }’
	

**Working with Aliases**

	alias
	alias vi='vim'
	alias cp='cp -i'
	alias egrep='egrep --color=auto'
	alias fgrep='fgrep --color=auto'
	alias grep='grep --color=auto'
	alias l.='ls -d .* --color=auto'
	alias ll='ls -l --color=auto'
	alias ls='ls --color=auto'
	alias mv='mv -i'
	alias rm='rm -i'
	alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot --show-tilde’
	
**USING CURL**

	curl -i http://company-stock-v2.elasticbeanstalk.com/stock/111895943?storeId=13933305000106
	
	curl -i https://www.uol.com.br -k

	curl -i -X POST -H "Content-Type:application/xml" -d '<movementRequestJson><sku>3213219</sku><seller>13933305000106</seller><totalQuantity>1</totalQuantity><leadTime>0</leadTime><subInventory>9801</subInventory><warehouse>98</warehouse><stockType>FISICO</stockType></movementRequestJson>' http://company-stock-v2.elasticbeanstalk.com/stock;
	
Examples for CURL usage;

<a href="http://www.codingpedia.org/ama/how-to-test-a-rest-api-from-command-line-with-curl/" target="_blank">Curl and examples GET POST All methods</a>
	
	
	
**Using WGET - This case downloading JDK 1.8u51 from Oracle**

	wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz"

Find below for more examples: 

<a href="https://stackoverflow.com/questions/10268583/downloading-java-jdk-on-linux-via-wget-is-shown-license-page-instead/" target="_blank">StackOverflow about WGET usage, very complete</a>

**SOAPUI**

One of the tools that I've been working with over the years is **Smart Bear SOAPUI**.

You can test, WSDL's, Restful API's, WebServices Endpoints, JMS workloads, simulate HTTP workload, work with payloads, anyways, unique tool!

Find below the link for further information:

<a href=?https://smartbear.com/" target="_blank">Smart Bear WebPage</a>	

**Backup using shell script (this example weblogic domain)**

	DATA=`date +%Y-%m-%d-%H.%M`
	tar -zcvf  /repo/bpel/backup/BPEL/backup-config-"$DATA".tar.gz /domains/BPEL/config
	tar -zcvf  /repo/bpel/backup/BPEL/backup-security-"$DATA".tar.gz /domains/BPEL/servers/bwBPEL_Admin/security
	tar -zcvf  /repo/bpel/backup/BPEL/backup-ldap-"$DATA".tar.gz /domains/BPEL/servers/bwBPEL_Admin/data/ldap
	clear
	echo "Backup successfully..."
	exit
	
**Backup II - Example**

Exclude Example


	echo "Starting Backup"
	DATE=`date +%Y-%m-%d-%H.%M.$$`
	echo "Starting Backup, except *.tar extensions"
	tar -zcvf blog-"${DATE}".tar.gz --exclude='*.tar' .
	if [ "$?" -eq "0" ]
	then
		echo "Backup Successfully..."
		exit 0
	else
		echo "Backup has failed, please check"
		exit 1
	fi

**CLEAN LOG - SCRIPT**

	[weblogic@snake001]$ cat limpa.sh
	cat /dev/null > /logs/HmlWLS/BusCloud_60101.log;
	
	
# **Working with Certificates**

**Import certificate - Using Java keytool**

	keytool -import -alias mundipagg -file CA_b2w_cert_test.cer -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass changeit -trustcacerts



**Listing Certificates**

	./keytool -list -v -keystore $JAVA_HOME/jre/lib/security/cacerts
	
	Example:
	/usr/java/jre1.7.0_80/bin/keytool -list -v  -alias "arizonacert" -keystore /usr/java/jre1.7.0_80/lib/security/cacerts

**Delete certificates on keystore!**

	keytool -delete -alias server1.domain.com -keystore server_keystore.jks

**DOWNLOAD CERTIFICATE CHAIN AND INPUT INTO A FILE** 

	echo "" | openssl s_client -connect smartwalletstaging.mundipaggone.com:443 -showcerts 2>/dev/null | openssl x509 -out certificado_do_site.cer
	
	
**GIT Command line**

**Creating remote repo through command line**

echo "# Test1" >> README.md

git init

git add README.md

git commit -m "first commit"

git remote add origin https://github.com/Eddie-Uncle/Test1.git

git push -u origin master


**VERY IMPORTANT - UNDO LAST PUSH / PULL**

git push -f origin HEAD^:master --> undo last push/pull

git pull -f origin HEAD^:master || git pull -f origin HEAD^:(branch)

**Delete git — Locally**

$ git checkout master #switch to another branch in this case master

$ git checkout -b edsonnewbranch #switched to the branch edsonnewbranch and so on ...
 
$ git branch -d Test_Branch # (Delete locally desired branch)

$ git branch -D Test_Branch # (Delete locally force option)

**Delete git - Remote**

git push origin --delete eddie-branch # (git push origin --delete branch to be deleted)	

**git pull / push commands**

Pulling code from Remote repo to local repo:

git pull origin master || git pull origin edsonnewbranch

Pushing code from Local repo to remote repo:

git push origin master || git push origin edsonnewbranch

**git operations**

git log -p

git status

git show

**git credentials and user settings**

git config --global user.name Eddie-Uncle

git config --global use.email bernardsp@gmail.com

git config --global core.editor vim

git config --global merge.tool vimdiff

git config --list
