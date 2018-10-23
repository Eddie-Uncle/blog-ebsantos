Title: WebServers
Date: 2018-02-02 01:15
Category: Technology
Tags: Linux, Unix, OS, sysadmin, devops, Apache, NGINX
Slug: ApacheNginx
Authors: Edson Santos

#Apache
**Apache Example** (Configs may vary, depends on each case - Basic overview)

	REVERSE PROXY - APACHE
	<VirtualHost *:80> 
	ProxyPreserveHost On
	ProxyRequests Off
	ServerName www.example.com
	ServerAlias example.com
	ProxyPass / http://localhost:8080/example/
	ProxyPassReverse / http://localhost:8080/example/
	</VirtualHost> 
	
	
	
#NGINX

**Simple upstream backend Load Balance Configuration**

  	 upstream backend {
     server 192.168.1.4 fail_timeout=10s;
     server 192.168.1.7 fail_timeout=10s;
  	 }

   	server {
    	 location / {
     	 proxy_pass http://backend;
    	 }
	}