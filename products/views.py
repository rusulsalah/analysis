from django.shortcuts import render
from .models import Product,Purchase
import pandas as pd
from .utils import get_simple_plot,get_image,get_salesman
from .forms import  purchaseForm
import matplotlib.pyplot as plt
import seaborn as sns
from  django.contrib.auth.decorators import login_required
# Create your views here.
def fund(request):

    return render(request,'home.html',{})
@login_required
def sales_dist_view(request):
    df=pd.DataFrame(Purchase.objects.all().values())
    #print(df)
    df['salesman_id']=df['salesman_id'].apply(get_salesman)
    df.rename({'salesman_id':'salesman'},axis=1,inplace=True)
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    #print(df)
    plt.switch_backend('Agg')
    sns.barplot(x='date',y='total_price',hue='salesman',data=df)
    plt.tight_layout()
    graph=get_image()


    context={'graph':graph

    }


    return render(request,'sales.html',context)
@login_required
def home(request):
    graph=None
    df=None
    error_message=None
    price=None
    qs1=Product.objects.all().values()
    qs2=Purchase.objects.all().values()
    try:
        product_df=pd.DataFrame(Product.objects.all().values())
        purchase_df= pd.DataFrame(Purchase.objects.all().values())
        product_df['product_id']=product_df['id']
        if purchase_df.shape[0]>0: # if we have a purchase detail of product
            df=pd.merge(product_df,purchase_df,on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis=1)
            price=df['price']
            if request.method=="POST":
                chart_type=request.POST.get('sales')
                date_from=request.POST['date_from']
                date_to = request.POST['date_to']
                df['date']=df['date'].apply(lambda x:x.strftime('%Y-%m-%d')) # all time for certain purchase
                df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')  # total price for  certain purchase(product) in certain period
                if chart_type !="": #if we choose chart
                    if date_from !='' and date_to !='': #if we choose date
                        df=df[(df['date']>date_from)&(df['date']<date_to)]
                        df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')  # total price for  certain purchase(product) in certain period
                         #function to get graph
                    graph=get_simple_plot(chart_type,x=df2['date'],y=df2['total_price'],data=df)

                else:
                    error_message='please select chart type'


                     #context={'products':product_df.to_html,
                              #'purchase':purchase_df.to_html,
                           # 'df':df.to_html           #'error_message':error_message}
        else:
            error_message= 'no recording in datebase'
    except:
        purchase_df=None
        product_df=None
        error_message = 'no recording in datebase'



    context = {'error_message':error_message,
               'graph':graph,
               'price':price,
    }

    return render(request,'main.html',context)
@login_required
def add_purchase(request):
    add_message=None
    form=purchaseForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.salesman=request.user
        obj.save()
        form = purchaseForm()
        add_message="purchase has been added"



    context = {'form': form,
               'add_message': add_message,

               }

    return render(request, 'add.html', context)


