from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html" 


class CursoPage(TemplateView):
    template_name = "cursos.html"

class SobrePage(TemplateView):
    template_name = "sobre.html"