from django.urls import path
from .views import ProblemListCreateView, ProblemDetailView

urlpatterns = [
    path('', ProblemListCreateView.as_view(), name='problem-list-create'),
    path('<int:pk>/', ProblemDetailView.as_view(), name='problem-detail'),
]
