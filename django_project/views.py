import requests
from django.shortcuts import render

def home(request):
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  data = response.json()
  jokes = data['setup']

  response = requests.get('https://catfact.ninja/fact')
  data = response.json()
  facts = data['fact']

  response = requests.get('http://api.genderize.io?name=james') 
  data = response.json()
  gender = data['count'] 

  response = requests.get('https://www.boredapi.com/api/activity')
  data = response.json()
  activity = data['activity']

  response = requests.get('https://dog.ceo/api/breeds/image/random')
  data = response.json()
  dog = data['message']
  
  return render (request, 'templates/index.html', {'jokes': jokes, 'facts': facts, 'gender': gender, 'activity': activity, 'dog': dog})
  