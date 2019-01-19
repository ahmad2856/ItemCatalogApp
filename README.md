# Project:  Linux Server Configuration project. 

#Project description
 on this project we will work on configuration and setup on the linux server to deploy Item Catalog App Project.You can visit http://52.56.172.37.xip.io for the App deployed on AWS.  

#Github Repository
https://github.com/ahmad2856/ItemCatalogApp.git
 
#Udacity Reviewer
 SSH Address: 52.56.172.37
 SSH Port: 2200
 UserAccount: grader,Password:123
 UserAccount: root  ,Password:student
 
 
 
#Summary of software you installed
 1-sudo apt-get update
 2-sudo apt-get install python-pip 
 3-sudo apt-get install python3-pip
 4-sudo apt-get install python-flask 
 5-sudo apt-get install apache2 
 6-sudo apt-get install libapache2-mod-wsgi
 7-sudo apt-get install python3-pip
 8-sudo apt-get install libapache2-mod-wsgi
 9-sudo apt-get install libapache2-mod-wsgi
 10-sudo apt-get install python-setuptools
 11-sudo apt-get install postgresql
 12-sudo apt-get install git


# Configuration implementation and steps :
1-Launch The Virtual Machine.

2-Follow the instructions provided to SSH into your server
 a. Use Private Key 
 b. Using putty Application to access to the server you can downloaded from the link :www.putty.org
 c.open the putty app and then click on ssh then auth then  browse to select the private kay.
 d.Click on session then put the ip of the instance: host: 52.56.172.37, username: grader then click on open button.

 
3- Create a new user named grader and give hem permission to sudo 

    a. sudo adduser grader
    b. vim /etc/sudoers
    c. touch /etc/sudoers.d/grader
    d. vim /etc/sudoers.d/grader, type in grader ALL=(ALL:ALL) ALL, save and quit

4-Set SSH login using the keys
   a.generate keys on local machine usingssh-keygen  then save the private key in ~/.ssh on the local machine

   b.deploy public key on developement enviroment

      On you virtual machine:

      $ su - grader
      $ mkdir .ssh
      $ touch .ssh/authorized_keys
      $ vim .ssh/authorized_keys

      Copy the public key generated on your local machine to this file and save

      $ chmod 700 .ssh
      $ chmod 644 .ssh/authorized_keys

    c.reload SSH using service ssh restart

    d.now you can use ssh to login with the new user you created

       ssh -i key grader@52.56.172.37


5.Update all currently installed packages by using the bellow commands:
  a.sudo apt-get update
  b.sudo apt-get upgrade
 
 
 
 6.Change the SSH port from 22 to 2200 by using the bellow commands:
 
  a. Use sudo vim /etc/ssh/sshd_config and then change Port 22 to Port 2200 then  save and quit
  b. Reload SSH using: sudo service ssh restart.


7.Configure the Uncomplicated Firewall
 Configure the Uncomplicated Firewall to only allow the incoming connections for SSH port 2200 and HTTP port 80 and NTP port 123 by using the below commands: 
  a.sudo ufw allow 2200/tcp
  b.sudo ufw allow 80/tcp
  c.sudo ufw allow 123/udp
  d.sudo ufw enable 


8.Configure the local timezone to UTC by using the bellow commands:
 a.Configure the time zone sudo dpkg-reconfigure tzdata


9.Install and configure Apache to serve a Python mod_wsgi application by using the below commands: 
  1-Install Apache sudo apt-get install apache2
  2-Install mod_wsgi sudo apt-get install python-setuptools libapache2-mod-wsgi
  3-Restart Apache sudo service apache2 restart
  4-sudo ufw allow 'Apache Full'
  
10.Install and configure the PostgreSQL by using the below instructions: 

   a.Install PostgreSQL using: sudo apt-get install postgresql

   b.Check if no remote connections are allowed sudo vim /etc/postgresql/9.3/main/pg_hba.conf

   c.Login as user "postgres" sudo su - postgres

   d.Get into postgreSQL shell psql
   e.Create a new database named catalog and create a new user named catalog in postgreSQL shell
      1.postgres=# CREATE DATABASE catalog;
      2.postgres=# CREATE USER catalog;
 
   f.Set a password for user catalog
      postgres=# ALTER ROLE catalog with the password ;

   g.Give user "catalog" permission to "catalog" application database
    postgres=# GRANT ALL PRIVILEGES ON DATABASE catalog TO catalog;

   h.Quit postgreSQL 
    postgres=# \q  then exit. 


11.installing git and clone and setup the ItemCatalogApp            

    a. Install Git using sudo apt-get install git
    b. Use cd /var/www to move to the /var/www directory
    c-Create the application directory sudo mkdir ItemCatalogApp - the final path of the project folder should be /var/www/ItemCatalogApp/ItemCatalogApp
    d-Move inside this directory using cd ItemCatalogApp
    e-Clone the ItemCatalogApp to the virtual machine git clone https://github.com/ahmad2856/ItemCatalogApp.git
    f-Rename the project name sudo mv ./ItemCatalogApp ./ItemCatalogApp
    g-Move to the inner ItemCatalogApp directory using cd ItemCatalogApp
    h-Rename app.py to application.py using sudo mv website.py application.py
	i-Edit application.py and change client_secrets.json to /var/www/ItemCatalogApp/ItemCatalogApp/client_secrets.json
    j-Install pip sudo apt-get install python3-pip 
    k-Use pip to install dependencies sudo pip3 install -r requirements.txt
    l-Install psycopg2 sudo apt-get -qqy install postgresql python-psycopg2
    m-Create database schema sudo python3 database_setup.py



12.Configure and Enabling a New Virtual Host
 a.Create ItemCatalogApp.conf to edit: sudo nano /etc/apache2/sites-available/ItemCatalogApp.conf.
 b.Add the following lines of code to the file to configure the virtual host.

    <VirtualHost *:80>
	ServerName 52.56.172.37
	ServerAdmin test@test.com   
	WSGIScriptAlias / /var/www/ItemCatalogApp/ItemCatalogApp.wsgi
	<Directory /var/www/ItemCatalogApp/ItemCatalogApp>
		Order allow,deny
		Allow from all
	</Directory>
	Alias /static /var/www/ItemCatalogApp/ItemCatalogApp/static/
	<Directory /var/www/ItemCatalogApp/ItemCatalogApp/static>
		Order allow,deny
		Allow from all
	</Directory>
	ErrorLog ${APACHE_LOG_DIR}/error.log
	LogLevel warn
	CustomLog ${APACHE_LOG_DIR}/access.log combined
    </VirtualHost>

 3-Enable the virtual host with the following command: sudo a2ensite ItemCatalogApp

 13.Create the .wsgi File
   1-Create the .wsgi File under /var/www/ItemCatalogApp/ItemCatalogApp:
       1.cd /var/www/ItemCatalogApp/ItemCatalogApp
       2.sudo nano ItemCatalogApp.wsgi
	   
   2-Add the following lines of code to the ItemCatalogApp.wsgi file:
   
      #!/usr/bin/python
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0,"/var/www/ItemCatalogApp/ItemCatalogApp")

    from ItemCatalogApp import app as application
	application.root_path = '/var/www/ItemCatalogApp/ItemCatalogApp'
	application.secret_key = 7uJB826hk2ltUZmdsYbsGHiN


   14.Restart Apache and run the ItemCatalogApp
    a. sudo service apache2 restart



	List of third-party resources that help me on these configurations : 
	a.Udacity tutorials video.  
	a.Stack overflow web site.
	b.Google search engine.
	c.http://flask.pocoo.org/docs/1.0/deploying.







