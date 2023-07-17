# 0x00. MySQL advanced
## Requirements
### General

    - All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
    - All files should end with a new line
    - All SQL queries have a comment just before (i.e. syntax above)
    - All files start by a comment describing the task
    - All SQL keywords be in uppercase (SELECT, WHERE…)
    - A README.md file, at the root folder of the project
    - The length of your files will be tested using wc

### Use “container-on-demand” to run MySQL

$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$

### How to import a SQL dump

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
