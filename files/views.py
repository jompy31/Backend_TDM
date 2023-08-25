from rest_framework import generics
from files.models import File, NewsPost, Distributor
from files.serializers import FileSerializer, NewsPostSerializer, DistributorSerializer

class FileListCreate(generics.ListCreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def perform_create(self, serializer):
        file = self.request.data.get('file')
        name = self.request.data.get('name')
        if file and name:
            serializer.save(user=self.request.user, file=file, name=name)
        else:
            serializer.save(user=self.request.user)


class FileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDestroy(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class NewsPostListCreate(generics.ListCreateAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

class NewsPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

class DistributorListCreate(generics.ListCreateAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

class DistributorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer