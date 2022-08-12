from django.shortcuts import render, redirect, HttpResponse
from django.http import FileResponse
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


def save_uploaded_file(file):
    with open('data.xlsx', 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def import_view(request):
    if request.method == "POST":
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            save_uploaded_file(request.FILES['file'])
            workbook = xlsxwriter.Workbook()
            return HttpResponse("Success")
    else:
        form = UploadDataForm()

    return render(request, "upload_file.html", {"upload_file_form": form})


def export_view(request):
    if request.user.restaurant is None:
        return HttpResponse("Вы должны быть авторизованы с аккаунта владельца ресторана")

    dishes = Dish.objects.filter(id=request.user.restaurant.id)

    workbook = xlsxwriter.Workbook("output.xlsx")
    dish_worksheet = workbook.add_worksheet()

    dish_worksheet.write(0, 0, "Название рус")
    dish_worksheet.write(0, 1, "Название англ")
    dish_worksheet.write(0, 2, "цена")
    dish_worksheet.write(0, 3, "Описание рус")
    dish_worksheet.write(0, 4, "Описание англ")
    dish_worksheet.write(0, 5, "Названия категорий на русском через ; (опционально)")
    dish_worksheet.write(0, 6, "Названия наборов на русском через ; (опционально)")

    for row_num, dish in enumerate(dishes):
        dish_worksheet.write(1 + row_num, 1, dish.name_ru)
        dish_worksheet.write(1 + row_num, 2, dish.name_en)
        dish_worksheet.write(1 + row_num, 3, dish.price)
        dish_worksheet.write(1 + row_num, 4, dish.description_ru)
        dish_worksheet.write(1 + row_num, 5, dish.description_en)
        categories = dish.dishescategory_set.all().only("name_ru")
        if categories is not None and len(categories) != 0:
            dish_worksheet.write(1 + row_num, 6, ";".join(categories))
    workbook.close()

    return FileResponse(open("output.xlsx", "rb"))
