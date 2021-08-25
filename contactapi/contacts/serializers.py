from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):

    class Meta:
        model=Contact

        fields = ['country_code','first_name','last_name','phone_number','contact_picture','is_favourite']