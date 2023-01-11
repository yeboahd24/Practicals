from peewee import *


db = SqliteDatabase('peewee.db')

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)


class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    subject = CharField()
    body = TextField()
    # timestamp = DateTimeField()

    class Meta:
        order_by = ('-user',)



def message_create():
    user = User.get(User.username == 'james')
    message = Message.create(
        user=user,
        subject='Hello',
        body='Hello world'
    )
    message.save()


def create_and_connect():
    db.connect()
    db.create_tables([User, Message], safe=True)


def sample_data():
    try:
        user = User(
            username='james',
            email = 'dominic@gmail.com'
        )
        user.save()
    except IntegrityError:
        pass



def retrieve_message():
    message = Message.get(Message.id == 1)
    print(message.user.username)
    print(message.subject)
    print(message.body)


def main():
    create_and_connect()
    sample_data()
    message_create()
    retrieve_message()


if __name__ == '__main__':
    main()