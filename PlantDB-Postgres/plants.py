from database import CursorFromConnectionFromPool




class Plant():
    def __init__(self, botanical_name, common_name, pot_size, owner, id):
        self.botanical_name = botanical_name
        self.common_name = common_name
        self.pot_size = pot_size
        self.owner = owner
        self.id = id

        # REPR method allows you to print an object, it must return a string
    def __repr__(self):
        return "<Plants:\n id: {}, botanical name: {}, common name: {}, {} gallons, owned by: {}>".format(self.botanical_name, self.common_name, self.pot_size, self.owner, self.id)#, self.common_name, self.pot_size, self.owner, self.id)

    #\n, {1}\n, {2}\n, {3}\n

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            # next we use the cursor. It is a tool that lets you retrieve data and read it row by row
            # Running some code... inserting 3 values into users table. Remember that ID is self-incrementing.
            cursor.execute('INSERT INTO plants (botanical_name, common_name, pot_size, owner) VALUES (%s, %s, %s, %s)',
                           (self.botanical_name, self.common_name, self.pot_size, self.owner))

    @classmethod  # This method doesnt access the currently bound object. 'cls' stand for currently bound class
    def load_from_db_by_bot_name(cls, botanical_name):
        with CursorFromConnectionFromPool() as cursor:
            # undeclared variable in a string, email var at the top
            cursor.execute('SELECT * FROM plants WHERE botanical_name=%s', (botanical_name,))
            # we have to define a tuple here because it thinks the parenthesis around email aren't needed.
            # we do that by adding a ',' comma in behind email like this (email,) this lets python know its a tuple
            # cursor.fetchone() should get us the first user with that email.
            plant_data = cursor.fetchone()
            # this is how you return the row from postgres. you can change the index order of returned items like this
            #return cls(plant_data, plant_data, plant_data, plant_data, plant_data)
            return cls(plant_data[0], plant_data[1], plant_data[2], plant_data[3], plant_data[4])


                    #(botanical_name = plant_data[1], common_name = plant_data[2], pot_size = plant_data[3], owner = plant_data[4], id = plant_data[0])
