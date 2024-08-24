from celery import shared_task
from .serializers import TrackCreateSerializer
@shared_task()
def bulk_upload_json_data(json_data):
    serializer = TrackCreateSerializer(data=json_data, many=True)
    if serializer.is_valid():
        serializer.save()
        return True
    else:
        return serializer.errors
