
class Connection:
    def __init__(self, host='localhosto'): # metodo normal recebe self
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod # metodo de classe recebe a classe (cls)
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


c1 = Connection()
c1.set_user('Stephcs')
c1.set_password('123')
print(c1.user)
print(c1.password)

c2 = Connection.create_with_auth('mmm', '456')
print(c2.user)
print(c2.password)