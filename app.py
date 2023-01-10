from fastapi import FastAPI
main  = FastAPI()
@main.get('/') #this the path/route
def index():
    return "This is the front page"
# this is a page
@main.get('about') #this the path/route
def index():
    return "This is the about page"
# this is backend
