def show_me(request):
    context = {}
    context['company'] = "Femme"    
    context['full_address'] = "A108 Adam Street, New York, NY 535022"    
    context['phone'] = "+27 67 106 6600"    
    context['tel'] =  "+27 12 023 2101"    
    return context