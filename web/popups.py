from django.views.generic import TemplateView
from django_popup_view_field.registry import registry_popup_view

class ColorsPopupView(TemplateView):
    template_name = 'web/popups/colors.html'

# REGISTER IS IMPORTANT
registry_popup_view.register(ColorsPopupView)