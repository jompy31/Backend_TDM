from rest_framework import generics
from .models import Product, Characteristic
from .serializers import ProductSerializer, CharacteristicSerializer
from rest_framework.permissions import AllowAny

class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        file = self.request.data.get('file')
        file1 = self.request.data.get('file1')
        name = self.request.data.get('name')
        description = self.request.data.get('description')
        characteristics_ids = self.request.data.getlist('characteristics')
        # characteristics = Characteristic.objects.filter(id__in=characteristic_ids)
        characteristics_data = self.request.data.get('characteristics', [])

        
        if file and name:
            product = serializer.save(user=self.request.user, file=file, file1=file1, name=name, description=description)
            for char_id in characteristics_ids:
                char = Characteristic.objects.get(pk=char_id)
                product.characteristics.add(char)
        else:
            serializer.save(user=self.request.user)

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CharacteristicListCreate(generics.ListCreateAPIView):
    serializer_class = CharacteristicSerializer
    queryset = Characteristic.objects.all()
    
class CharacteristicRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer

class CharacteristicDestroy(generics.DestroyAPIView):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


    