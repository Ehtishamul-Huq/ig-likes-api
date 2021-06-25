from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from userproject.serializers import LikeSerializer
from userproject.models import Like
from rest_framework.generics import ListAPIView
from .permissions import CustomPermission

class BaseView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):    
        _data = {**request.data, **{"user":request.user.pk}}
        serializer = self.serializer_class(data=_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response({'data': serializer.data,
                             'message': 'Likes has been added'}, status=status.HTTP_200_OK)

    def get(self,request):
        instance = self.model_class.objects.filter(user=request.user)
        serializer = self.serializer_class(instance, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)


class UpdateView(APIView):
    permission_classes = (IsAuthenticated, CustomPermission)

    def get(self, request, pk):
        obj = self.model_class.objects.get(id=pk)
        self.check_object_permissions(self.request, obj)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        obj = self.model_class.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        serializer = self.serializer_class(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data": serializer.data, "message": "Data has been updated"}, status=status.HTTP_200_OK)

    def delete(self,request,pk):
        obj = self.model_class.objects.get(id=pk)
        self.check_object_permissions(self.request,obj)
        obj.delete()
        return Response({'Message': 'Deleted'}, status=status.HTTP_200_OK)


class LikeView(BaseView):
    model_class = Like
    serializer_class = LikeSerializer
    search_fields = ['likes']

class LikeUpdateView(UpdateView):
    model_class = Like
    serializer_class = LikeSerializer