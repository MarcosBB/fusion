from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
class Erro404View(TemplateView):
    template_name = '404.html'

class Erro500View(TemplateView):
    template_name = '500.html'