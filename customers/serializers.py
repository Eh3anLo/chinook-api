from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id','first_name','last_name','phone','email']
        # fields = '__all__'
        extra_kwargs = {
            'customer_id' : {'validators' : []},
            'first_name' : {'required' : False},
            'last_name' : {'required' : False},
        }

        