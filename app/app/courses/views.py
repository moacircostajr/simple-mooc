from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.


def index(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses.html', context)


def details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}
    return render(request, 'details.html', context)
