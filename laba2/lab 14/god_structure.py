from app import ma


class GodStructure(ma.Schema):
    class Meta:
        fields = ('id', 'price', 'fish', 'name', 'veres')
