RESTORE DATABASE MuOnline
FROM DISK = '/sqlserver/MuOnline.bak'
WITH MOVE 'MuOnlineS6' TO '/var/opt/mssql/data/MuOnline.mdf',
     MOVE 'MuOnlineS6_Log' TO '/var/opt/mssql/data/MuOnline_log.ldf',
     REPLACE;
