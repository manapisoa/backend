from django.shortcuts import render
from rest_framework import generics
from .models import Transaction,Notification
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
class RetieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = 'id'

@api_view(['POST'])
def create_notif(request):
    notif = Notification.objects.create(title = request.data['title'],
                                        message = request.data['message']
                                        )
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)
    (
        "notif_group",
        {
            "type":"send_notif",
            "data":{
                "id":notif.id,
                "title":notif.title,
                "message":"message envoyer depuis le backend"
            }
        }
    )
    
    return Response({"status":"sent"})
@api_view(['GET'])
def list_notif(request):
    notifs = Notification.objects.order_by('-created_at')[:20].values()
    return Response(list(notifs))


    
