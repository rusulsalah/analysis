from django.shortcuts import render
from .forms import CsvForm
import csv
from products.models import Product,Purchase
from .models import Csv
from django.contrib.auth.models import User

# Create your views here.
def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj=Csv.objects.get(activated=False)
            with open(obj.file_name.path,'r') as f:
                reader=csv.reader(f)
                for i,row in enumerate(reader):#to skip first row of file which conatin title
                    if i==0:
                        pass
                    else:
                        row="".join(row) # convert to string
                        row=row.replace(";"," ")# between item and other only space
                        row=row.split() # 'item','item' in list
                        product,_ =Product.objects.get_or_create(name=row[1])#to take name of product from table
                        user =User.objects.get(username=row[3])

                        Purchase.objects.create(
                            product =product,
                            quantity= int(row[2]),
                            salesman=user,
                            price=int(row[4]),
                        )
                        print(row)
                        #print(type(row))
                obj.activated=True
                obj.save()
            sucess_message='ok uploaded'

        except:error_message='try again'



    context={
        'form':form,
        'success_message':success_message,
        'error_message':error_message,

    }
    return render(request,'upload.html',context)