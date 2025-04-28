from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import status

@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view(['GET','PUT'])
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serializer_item = MenuItemSerializer(item)
    return Response(serializer_item.data)





# def single_item(request, pk):
#     try:
#         item = MenuItem.objects.get(pk=pk)
#     except MenuItem.DoesNotExist:
#         return Response({"error": "MenuItem not found"}, status=404)

#     if request.method == 'GET':
#         serializer = MenuItemSerializer(item)
#         return Response(serializer.data)

#     # For PUT, you can add code to update the item here
#     elif request.method == 'PUT':
#         serializer = MenuItemSerializer(item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)