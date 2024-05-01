from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    html = """
        <div style='margin: 0 auto; text-align: center;'>
            <h1>Home page</h1>
            <a href = 'about/'>About us</a></br></br>
            
            <a href = '/'>Return to main page</a>
        </div>
    """
    logger.info('Обработана страница Home page')
    return HttpResponse(html)


def about(request):
    html = """
        <div style='margin: 0 auto; text-align: center;'>
            <h1>About us</h1>
            <a href = '/hw1'>Home page</a></br></br>
            
            <a href = '/'>Return to main page</a>
        </div>
    """
    logger.info('Обработана страница About us')
    return HttpResponse(html)
