from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order, OrderItem
from .forms import OrderForm
from users.models import BuyerProfile
from django.contrib import messages

# Create your views here.

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.user.is_authenticated or not hasattr(request.user, 'buyerprofile'):
        return redirect('login')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            total_price = product.price * quantity

            # Create order
            order = Order.objects.create(
                buyer=request.user,
                total_amount=total_price,
                status='Placed'
            )

            # Create order item
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            return render(request, 'orders/order_success.html', {
                'product': product,
                'order': order
            })

    else:
        form = OrderForm()

    return render(request, 'orders/place_order.html', {
        'product': product,
        'form': form
    })


@login_required
def my_orders(request):
    orders = Order.objects.filter(buyer=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})


@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, buyer=request.user)
    if order.status != 'Cancelled':
        order.status = 'Cancelled'
        order.save()
        messages.success(request, f"Order #{order.id} has been cancelled.")
    else:
        messages.info(request, f"Order #{order.id} is already cancelled.")
    return redirect('orders:my_orders')
