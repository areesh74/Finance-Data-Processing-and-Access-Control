from rest_framework.views import APIView
from rest_framework.response import Response
from records.models import Record
from django.db.models import Sum

class DashboardView(APIView):
    def get(self, request):
        total_income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        net_balance = total_income - total_expense
        category_data = Record.objects.values('category').annotate(total=Sum('amount'))

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance
        })