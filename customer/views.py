from django.shortcuts import render
from django.shortcuts import render
from .models import Customer
import pandas as pd
from products.utils import get_image
import seaborn as sns
import matplotlib.pyplot as plt


# Create your views here.
def customer_corr_view(request):
    df = pd.DataFrame(Customer.objects.all().values())
    corr=round(df['budget'].corr(df['employment']),)
    plt.switch_backend('Agg')
    sns.jointplot(x='budget',y='employment',kind='reg',data=df).set_axis_labels('company budget','no of employment')
    graph=get_image()

    context={
        'graph':graph,
         'corr':corr,

    }
    return render(request,'corr.html',context)