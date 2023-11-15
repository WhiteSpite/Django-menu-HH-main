from django.shortcuts import render
    
    
def menu_view(request, slug=''):
    context = {'slug': slug}
    return render(request, 'default.html', context)
        
