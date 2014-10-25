Title: Simple MySQL Backup/Restore
Date: 2004-02-22
Modified: 2012-12-22
Tags: backups, linux
Slug: simple-mysql-backuprestore

To backup:

    $ mysqldump -u username -p -h hostname databasename > filename


And restore:

    $ cat filename | mysql -u username -p -h hostname databasename
