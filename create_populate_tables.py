## import pymysql and csv packages
import pymysql
import csv

## connect to SQL
conn = pymysql.connect(host='127.0.0.1', user = 'root', passwd = 'TeOtAuY16!', db='mysql')
cur = conn.cursor()

## select the schema voter_turnout_data 
cur.execute("USE voter_turnout_data")

#### create the tables
## voter_turnout
cur.execute("CREATE TABLE voter_turnout (country VARCHAR(50) NOT NULL, year SMALLINT(4) NOT NULL, election_type ENUM('Parliamentary', 'Presidential') NOT NULL, turnout_rate DECIMAL(5,2) NOT NULL, reg_pop_pct DECIMAL(5,2), total_pop INT(20) NOT NULL, compulsory ENUM('Yes', 'No') NOT NULL, PRIMARY KEY (country, year, election_type))")
## gdp
cur.execute("CREATE TABLE gdp (country VARCHAR(50) NOT NULL, year SMALLINT(4) NOT NULL, gdp BIGINT(20) NOT NULL, gdp_per_cap BIGINT(20) NOT NULL, PRIMARY KEY (country, year))")
## life_expectancy
cur.execute("CREATE TABLE life_expectancy (country VARCHAR(50) NOT NULL, year SMALLINT(4) NOT NULL, life_expectancy INT(3) NOT NULL, PRIMARY KEY (country, year))")

## open the VTData csv file and read it
with open('VTData.csv', 'r') as csvfile:
    vt_data = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    for row  in vt_data:
        ## check to see if the row has any empty cells; if so, then skip that row
        if (row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '' and row[5] != '' and row[6] != ''):
            ## print each row (this helps keep track of progress)
            print(row)
            ## insert the row into the table
            cur.execute("INSERT INTO voter_turnout (country, year, election_type, turnout_rate, reg_pop_pct, total_pop, compulsory) VALUES ('" + row[0] + "', " + row[1] + ", '" + row[2] + "', " + row[3] + ", " + row[4] + ", " + row[5] + ", '" + row[6] + "')")
            cur.connection.commit()
## close the file
vt_data.close()

## open the GDP data csv file and read it
with open('GDP data.csv', 'r') as csvfile:
    gdp_data = csv.reader(csvfile)
    for row  in gdp_data:
        ## check to see if the row has any empty cells; if so, then skip that row
        if (row[0] != '' and row[1] != '' and row[2] != '' and row[3] != ''):
            ## print each row (this helps keep track of progress)
            print(row)
            ## insert the row into the table 
            cur.execute("INSERT INTO gdp (country, year, gdp, gdp_per_cap) VALUES ('" + row[0] + "', " + row[1] + ", " + row[2] + ", " + row[3] + ")")
            cur.connection.commit()
## close the file
gdp_data.close()

## open the Life expectancy data csv file and read it
with open('Life expectancy data.csv', 'r') as csvfile:
    life_expec_data = csv.reader(csvfile, delimiter = ',', quotechar = '|')
    for row  in life_expec_data:
        ## check to see if the row has any empty cells; if so, then skip that row
        if (row[1] != '' and row[2] != ''):
            ## print each row (this helps keep track of progress)
            print(row)
            cur.execute("INSERT INTO life_expectancy (country, year, life_expectancy) VALUES (\"" + row[0] + "\", " + row[1] + ", " + row[2] + ")")
            cur.connection.commit()
## close the file
life_expec_data.close()

## end the connection to SQL
cur.close()
conn.close()
