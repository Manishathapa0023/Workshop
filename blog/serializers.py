from rest_framework import serializers
from blog.models import BloodDoner
class BloodDonerSerializers(serializers.ModelSerializer):
    class Meta:
        model = BloodDoner
        fields= '__all__'