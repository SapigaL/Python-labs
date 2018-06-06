from app import db


class God(db.Model):
    __tablename__ = "good"
    id = db.Column('id', db.Integer, primary_key=True)
    price = db.Column('price', db.Integer)
    weight = db.Column('weight', db.Integer)
    name = db.Column('name', db.String(20))
    veres = db.Column('veres', db.String(20))

    def __str__(self):
        return str("stuff id: " + str(self.id) + "\nprice: " + str(self.price) + "\nweight: " + str(self.weight) + "\nname: " + str(self.name) + "\nveres: " + str(self.veres))
