from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def xfound(request):
    return render(request, '404.html')
    
def categoGrid(request):
    return render(request, 'categories-grid.html')

def categoList(request):
    return render(request, 'categories-list.html')

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    return render(request, 'signin.html')

def singlePost(request):
    return render(request, 'single-post.html')

def typography(request):
    return render(request, 'typography.html')