from .models import MyExcelFiles
from django.shortcuts import redirect, render
from .forms import MyExcelFilesForm
from django.conf import settings
import os
import csv
# Create your views here.
import simplejson as json


def UpdateForm(request):
    form = MyExcelFilesForm()

    if request.method == 'POST':
        form = MyExcelFilesForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            print(file.id)
            return redirect('data_views', id=file.id)
        

    return render(
        request,
        "excel/form.html",
        context={'form': form}
    )


def ShowData(request, id):
    file = MyExcelFiles.objects.get(id=id)
    print(file.excel)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file.excel))
    data = []
    with open(file_path , newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
         header = next(spamreader)
         print(header)
         print("-----")
         for row in spamreader:
             data.append({header[0] : row[0], header[1] :row[1], header[2]: row[2]})
             
    
    algo = json.dumps(data)
    print(algo)


    return render(
        request,
        "excel/data.html",
        context={'id':id, 'algo' : algo}
    )