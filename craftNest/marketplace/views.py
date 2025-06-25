from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    html_content="""
    <html>
    <head>
    <title>Craft Nest</title>
    </head>
    <body>
    <p>Connecting You with Local Artisans & Handmade Treasures</p>

        <h2>Explore Categories</h2>
        <ul>
            <li>Home Decor</li>
            <li>Jewelry</li>
            <li>Pottery</li>
            <li>Handwoven</li>
        </ul>

        <h2>Featured Products</h2>
        <ul>
            <li>
                <strong>Macrame Wall Hanging</strong><br>
                By: Artisan A
            </li>
            <li>
                <strong>Clay Mug Set</strong><br>
                By: Artisan B
            </li>
            <li>
                <strong>Beaded Necklace</strong><br>
                By: Artisan C
            </li>
        </ul>

        <h2>Why Choose CraftNest?</h2>
        <p>Support local creators, discover unique handcrafted items, and shop ethically.</p>

        <h2>Become a Seller</h2>
        <p><a href="/signup/">Sign up now</a> to showcase your craft to the world!</p>

        <hr>
        <p>© 2025 CraftNest. All rights reserved.</p>
    
    </body>
    </html>
    """
    return HttpResponse(html_content)

def product_list(request):
    html_content="""
    <html>
    <head>
    <title>Craft Nest- Product List</title>
    </head>
    <body>
    <h2>Product List Page</h2>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def contact_us(request):
    html_content="""
    <html>
    <head>
    <title>Craft Nest- Contact Us</title>
    </head>
    <h2>Contact Us Page</h2>
    </body>
    </html>
    """
    return HttpResponse(html_content)



