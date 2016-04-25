import pymysql
from prettytable import PrettyTable
conn = pymysql.connect(host='127.0.0.1', user = 'root', passwd = 'TeOtAuY16!', db='mysql')
cur = conn.cursor()
cur.execute("USE voter_turnout_data")

print("International Voter Turnout Database")
cont = ''
while (cont != "N" and cont != "n"):
    count = 0
    invalid = False
    cont = ''
    answer = input("\nSelect a query from the menu:\n\n" +
        "1. What is the voter turnout for countries where there is compulsory voting?\n" +
        "2. What is the voter turnout for a country with a high life expectancy?\n" +
        "3. What is the voter turnout for a country with a low life expectancy?\n" +
        "4. What is the voter turnout for the countries with the top 100 GDPs?\n" +
        "5. What is the voter turnout for the countries with the bottom 100 GDPs?\n" +
        "6. Which countries have a higher voter turnout rate than the US in recent years?\n")
    print("Your answer is " + answer)
    if (answer == "1"):
        print("Voter turnout for countries where there is compulsory voting:\n")
        ##1
        ##SELECT country, year, turnout_rate
        ##FROM voter_turnout
        ##WHERE compulsory = 'Yes';
        cur.execute("SELECT country, year, turnout_rate FROM voter_turnout WHERE compulsory = 'Yes'")
        print("SELECT country, year, turnout_rate\n" +
              "FROM voter_turnout\n" +
              "WHERE compulsory = 'Yes';")
        x = cur.fetchone()
        if x != None:
            t = PrettyTable(['country', 'year', 'turnout_rate'])
            while x != None:
                t.add_row([x[0], x[1], x[2]])
                count += 1
                x = cur.fetchone()

    elif(answer == "2"):
        print("Voter turnout for a country with a high life expectancy:\n")
        ##2
        ##SELECT country, year, turnout_rate, life_expectancy
        ##FROM voter_turnout v JOIN life_expectancy l
        ##ON v.country = l.country AND v.year = l.year
        ##WHERE l.life_expectancy > 75
        print("SELECT v.country, v.year, v.turnout_rate, l.life_expectancy\n" +
              "FROM voter_turnout v INNER JOIN life_expectancy l\n" +
              "ON v.country = l.country AND v.year = l.year\n" +
              "WHERE l.life_expectancy > 75;")
        cur.execute("SELECT v.country, v.year, v.turnout_rate, l.life_expectancy FROM voter_turnout v INNER JOIN life_expectancy l ON v.country = l.country AND v.year = l.year WHERE l.life_expectancy > 75")
        x = cur.fetchone()
        if x != None:
            t = PrettyTable(['country', 'year', 'turnout_rate', 'life_expectancy'])
            while x != None:
                t.add_row([x[0], x[1], x[2], x[3]])
                count += 1
                x = cur.fetchone()

    elif(answer == "3"):
        print("Voter turnout for a country with a low life expectancy:\n")
        ##3
        ##SELECT v.country, v.year, v.turnout_rate, l.life_expectancy
        ##FROM voter_turnout v INNER JOIN life_expectancy l
        ##ON v.country = l.country AND v.year = l.year
        ##WHERE l.life_expectancy < 50
        cur.execute("SELECT v.country, v.year, v.turnout_rate, l.life_expectancy FROM voter_turnout v INNER JOIN life_expectancy l ON v.country = l.country AND v.year = l.year WHERE l.life_expectancy < 50")
        print("SELECT v.country, v.year, v.turnout_rate, l.life_expectancy\n" +
              "FROM voter_turnout v INNER JOIN life_expectancy l\n" +
              "ON v.country = l.country AND v.year = l.year\n" +
              "WHERE l.life_expectancy < 50;")
        x = cur.fetchone()
        if x != None:
            print("  country   year   turnout_rate   life_expectancy")
            t = PrettyTable(['country', 'year', 'turnout_rate', 'life_expectancy'])
            while x != None:
                t.add_row([x[0], x[1], x[2], x[3]])
                count += 1
                x = cur.fetchone()

    elif(answer == "4"):
        print("Voter turnout, GDP, and GDP Per Capita for the countries with the top 100 GDPs:\n")
        ##4
        ##SELECT v.country, v.year, v.turnout_rate, g.gdp, g.gpd_per_cap
        ##FROM voter_turnout v INNER JOIN gdp g
        ##ON v.country = g.country AND v.year = g.year
        ##ORDER BY gdp DESC LIMIT 100
        cur.execute("SELECT v.country, v.year, v.turnout_rate, g.gdp, g.gdp_per_cap FROM voter_turnout v INNER JOIN gdp g ON v.country = g.country AND v.year = g.year ORDER BY gdp DESC LIMIT 100")
        print("SELECT v.country, v.year, v.turnout_rate, g.gdp, g.gdp_per_cap\n" +
              "FROM voter_turnout v INNER JOIN gdp g\n" +
              "ON v.country = g.country AND v.year = g.year\n" +
              "ORDER BY gdp DESC LIMIT 100;")
        x = cur.fetchone()
        if x != None:
            t = PrettyTable(['country', 'year', 'turnout_rate', 'gdp', 'gdp_per_cap'])
            while x != None:
                t.add_row([x[0], x[1], x[2], x[3], x[4]])
                count += 1
                x = cur.fetchone()

    elif(answer == "5"):
        print("Voter turnout, GDP, and GDP Per Capita for the countries with the bottom 100 GDPs:\n")
        ##5
        ##SELECT v.country, v.year, v.voter_turnout, g.gdp, g.gdp_per_cap
        ##FROM voter_turnout v INNER JOIN gdp g
        ##ON v.country = g.country AND v.year = g.year
        ##ORDER BY gdp LIMIT 100
        cur.execute("SELECT v.country, v.year, v.turnout_rate, g.gdp, g.gdp_per_cap FROM voter_turnout v INNER JOIN gdp g ON v.country = g.country AND v.year = g.year ORDER BY gdp LIMIT 100")
        print("SELECT v.country, v.year, v.voter_turnout, g.gdp, g.gdp_per_cap\n" +
              "FROM voter_turnout v INNER JOIN gdp g\n" +
              "ON v.country = g.country AND v.year = g.year\n" +
              "ORDER BY gdp LIMIT 100;")
        x = cur.fetchone()
        if x != None:
            t = PrettyTable(['country', 'year', 'turnout_rate', 'gdp', 'gdp_per_cap'])
            while x != None:
                t.add_row([x[0], x[1], x[2], x[3], x[4]])
                count += 1
                x = cur.fetchone()

    elif(answer == "6"):
        print("Countries that have a higher voter turnout rate than the US in recent years:\n")
    ##    6
    ##    SELECT v1.country, v1.year, v1.turnout_rate
    ##        FROM voter_turnout v1 INNER JOIN
    ##            (SELECT v3.country, v3.year, v3.turnout_rate
    ##             FROM voter_turnout v3
    ##             WHERE v3.country = 'United States'
    ##             ORDER BY year DESC LIMIT 10) v2
    ##        ON v1.turnout_rate > v2.turnout_rate
        cur.execute("SELECT v1.country, v1.year, v1.turnout_rate FROM voter_turnout v1 INNER JOIN (SELECT v3.country, v3.year, v3.turnout_rate FROM voter_turnout v3 WHERE v3.country = 'United States' ORDER BY year DESC LIMIT 10) v2 ON v1.turnout_rate > v2.turnout_rate")
        print("SELECT v1.country, v1.year, v1.turnout_rate\n" +
              "FROM voter_turnout v1 INNER JOIN\n" +
              "\t(SELECT v3.country, v3.year, v3.turnout_rate\n" +
              "\tWHERE v3.country = 'United States'\n" +
              "\tORDER BY year DESC LIMIT 10) v2\n" +
              "ON v1.turnout_rate > v2.turnout_rate;")
        x = cur.fetchone()
        if x != None:
            t = PrettyTable(['country', 'year', 'turnout_rate'])
            while x != None:
                t.add_row([x[0], x[1], x[2]])
                count += 1
                x = cur.fetchone()
            
    else:
        print("Sorry! Your response is not valid!")
        invalid = True
        
    if invalid:
        print("Please try again.\n")
        
    else:
        print(t)
        print(str(count) + " rows in set\n")
        cont = input("Would you like to SELECT another query? (Y/N) ")
        while (cont != "Y" and cont != "y" and cont != "N" and cont != "n"):
            print("Sorry! That response is not valid. Please try again.")
            cont = input("Would you like to SELECT another query? (Y/N) ")
            


cur.close()
conn.close()




