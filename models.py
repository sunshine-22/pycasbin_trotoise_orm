from tortoise.models import Model
from tortoise import fields




class Contact(Model):
    name = fields.CharField(max_length=255)
    phone_number = fields.CharField(max_length=20)
    def __str__(self):
        return self.name




class usertable(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)

class Country(Model):
    id = fields.UUIDField(pk=True)
    country_name = fields.CharField(max_length=100)
    created_by = fields.ForeignKeyField(
        model_name="models.usertable",null=True,on_delete=fields.SET_NULL
    )
class State(Model):
    id = fields.UUIDField(pk=True)
    state_name = fields.CharField(max_length=100)
    country = fields.ForeignKeyField(
        model_name="models.Country",null=True,on_delete=fields.SET_NULL
    )
    created_by = fields.ForeignKeyField(
        model_name="models.usertable",null=True,on_delete=fields.SET_NULL
    )