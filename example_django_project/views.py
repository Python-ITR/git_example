from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def main_page(req: HttpRequest) -> HttpResponse:
    return render(req, "index.html")

