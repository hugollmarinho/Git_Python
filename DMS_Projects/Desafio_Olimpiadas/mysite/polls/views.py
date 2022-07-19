from django.http import HttpResponse
from django.utils.translation import gettext as _


def index(request):
    output = _("Hello, world. You're at the polls index.")
    return HttpResponse(output)

