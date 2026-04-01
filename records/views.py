from rest_framework.viewsets import ModelViewSet
from .models import Record
from .serializers import RecordSerializer
from .permissions import RoleBasedPermission

class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [RoleBasedPermission]


    def get_queryset(self):
        queryset = Record.objects.all()

        
        category = self.request.query_params.get('category')
        type_ = self.request.query_params.get('type')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if category:
            queryset = queryset.filter(category__icontains=category)

        if type_:
            queryset = queryset.filter(type=type_)

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset