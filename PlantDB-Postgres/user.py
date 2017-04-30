from database import CursorFromConnectionFromPool

class User():
    def __init__(self, email, name, id):
        self.email = email
        self.name = name
        self.id = id

        # REPR method allows you to print an object, it must return a string
    def __repr__(self):
        return "<User: {}>".format(self.email)

    def save_to_db(self):
        with CursorFromConnectionFromPool() as cursor:
            # next we use the cursor. It is a tool that lets you retrieve data and read it row by row
            # Running some code... inserting 3 values into users table. Remember that ID is self-incrementing.
            cursor.execute('INSERT INTO users (email, name) VALUES (%s, %s)',
                           (self.email, self.name))

    @classmethod  # This method doesnt access the currently bound object. 'cls' stand for currently bound class
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:
            # undeclared variable in a string, email var at the top
            cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
            # we have to define a tuple here because it thinks the parenthesis around email aren't needed.
            # we do that by adding a ',' comma in behind email like this (email,) this lets python know its a tuple
            # cursor.fetchone() should get us the first user with that email.
            user_data = cursor.fetchone()
            # this is how you return the row from postgres. you can change the index order of returned items like this
            return cls(email=user_data[1], name=user_data[2], id=user_data[0])
