from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
  
  peoples = [
    {'name': 'Rohan Paudel' , 'age': 20},
    {'name': 'Bishwas Baral' , 'age': 24},
    {'name': 'Avinash Lamichanne' , 'age': 22},
    {'name': 'Aakash Basnet' , 'age': 23},
    {'name': 'Roshan Chand' , 'age': 21},
    
  ]
  
  for people in peoples:
    if people['age']:
      print("yes")
  
  vegetables = ['Pumpkin' , 'Tomato' , 'Potatoes']
  

  
  
  return render(request , "index.html" , context = { 'page': 'Home' , 'peoples' : peoples , 'vegetables' : vegetables})

def about(request):
  context = {'page' : 'About'}
  return render(request , "about.html" , context)

def contact(request):
  context = {'page' : 'Contact'}
  return render(request , "contact.html", context)
  
def success_page(request):
  context = {'page' : 'Success page'}
  print("*" * 10)
  return HttpResponse("<h1> Hey this is a Success Page</h1>" , context)
