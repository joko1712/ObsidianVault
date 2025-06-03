Is better to take performance metrics from different dbs then to take from different pc configs.

MariaDB - 
PostgreDB -
MySQL -

SQLServer -
Oracle -
Db2 -

Also test different bd file locations
	- HDD
	- SSD
	- External Drive

Also Test on different hardware

tpc-h

Show VARIABLES LIKE 'max_connections';

Set GLOBAL max_connections = **500**;

Max Connections
Buffer pool size
Log Buffer size

Change also the virtual users




Lauch the hammerdb:
`open -a XQuartz`
Then open XQuartz terminal:
`xhost +`
Then in VM terminal:
export DISPLAY=host.docker.internal:0.0
/opt/HammerDB-5.0/hammerdb


ip of machine: host.docker.internal

CONFIGS=(
  "5,5,100,256M,8M"
  "10,10,200,512M,16M"
  "20,20,500,1G,32M"
  "50,20,500,2G,64M"
  "20,5,200,256M,8M"
  "10,10,200,2G,64M"
  "5,20,100,128M,8M"
  "100,50,1000,4G,128M"
)

# Tests:
# MariaDB:

docker run -d --name mariadb-bench \
  -v $(pwd)/my.cnf:/etc/mysql/conf.d/my.cnf \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=tpcc \
  -p 3306:3306 \
  mariadb:latest

docker exec -it mariadb-bench bash
mariadb -u root -p


SHOW VARIABLES LIKE "max_connectios";
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
SHOW VARIABLES LIKE 'innodb_log_buffer_size';

| Test Case | `max_connections` | `buffer_pool_size` | `log_buffer_size` | `virtual_users` | `warehouses` | Test Nº |
| --------- | ----------------- | ------------------ | ----------------- | --------------- | ------------ | ------- |
| Small     | 151               | 1G                 | 16M               | 2               | 10           | 1       |
| Medium    | 151               | 1G                 | 16M               | 5               | 10           | 2       |
| Large     | 200               | 1G                 | 16M               | 2               | 10           | 3       |
| Max CPU   | 200               | 1G                 | 16M               | 5               | 10           | 4       |

## 1:
	DATES: 
			18/05/2025
				Virtual Users: 2
				Wheare houses: 10
				Iterations: 1
				NOPM:27317
				TPM:63435
				
	OS: UBUNTU
	Drive: SSD
	Max_connections = 151
	Buffer Pool size = 1G
	Log Buffer size = 16MB
	
![[Pasted image 20250518190436.png]]


## 2:
	DATES: 
			18/05/2025
				Virtual Users: 5
				Wheare houses: 10
				Iterations: 1
				NOPM: 32809
				TPM: 75921
	OS: UBUNTU
	Drive: SSD
	Max_connections = 151
	Buffer Pool size = 1G
	Log Buffer size = 16MB
	
![[Pasted image 20250518191824.png]]

## 3:
	DATES: 
			19/05/2025
				Virtual Users: 2
				Wheare houses: 10
				Iterations: 1
				NOPM: 27250
				TPM: 63390
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 1G
	Log Buffer size = 16MB

![[Pasted image 20250519113507.png]]

## 4:
	DATES: 
			19/05/2025
				Virtual Users: 5
				Wheare houses: 10
				Iterations: 1
				NOPM: 34419
				TPM: 79599
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 1G
	Log Buffer size = 16MB

![[Pasted image 20250519114754.png]]


# Now let's compare with others:

| Test Case | `max_connections` | `buffer_pool_size` | `log_buffer_size` | `virtual_users` | `warehouses` | Test Nº |
| --------- | ----------------- | ------------------ | ----------------- | --------------- | ------------ | ------- |
| Small     | 100               | 256M               | 8M                | 5               | 5            | 1       |
| Medium    | 200               | 512M               | 16M               | 10              | 10           | 2       |
| Large     | 500               | 1G                 | 32M               | 20              | 20           | 3       |
| Max CPU   | 500               | 2G                 | 64M               | 50              | 20           | 4       |
| I/O Test  | 200               | 256M               | 8M                | 20              | 5            | 5       |
| Memory    | 200               | 2G                 | 64M               | 10              | 10           | 6       |
| Latency   | 100               | 128M               | 8M                | 5               | 20           | 7       |
| Stress    | 1000              | 4G                 | 128M              | 100             | 50           | 8       |

# 1: 
DATES: 
			19/05/2025
				Virtual Users: 5
				Wheare houses: 5
				Iterations: 1
				NOPM: 52171
				TPM: 120634
	OS: UBUNTU
	Drive: SSD
	Max_connections = 100
	Buffer Pool size = 256MB
	Log Buffer size = 8MB

![[Pasted image 20250519121617.png]]


# 2:
DATES: 
			19/05/2025
				Virtual Users: 10
				Warehouses: 10
				Iterations: 1
				NOPM: 81529
				TPM: 187858
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 512MB
	Log Buffer size = 16MB
![[Pasted image 20250519122816.png]]

# 3:
DATES: 
			19/05/2025
				Virtual Users: 20
				Warehouses: 20
				Iterations: 1
				NOPM: 105417
				TPM: 241170
	OS: UBUNTU
	Drive: SSD
	Max_connections = 500
	Buffer Pool size = 1G
	Log Buffer size = 32MB

![[Pasted image 20250519124059.png]]


# 4:

DATES: 
			19/05/2025
				Virtual Users: 50
				Warehouses: 20
				Iterations: 1
				NOPM: 44438
				TPM: 103331
	OS: UBUNTU
	Drive: SSD
	Max_connections = 500
	Buffer Pool size = 2G
	Log Buffer size = 64MB
![[Pasted image 20250519155700.png]]


# 5:

DATES: 
			19/05/2025
				Virtual Users: 20
				Warehouses: 5
				Iterations: 1
				NOPM: 73619
				TPM: 170954
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 256MB
	Log Buffer size = 8MB

![[Pasted image 20250519161040.png]]

# 6:
DATES: 
			19/05/2025
				Virtual Users: 10
				Warehouses: 10
				Iterations: 1
				NOPM: 42691
				TPM: 98935
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 2G
	Log Buffer size = 64MB
	
![[Pasted image 20250519162423.png]]

# 7:

DATES: 
			19/05/2025
				Virtual Users: 5
				Warehouses: 20
				Iterations: 1
				NOPM: 41251
				TPM: 95860
	OS: UBUNTU
	Drive: SSD
	Max_connections = 100
	Buffer Pool size = 128MB
	Log Buffer size = 8MB

![[Pasted image 20250519163738.png]]
	
# 8:

DATES: 
			19/05/2025
				Virtual Users: 100
				Warehouses: 50
				Iterations: 1
				NOPM: 28298
				TPM: 65671
	OS: UBUNTU
	Drive: SSD
	Max_connections = 1000
	Buffer Pool size = 4G
	Log Buffer size = 128MB
![[Pasted image 20250519170037.png]]

# PostgreDB:
docker run -d --name postgres-bench \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=tpcc \
  -p 5432:5432 \
  postgres:16 \
  -c max_connections=151 \
  -c shared_buffers=1GB \
  -c wal_buffers=16MB
  
CREATE DATABASE tpcc;
CREATE USER tpcc WITH PASSWORD 'root';
GRANT ALL PRIVILEGES ON DATABASE tpcc TO tpcc;
ERROR:  database "tpcc" already exists
CREATE ROLE
GRANT

| Test Case | `max_connections` | `buffer_pool_size` | `log_buffer_size` | `virtual_users` | `warehouses` | Test Nº |
| --------- | ----------------- | ------------------ | ----------------- | --------------- | ------------ | ------- |
| Small     | 151               | 1G                 | 16M               | 2               | 10           | 1       |
| Medium    | 151               | 1G                 | 16M               | 5               | 10           | 2       |
| Large     | 200               | 1G                 | 16M               | 2               | 10           | 3       |
| Max CPU   | 200               | 1G                 | 16M               | 5               | 10           | 4       |

# 1:

	DATES: 
			18/05/2025
				Virtual Users: 2
				Wheare houses: 10
				Iterations: 1
				NOPM:
				TPM:
				
	OS: UBUNTU
	Drive: SSD
	Max_connections = 151
	Buffer Pool size = 1G
	Log Buffer size = 16MB

![[Pasted image 20250519175201.png]]

# 2:
	DATES: 
			18/05/2025
				Virtual Users: 5
				Wheare houses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 151
	Buffer Pool size = 1G
	Log Buffer size = 16MB

![[Pasted image 20250519180417.png]]

# 3:
DATES: 
			19/05/2025
				Virtual Users: 2
				Wheare houses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 1G
	Log Buffer size = 16MB

![[Pasted image 20250519181609.png]]

# 4:
	DATES: 
			19/05/2025
				Virtual Users: 5
				Wheare houses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 1G
	Log Buffer size = 16MB

![[Pasted image 20250519182559.png]]



# Now let's compare with others:

| Test Case | `max_connections` | `buffer_pool_size` | `log_buffer_size` | `virtual_users` | `warehouses` | Test Nº |
| --------- | ----------------- | ------------------ | ----------------- | --------------- | ------------ | ------- |
| Small     | 100               | 256M               | 8M                | 5               | 5            | 1       |
| Medium    | 200               | 512M               | 16M               | 10              | 10           | 2       |
| Large     | 500               | 1G                 | 32M               | 20              | 20           | 3       |
| Max CPU   | 500               | 2G                 | 64M               | 50              | 20           | 4       |
| I/O Test  | 200               | 256M               | 8M                | 20              | 5            | 5       |
| Memory    | 200               | 2G                 | 64M               | 10              | 10           | 6       |
| Latency   | 100               | 128M               | 8M                | 5               | 20           | 7       |
| Stress    | 1000              | 4G                 | 128M              | 100             | 50           | 8       |

# 1:
DATES: 
			19/05/2025
				Virtual Users: 5
				Wheare houses: 5
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 100
	Buffer Pool size = 256MB
	Log Buffer size = 8MB
![[Pasted image 20250519185609.png]]

# 2:
DATES: 
			19/05/2025
				Virtual Users: 10
				Warehouses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 512MB
	Log Buffer size = 16MB

![[Pasted image 20250519191005.png]]

# 3:
DATES: 
			19/05/2025
				Virtual Users: 20
				Warehouses: 20
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 500
	Buffer Pool size = 1G
	Log Buffer size = 32MB

![[Pasted image 20250519192224.png]]


# 4:

DATES: 
			19/05/2025
				Virtual Users: 50
				Warehouses: 20
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 500
	Buffer Pool size = 2G
	Log Buffer size = 64MB

![[Pasted image 20250519193413.png]]

# 5:

DATES: 
			19/05/2025
				Virtual Users: 20
				Warehouses: 5
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 256MB
	Log Buffer size = 8MB

![[Pasted image 20250519194606.png]]

# 6:
DATES: 
			19/05/2025
				Virtual Users: 10
				Warehouses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 2G
	Log Buffer size = 64MB

![[Pasted image 20250519195701.png]]

# 7:

DATES: 
			19/05/2025
				Virtual Users: 5
				Warehouses: 20
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 100
	Buffer Pool size = 128MB
	Log Buffer size = 8MB
![[Pasted image 20250520004636.png]]


# 8:

DATES: 
			19/05/2025
				Virtual Users: 100
				Warehouses: 50
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 1000
	Buffer Pool size = 4G
	Log Buffer size = 128MB
![[Pasted image 20250520005839.png]]


# Oracle

| Test Case | `max_connections` | `buffer_pool_size` | `log_buffer_size` | `virtual_users` | `warehouses` | Test Nº |
| --------- | ----------------- | ------------------ | ----------------- | --------------- | ------------ | ------- |
| Small     | 151               | 1G                 | 16M               | 2               | 10           | 1       |
| Medium    | 151               | 1G                 | 16M               | 5               | 10           | 2       |
| Large     | 200               | 1G                 | 16M               | 2               | 10           | 3       |
| Max CPU   | 200               | 1G                 | 16M               | 5               | 10           | 4       |

# 1:

	DATES: 
			18/05/2025
				Virtual Users: 2
				Wheare houses: 10
				Iterations: 1
				NOPM:
				TPM:
				
	OS: UBUNTU
	Drive: SSD
	Max_connections = 151
	Buffer Pool size = 1G
	Log Buffer size = 16MB



# 2:
	DATES: 
			18/05/2025
				Virtual Users: 5
				Wheare houses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 151
	Buffer Pool size = 1G
	Log Buffer size = 16MB



# 3:
DATES: 
			19/05/2025
				Virtual Users: 2
				Wheare houses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 1G
	Log Buffer size = 16MB



# 4:
	DATES: 
			19/05/2025
				Virtual Users: 5
				Wheare houses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 1G
	Log Buffer size = 16MB





# Now let's compare with others:

| Test Case | `max_connections` | `buffer_pool_size` | `log_buffer_size` | `virtual_users` | `warehouses` | Test Nº |
| --------- | ----------------- | ------------------ | ----------------- | --------------- | ------------ | ------- |
| Small     | 100               | 256M               | 8M                | 5               | 5            | 1       |
| Medium    | 200               | 512M               | 16M               | 10              | 10           | 2       |
| Large     | 500               | 1G                 | 32M               | 20              | 20           | 3       |
| Max CPU   | 500               | 2G                 | 64M               | 50              | 20           | 4       |
| I/O Test  | 200               | 256M               | 8M                | 20              | 5            | 5       |
| Memory    | 200               | 2G                 | 64M               | 10              | 10           | 6       |
| Latency   | 100               | 128M               | 8M                | 5               | 20           | 7       |
| Stress    | 1000              | 4G                 | 128M              | 100             | 50           | 8       |

# 1:
DATES: 
			19/05/2025
				Virtual Users: 5
				Wheare houses: 5
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 100
	Buffer Pool size = 256MB
	Log Buffer size = 8MB


# 2:
DATES: 
			19/05/2025
				Virtual Users: 10
				Warehouses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 512MB
	Log Buffer size = 16MB



# 3:
DATES: 
			19/05/2025
				Virtual Users: 20
				Warehouses: 20
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 500
	Buffer Pool size = 1G
	Log Buffer size = 32MB




# 4:

DATES: 
			19/05/2025
				Virtual Users: 50
				Warehouses: 20
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 500
	Buffer Pool size = 2G
	Log Buffer size = 64MB



# 5:

DATES: 
			19/05/2025
				Virtual Users: 20
				Warehouses: 5
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 256MB
	Log Buffer size = 8MB



# 6:
DATES: 
			19/05/2025
				Virtual Users: 10
				Warehouses: 10
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 200
	Buffer Pool size = 2G
	Log Buffer size = 64MB



# 7:

DATES: 
			19/05/2025
				Virtual Users: 5
				Warehouses: 20
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 100
	Buffer Pool size = 128MB
	Log Buffer size = 8MB



# 8:

DATES: 
			19/05/2025
				Virtual Users: 100
				Warehouses: 50
				Iterations: 1
				NOPM: 
				TPM: 
	OS: UBUNTU
	Drive: SSD
	Max_connections = 1000
	Buffer Pool size = 4G
	Log Buffer size = 128MB




# Find the best Config for each:

## Configure a DBMS to achieve better performance in the benchmark(s)

## Tune the database to achieve better performance in the benchmark(s)

## Analyze the performance when the number of users/size of the database increases

## Compare the different characteristics of the benchmarks and add extra characteristics to the benchmark (e.g. new transactions, new queries)

## Compare two or more database systems for a particular setting





Computer utilization - 
Transitions graph is it possible to generate from hammercli - 


In Build schema add 

|tcstart|Usage: tcstart|Starts the Transaction Counter.|
|tcstatus|Usage: tcstatus|Checks the status of the Transaction Counter.|
|tcstop|

AND 

| metset    | Usage: metset [agent_hostname\|agent_id] | Configure the CPU Metrics options. Equivalent to the Metrics Options window in the graphical interface. |
| --------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| metstart  | Usage: metstatus                         | Checks the status of the CPU Metrics.                                                                   |
| metstatus | Usage: metstart                          | Starts the CPU Metrics and agent if configured to the localhost.                                        |
| metstop   | Usage: metstop                           |                                                                                                         |

Dict config
