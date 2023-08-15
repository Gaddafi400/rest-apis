from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import IsOwner
from .serializers import ExpensesSerializer
from .models import Expense


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        :param serializer:
        :return: serializer
        It takes the serializer as an argument
        and saves the expense while associating it
        with the current user (self.request.user).
        This is done to set the owner of the expense to the currently
        logged-in user.
        """
        return serializer.save(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Expense.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
