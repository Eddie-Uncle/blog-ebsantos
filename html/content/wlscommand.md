Title: WebLogic Commands!!
Date: 2018-01-27 14:05
Category: Technology
Tags: WebLogic, Oracle, SysOps, DevOps, Middleware
Slug: WebLogic Skyrocking
Authors: Edson Santos



##WebLogic Hacks

**Decrypt or Encrypt passwords**

Extract - wlsdecrypt usage
	 
You must copy $WLS-DOMAIN-HOME/security folder first, then run the command below inside this folder.
	 
	 Decrypt
	 /opt/oracle/Middleware/Oracle_Home/wlserver/common/bin/wlst.sh wlsdecrypt.py boot.properties or
	 
	 Encrypt
	 /opt/oracle/Middleware/Oracle_Home/wlserver/common/bin/wlst.sh wlsencrypt.py boot.properties
	 
Of course, you must have these scripts working. 
	 
You can download them from here:

<a href="https://github.com/Eddie-Uncle/Decrypt-WLS-passwords/" target="_blank">Uncle Eddie Git Hub - WLS Decrypt and Encrypt passwords</a>



**WEBLOGIC PATCHES**

Tool : BSU (Previously BEA)

*Windows*

	Installing

	C:\bea\utils\bsu>bsu.cmd -prod_dir=c:\bea\weblogic92 -patch_download_dir=D:\pat -patchlist=2LYV -verbose -install -log=D:\pat\pat.txt -log_priority=trace

*Linux*

	Installing

	cd /u01/middleware/oracle/appserver/BPMDomain/utils/bsu/
	./bsu.sh -prod_dir=/u01/middleware/oracle/appserver/BPMDomain/wlserver_10.3 -patch_download_dir=/u01/middleware/oracle/appserver/BPMDomain/utils/bsu/cache_dir -patchlist=S28A -verbose -install

	Removing

	cd /u01/middleware/oracle/appserver/BPMDomain/utils/bsu/./bsu.sh -prod_dir=/u01/middleware/oracle/appserver/BPMDomain/wlserver_10.3 -patchlist=YUIS -verbose -remove

	Verbose Listing patches applied

	./bsu.sh -prod_dir=/u01/middleware/oracle/appserver/SOADomain/wlserver_10.3 -status=applied -verbose -view

Tool : OPatch - (Oracle Patch)

	./opatch lsinventory -invPtrLoc /products/oracle/wls1036/osb11116/oraInst.loc
	
	./opatch apply -invPtrLoc /products/oracle/wls1036/osb11116/oraInst.loc


##Useful Links
**WEBLOGIC WLST COMMANDS**

<a href="http://docs.oracle.com/cd/E28271_01/web.1111/e13813/custom_soa.htm" target="_blank">Custom SOA Suite - WLST Scripting Commands</a>

<a href="https://blogs.oracle.com/weblogicserver/" target="_blank">Oficial WebLogic Server Blog</a>




**nmEnroll - NodeManager**

	Set the Environment
	/products/oracle/wlp1002/wlserver_10.0/common/bin/wlst.sh
	
	Example 1:
	connect('weblogic','37a6ef686f','t3://192.168.0.67:60000')
	nmEnroll('/home/ndmgr/clustdomain','/home/ndmgr')
	exit(

	Example 2:
	connect("weblogic","d5e58b2f92","t3://10.3.172.43:51000")
	nmEnroll("/domains/HmlBUS")
	
	
**START UP SCRIPT**

nohup ./startWebLogic.sh &>/logs/WLSDomain/ServerAdm_64000.out &
echo "WLSDomain - Starting UP the ADMIN Server - ServerAdm_64000: /logs/WLSDomain/ServerAdm_64000.out"

DEBUG FLAGS

	-Dweblogic.StdoutDebugEnabled=true

	-Dssl.debug=true
	

##Java 

Verify and count a specific  java class

	grep com.b2w.controlpanel.exception.ServiceException server_log.out | wc -l
	11466


	grep <com.b2w.controlpanel.exception.ServiceException <log.out | wc -l>
	Results:

*Setting up Home Directories*

ORACLE_HOME (Oracle XE)

	export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe
	export ORACLE_SID=XE
	export ORACLE_BASE=/u01/app/oracle
	export PATH=$ORACLE_HOME/bin:$PATH

ANT

	export ANT_HOME=/home/weblogic/SCRIPTS/apache-ant-1.9.4
	export PATH=$ANT_HOME/bin:$PATH

JAVA_HOME

	export JAVA_HOME=/products/java7
	export PATH=$JAVA_HOME/bin:$PATH
	export PATH=$JRE_HOME/bin:$PATH

	export JAVA_HOME=/products/jvm/java8
	export PATH=$JAVA_HOME/bin:$PATH
	export PATH=$JRE_HOME/bin:$PATH

	export JAVA_HOME=/oracle/wls11g/jrockit-jdk1.6.0_37-R28.2.5-4.1.0
	export PATH=$JAVA_HOME/bin:$PATH
	export PATH=$JRE_HOME/bin:$PATH


**THREAD CONFIGURATION**

WEBLOGIC JVM THREADPOOL CONFIGURATION

	-Dweblogic.threadpool.MinPoolSize=300


**THREAD POOL SIZE - weblogic**

	-Dweblogic.threadpool.MinPoolSize=300


**THREAD DUMP - WEBLOGIC**

	/app/bea/jrockit-R27.5.0-jdk1.5.0_14/bin/jrcmd 31786 print_threads

	/products/jvm/jrockit-jdk1.6.0_45-R28.2.7-4.1.0/bin/jrcmd 25817 print_threads

	/bea/java6/bin/jrcmd 27287 print_threads

	/oracle/wls11g/Oracle/Middleware/jrockit_160_29_D1.2.0-10/bin/jrcmd 15470 print_threads > /home/weblogic/print.txt

	


*PRE REQ ORACLE DB 11g INSTALLATION - RED HAT LINUX 6 *

	yum install oracle-rdbms-server-11gR2-preinstall
	
