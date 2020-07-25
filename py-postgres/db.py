import psycopg2


connection = None
try:
    connection = psycopg2.connect(user = "mehul",
                                  password = "meena*243036",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "mydata")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()

    print("You are connected to - ", record,"\n")
    print("\n---------------------------------------------------\n");
    print("--------- FETCHING RECORDS FROM TABLE company ------------\n")

    s = "SELECT * FROM company"
    cursor.execute(s)
    list_rcd = cursor.fetchall()

    for x in list_rcd:
      print("id ::->{0} name ::->{1} salary ::->{2}\n".format(x[0],x[1],x[4]))

except (Exception, psycopg2.Error) as error :
  print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        else:
          print("CONNECTION NOT AVAILABLE !!!")