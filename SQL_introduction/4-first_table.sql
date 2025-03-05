-- A scripting creating a table called 'first_table'
-- Recreated the previously deleted hbtn database
-- columns: id(INT), name(VARCHAR(256))

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
