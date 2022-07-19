from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("""
        <h1>
        <font size="10" face="Times" color="#8B008B">
        Olá Mundo!
        </h1></font>
        <h2>
        <font size="4" face="Verbena" color="#4B0082">
        <p>Você está na página principal do site.</p>
        <p>Esta é a página em desenvolvimento.</p>
        </h2> </font>
        <i>Você está vendo um projeto do Hugo Marinho.</i>

    """)