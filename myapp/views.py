
from django.shortcuts import get_object_or_404, redirect, render
from .models import Inventory
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .forms import AddInventoryForm, UpdateInventoryForm
from django.contrib import messages
from django_pandas.io import read_frame
import plotly
import plotly.express as px 
import json



@login_required
def Inventory_list(request):
    Inventories = Inventory.objects.all()
    context = {
        "Inventories": Inventories
    }
    return render(request, "dashboard.html", context=context)

class per_product_view(DetailView):
    model = Inventory
    template_name='per_product.html'

@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)  # Pass request.POST data to the form
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = (
                float(add_form.cleaned_data['cost_per_item']) *
                float(add_form.cleaned_data['quantity_sold'])
            )
            new_inventory.save()
            messages.success(request,"Successfully added Product")
            return redirect("templates")  # Replace with the appropriate URL to redirect to
    else:
        add_form = AddInventoryForm()  # Create a new form instance for GET requests

    return render(request, "inventory_add.html", {"form": add_form})


# def delete_inventory(request,pk):
#     inventory=get_object_or_404(Inventory,pk=pk)
#     inventory.delete()
#     return redirect("templates")
        

class delete_inventory(DetailView):
    model = Inventory
    template_name='per_product.html'


@login_required
def delete_inventory(request,pk):
    inventory = get_object_or_404(Inventory, id=pk)
    print(" delete successfull ")
    inventory.delete()
    return redirect("myapp:Inventory_list")

@login_required
def update_inventory(request,pk):
    inventory = get_object_or_404(Inventory, id=pk)

    if request.method=="POST":
        UpdateForm=UpdateInventoryForm(request.POST,instance=inventory)
        if UpdateForm.is_valid():
            # inventory.name = UpdateForm.clear_data.get['name']
            # inventory.quantity_in_stock=UpdateForm.data['quantity_in_stock']
            # inventory.quantity_sold=UpdateForm.data['quantity_sold']
            # inventory.cost_per_item=UpdateForm.data['cost_per_item']
            # inventory.sales=float('inventory.cost_per_item')   * float(inventory.quantity_sold)
            item=UpdateForm.save(commit=False)
            item.save()
            
            return redirect("myapp:tables")
        print(" update ")
    else :
        UpdateForm = UpdateInventoryForm(instance=inventory)
        context={"form": UpdateForm}
        return render (request,"inventory_update.html",context=context)

# @login_required
# def dashboard(request):
#     inventories=Inventory.objects.all()

#     df = read_frame(inventories)


#     sales_graph = df.groupby(by="last_sales_date",as_index=False, sort=False)['sales'].sum()
#     sales_graph = px.line(sales_graph,x=sales_graph.last_sales_date,y=sales_graph.sales, title="Sales Trend")
#     sales_graph= json.dumps(sales_graph,cls=plotly.util.PlotlyJSONEncoder)


#     context={
#         "sales_graph":sales_graph
#     }


#     return render(request,"inventories/dashboard.html",context=context)

@login_required
def chart(request):
    Inventories = Inventory.objects.all()
    context = {
        "Inventories": Inventories
    }
    return render(request, "chart.html", context=context)

@login_required
def tables(request):
    Inventories = Inventory.objects.all()
    context = {
        "Inventories": Inventories
    }
    return render(request, "table.html", context=context)
    
    