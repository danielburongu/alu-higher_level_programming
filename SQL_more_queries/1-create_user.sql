--  creates the MySQL server user 
--  Root user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PERMISSIONS ON *.* TO user_0d_1@localhost
