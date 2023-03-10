from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer
from products.models import Product


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW

    """
    Serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance= Serializer.save()
        print(instance)
        return Response(Serializer.data)

   