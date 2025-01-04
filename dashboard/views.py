from django.shortcuts import render
from .helper import get_weather, get_travel_recommendations


def index(request):
    if request.method == 'POST':
        city_name = request.POST.get('city_name')
        
        try:
            # Fetch weather data
            weather = get_weather(city_name)
            
            # Get travel recommendations from the model
            recommendations = get_travel_recommendations(
                city_name, weather["temperature"], weather["conditions"]
            )
            
            return render(request, 'dashboard/index.html', {
                'city_name': city_name,
                'weather': weather,
                'recommendations': recommendations
            })
        
        except Exception as e:
            return render(request, 'dashboard/index.html', {'city_name': city_name,'error': f"An error occurred: {str(e)}"})
    
    return render(request, 'dashboard/index.html')




def about(request):
    return render(request,'dashboard/about.html')

def contact(request):
    return render(request,'dashboard/contact.html')