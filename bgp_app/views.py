from django.shortcuts import render


def index(request):
    """Main page 'BGP'"""
    return render(request, 'bgp_app/index.html')

# Create your views here.
