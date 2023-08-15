import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from expenses.models import Expense


# Create your models here.


class ExpenseSummaryStats(APIView):

    def get(self, request):
        today_date = datetime.date.today()
        a_year_ago = today_date - datetime.timedelta(days=30 * 12)
        expenses = Expense.objects.filter(owner=request.user, date__gte=a_year_ago, date__lte=today_date)

        final = {}
        categories = list(map(self.get_category, expenses))
        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(expense, category)

        return Response({'category_data': final}, status=status.HTTP_200_OK)

    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0
        for expense in expenses:
            amount += expense.amount
        return {'amount': str(amount)}

    def get_category(self, expense):
        return expense.category
