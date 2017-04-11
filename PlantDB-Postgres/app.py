from database import Database
from user import User
from plants import Plant
import psycopg2

# DB connection
#database_con = 'postgres'
#user_con = 'postgres'
#password_con = 'postgres'
#host_con = '192.168.0.177'
#conn_info = "{}{}{}{}"
#connect_info = str(database='postgres', user='postgres', password='postgres', host='192.168.0.177') 
# default db info:   database='plant-db', user='postgres', password='Ac3TeX411', host='localhost'
conn_info = Database.initialise(database='postgres', user='postgres', password='postgres', host='192.168.0.177')
conn_info

connection2db = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='192.168.0.177')

def automateDB():
    userChoice = input("Press 'A':New plant, 'U':New user, 'L':Look up plant, 'P':Display all plants,\n 'N':Display all users, 'X':Exit,\n'T':Uploads tables to DB(ONLY USE IF TABLES DONT EXIST)...: ")
    if userChoice.upper() == 'A':
        makePlant()
    if userChoice.upper() == 'U':
        makeUser()
    if userChoice.upper() == 'L':
        printPlants()
    if userChoice.upper() == 'P':
        unloadPlants()
    if userChoice.upper() == 'N':
        unloadUsers()
    if userChoice.upper() == 'T':
        uploadTables()
    elif userChoice.upper() == 'X':
        exit()
    else:
        automateDB()

def makeUser():
    # Instantiated creation of a 'User' object by program user
    user_name_input = input("Enter your name: ")
    user_email_input = input("Enter your email: ")
    # Format for adding a user to the Postgres DB
    # example format: ('seanw@protonmail.ch', 'Sean Wilkie', None)
    user = User(user_email_input, user_name_input, None)

    # This code will save to the DB
    user.save_to_db()
    print(user)
    automateDB()

# add a plant here:
def makePlant():
    user_plantName = input('Enter botanical name of plant: ')
    user_plantCommon = input('Enter common name of plant: ')
    user_plantSize = input('Size of pot in Gallons(INTEGER): ')
    user_plantOwner = input('Who owns this plant?: ')

    #def __init__(self, botanical_name, common_name, pot_size, owner, id):
    plant2DB = Plant(user_plantName, user_plantCommon, user_plantSize, user_plantOwner, None)
    # save to db: cursor.execute('INSERT INTO plants (botanical_name, common_name, pot_size, owner) VALUES (%s, %s, %s, %s)',
    #                           (self.botanical_name, self.common_name, self.pot_size, self.owner))
    plant2DB.save_to_db()
    print("Added plant to database...")
    automateDB()

def printPlants():
    plantLookup = input("Name of plant to look up?: ")
    plant_from_db = Plant.load_from_db_by_bot_name(plantLookup)
    print(plant_from_db)
    automateDB()

def unloadPlants():
    connection = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='192.168.0.177')
    cursor = connection.cursor()
    cursor.execute("select * from plants")
    for row in cursor:
        print(row)
    connection.close
    automateDB()

def unloadUsers():
    connection = psycopg2.connect(database='postgres', user='postgres', password='postgres', host='192.168.0.177')
    cursor = connection.cursor()
    cursor.execute("select * from users")
    for row in cursor:
        print(row)
    connection.close
    automateDB()

def uploadTables():
    connection2db
    cursor = connection2db.cursor()
    cursor.execute('CREATE TABLE public.plants    (id serial NOT NULL, botanical_name character varying(255) COLLATE pg_catalog. "default" NOT NULL, common_name character varying(255) COLLATE pg_catalog."default" NOT NULL, pot_size integer,owner character varying(255) COLLATE pg_catalog."default", CONSTRAINT plants_pkey PRIMARY KEY (id) ) WITH (OIDS = FALSE) TABLESPACE pg_default; ALTER TABLE public.plants  OWNER to postgres;')
    cursor.execute('CREATE TABLE public.users(    id serial NOT NULL , name character varying(255) COLLATE pg_catalog."default" NOT NULL, email character varying(255) COLLATE pg_catalog."default" NOT NULL, CONSTRAINT users_pkey PRIMARY KEY (id))WITH (OIDS = FALSE) TABLESPACE pg_default; ALTER TABLE public.users OWNER to postgres;')
    connection2db.commit()
    connection2db.close
    automateDB()
#try:
automateDB()
#except Exception:
#    print('got an error, restarting...')
#    pass
# user_from_db = User.load_from_db_by_email('johnsmith@hotmail.com')
# print(user_from_db)

#print(plant2DB)

