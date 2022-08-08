from django.shortcuts import  render, redirect, HttpResponse
from .forms import NewUserForm, UploadDataForm
from .models import Restaurant, Dish
from django.contrib.auth import login
from django.contrib import messages
import io
import xlsxwriter


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return HttpResponse("Registered")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def handle_uploaded_file(file):
    with open('data.xlsx', 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def import_view(request):
    if request.method == "POST":
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("Success")
    else:
        form = UploadDataForm()

    return render(request, "upload_file.html", {"upload_file_form": form})


def export_view(request):
    if request.user.restaurant is None:
        return HttpResponse("Вы должны быть авторизованы с аккаунта владельца ресторана")

    dishes = Dish.objects.filter(id=request.user.restaurant.id)

    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    return HttpResponse("test")
