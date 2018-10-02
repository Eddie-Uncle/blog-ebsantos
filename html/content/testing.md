Title: Testing and Text Downloads!
Date: 2018-02-01 01:10
Category: Technology
Tags: Linux, Unix, OS, sysadmin, devops, Testing, SOAPUI
Slug: Testing
Authors: Edson Santos

**USING CURL**

	curl -i http://company-stock-v2.elasticbeanstalk.com/stock/111895943?storeId=13933305000106

	curl -i -X POST -H "Content-Type:application/xml" -d '<movementRequestJson><sku>3213219</sku><seller>13933305000106</seller><totalQuantity>1</totalQuantity><leadTime>0</leadTime><subInventory>9801</subInventory><warehouse>98</warehouse><stockType>FISICO</stockType></movementRequestJson>' http://company-stock-v2.elasticbeanstalk.com/stock;
	
	
**Using WGET - This case downloading JDK 1.8u51 from Oracle**

	wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz"

Find below for more examples: 

<a href="https://stackoverflow.com/questions/10268583/downloading-java-jdk-on-linux-via-wget-is-shown-license-page-instead/" target="_blank">StackOverflow about WGET usage, very complete</a>

**SOAPUI**

One of the tools that I've been working with over the years is **Smart Bear SOAPUI**.

You can test, WSDL's, Restful API's, WebServices Endpoints, JMS workloads, simulate HTTP workload, work with payloads, anyways, unique tool!

Find below the link for further information:

<a href=?https://smartbear.com/" target="_blank">Smart Bear WebPage</a>


	
