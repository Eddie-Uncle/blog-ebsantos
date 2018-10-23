Title: The Docker Ninja!
Date: 2018-02-07 01:50
Category: Technology
Tags: Devops, Containers, SysOps
Slug: Dockercommand
Authors: Edson Santos

#Docker Resource Kit

*Installing Docker*

	RedHat --> yum -y install docker;
	Ubuntu --> apt install docker;
	MacOS --> brew install docker;
	
*Istalling Docker Compose*

Find below the link with instructions:

**<a href="https://docs.docker.com/compose/install/" target="_blank">Docker Compose Install</a>**

*Important tip, always check if you have your Docker Repo updated*

	/etc/yum.repos.d/docker.repo	(RHEL)

*Containers - Downloading Images and Creating containers*

	docker run -dit ubuntu:latest

*Containers operational cycle*

	docker ps -a (List all containers created)
	docker start $(docker ps -a -q)
	docker stop $(docker ps -a -q)
	docker rm $(docker ps -a -q)

*Containers = per Status*

	docker start $(docker ps -aq -f status=exited)
	docker rm $(docker ps -aq -f status=exited)
	sudo docker ps -a | grep exited | cut -d ' ' -f 1 | xargs sudo docker rm


*Docker  removing Images - Docker rmi*

Usage:

	docker rmi $( sudo docker images | grep ‘'image_name'' | tr -s ' ' | cut -d ' ' -f 3)

Images = grep string gcr = google

	docker rmi $( docker images | grep 'gcr' | tr -s ' ' | cut -d ' ' -f 3)


Images = grep string doc = docker

	docker rmi $( docker images | grep ‘docker' | tr -s ' ' | cut -d ' ' -f 3)


**Saving Images**

COMMIT savings into an image

	First, create a container from any pulled image!
	
	docker run -it 'base_image' /bin/bash
	
	Make the necessary changes (Install updates and softwares you wish)

	Example: 
	yum -y upgrade && yum -y update
	yum install httpd (RHEL)
	RUN apt-get update && apt-get install -y props (Ubuntu)
	RUN apt-get update && apt-get install -y iputils-ping (Ubuntu)

	Commit it with a new name Image.

	docker commit 'hash tag of running container' new_image 


##Installing Products (images) with Docker

**WordPress Stack**

*mariaDB (SQL Database)*

	docker run -e MYSQL_ROOT_PASSWORD=mariadb -e MYSQL_DATABASE=wordpress --name wordpressdb -v “$PWD/database":/var/lib/mysql -d mariadb:latest

*Wordpress*

	docker run -e WORDPRESS_DB_PASSWORD=mariadb --name wordpress --link wordpressdb:mysql -p 0.0.0.0:80:80 -v "$PWD/html":/var/www/html -d wordpress

	variables
	MYSQL_ROOT_PASSWORD='db_password'
	MYSQL_DATABASE='name_database'

**Splunk**

	Example1:
	docker run --name splunkwls --hostname splunk01 -p 8000:8000 -e "SPLUNK_START_ARGS=--accept-license" -v "$PWD/opt":/opt/splunk/var splunk/splunk:latest

	Example2:
	docker run -d --name splunkwls --hostname splunk01 -p 8000:8000 -e "SPLUNK_START_ARGS=--accept-license" -v /opt/oracle/Middleware/domains/snake01/servers:/mnt/splunk splunk/splunk

	user=passwd: admin/admin01

	Example:
	Vars = /host/directory:/container/directory 

**HTTPD - APACHE**

DOCKER HTTPD IMAGE - as reference (only)

	docker pull http

	docker run -dit --name my-apache-app -v "$PWD":/usr/local/apache2/htdocs/ -p 8000 httpd:2.4

	docker run -dit —name my-apache-app -v "$PWD":/usr/local/apache2/htdocs/ -p 192.168.1.4:80:9000 httpd:2.4


**RANCHER** --> Amazing Product!

	docker run -d --restart=unless-stopped -p 8080:8080 rancher/server:stable 

	docker run -d --restart=unless-stopped -p 8080:8080 rancher/server:preview


**UBUNTU**

	docker pull ubuntu:latest

	docker run -it -p 8080:80 -p 4443:443 —name 'containername' 'containerimage' ubuntu:latest /bin/bash


**Jira - Docker**

	https://hub.docker.com/r/blacklabelops/jira/

	docker run -d -p 8080:8080 -v jiravolume:/var/atlassian/jira --name bernardojira blacklabelops/jira


**DOCKER WEBLOGIC 12.2.1.3**

Copy and paste below:

	docker run -d  —name b-001wls -p 7001:7001 -e ADMIN_USERNAME=weblogic -e ADMIN_PASSWORD=welcome1 -e DOMAIN_HOME=/u01/oracle/user_projects/domains/b001_domain -e DOMAIN_NAME=b001_domain oracle/weblogic:12.2.1.3-generic 

**DOCKER & RED HAT**

*Installing DOCKER CE (Community Edition on Red HAT Enterprise)*


*Container SELINUX*

	yum install -y http://mirror.centos.org/centos/7/extras/x86_64/Packages/container-selinux-2.33-1.git86f33cd.el7.noarch.rpm

	Package Name: container-selinux-2.33-1.git86f33cd.el7.noarch.rpm


**DOCKER MACHINE**
Driver: VirtualBox (Oracle)

	docker-machine create -d virtualbox rancher01

	docker-machine create -d 'drive : virtualbox, vmware, cloud 'virtual machine name'


**SysDig**

docker run -d --name sysdig-agent --privileged --net host --pid host -e ACCESS_KEY=YOUR_ACCESS_KEY -v /var/run/docker.sock:/host/var/run/docker.sock -v /dev:/host/dev -v /proc:/host/proc:ro -v /boot:/host/boot:ro -v /lib/modules:/host/lib/modules:ro -v /usr:/host/usr:ro sysdig/agent

*Docker inspect feature*
	
	docker inspect 'CONTAINER ID' | grep -w "IPAddress" | awk '{ print $2 }' | head -n 1 | cut -d "," -f1


##Troubleshooting Docker

**Get systemd (RedHat/CentOS) working properly after import from Docker Image**

If you've been running into problems to use **systemd** on centOS 7 images from docker hub or any other container repository, you might would like to get rid of them, right?

Find below the the steps you should use to fix it.

You must have pulled off from an image of Docker hub, I'd suggest the link below:

<a href="https://hub.docker.com/r/_/centos/" target="_blank">Official Docker Hub CentOS</a>

Once you checked, you should type the command in your shell or command prompt just in case using Windows OS

**docker pull centos**

So, once you have done that, you have downloaded the centos image from docker hub, now you must run your container like this:

**docker run -dit --name 'container_name' -p 'hostipmachine':80:80 --privileged -ti -e "container=docker" -v /sys/fs/cgroup:/sys/fs/cgroup -v "$PWD/html":/var/www/html dockerimage:latest /usr/sbin/init**

Basically, you are informing the container type (which is docker) and after that, you should able to use systemd in your container. Additionally, in the example above, we are setting the port -p and sharing the volume between the host and the container


**Go ahead and take a look yourself at DockerFiles, Docker Swarm, Docker Compose**

Cheers...

	
