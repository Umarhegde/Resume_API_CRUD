from django.urls import path
from .views import ResumeAPI,ResumeDetails


urlpatterns = [
    path('resume/',ResumeAPI.as_view()),
    path('detail/<int:id>/',ResumeDetails.as_view())
]
