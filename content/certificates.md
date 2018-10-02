Title: Certificates
Date: 2018-02-02 01:00
Category: Technology
Tags: Certificates, Linux, keytool
Slug: Certificates
Authors: Edson Santos

# **Working with Certificates**

**Import certificate - Using Java keytool**

	keytool -import -alias mundipagg -file CA_b2w_cert_test.cer -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass changeit -trustcacerts

	./keytool -import -alias neogrid -file  webedi_neogrid_com.cer -keystore $JAVA_HOME/jre/lib/security/cacerts -storepass changeit -trustcacerts

	./keytool -import -alias mundipaggbase64 -file MundiPaggOne_Base64_X509.cer -keystore cacerts -storepass changeit -trustcacerts


**Listing Certificates**

	./keytool -list -v -keystore $JAVA_HOME/jre/lib/security/cacerts

**Delete certificates on keystore!**

	keytool -delete -alias server1.domain.com -keystore server_keystore.jks

**DOWNLOAD CERTIFICATE CHAIN AND INPUT INTO A FILE** 

	echo "" | openssl s_client -connect smartwalletstaging.mundipaggone.com:443 -showcerts 2>/dev/null | openssl x509 -out certificado_do_site.cer
