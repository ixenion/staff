# Install postgresql client to connect to postgresql db
sudo apt install postgresql-client-12 (4.5kB)

# Install postgresql server
sudo apt install postgresql (117mB)


# enable/disable
systemctl enable/disable postgresql
systemctl start/stop postgresql


# Connect to postgresql to check that's all right
sudo -u postgres psql -c "SELECT version();"
# OUTPUT:
												version                                         
-------------------------------------------------------------------------------------------------
PostgreSQL 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0, 64-bit
(1 row)

# Setup default user (postgres) password
https://chartio.com/resources/tutorials/how-to-set-the-default-user-password-in-postgresql/
sudo -u postgres psql -c "ALTER USER postgres PASSWORD '0000';"

# Create new user
$ psql -h localhost -U postgres
create user arix with encrypted password '0000';

# Create new admin user
$ psql -h localhost -U postgres
CREATE ROLE dummy WITH LOGIN SUPERUSER PASSWORD '123456';

# Delete user
$ sudo su - postgres
$ dropuser <username> -e

# Create DB
$ psql -h localhost -U postgres
create database shop;

# Assign DB to user
$ psql -h localhost -U postgres
grant all privileges on database shop to arix;

# Connect to the db
psql -h localhost -U arix -d shop -W
-h	hostname
-U	Username
-d	DBname
-W	Force passwort prompt



#######################
###### SEQUENCES ######
#######################

\q				exit
\c <db-name>	switch db (or '\connect <db-name>' )
\d				show table relations

