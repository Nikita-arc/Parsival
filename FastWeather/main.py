from pyowm.owm import OWM
from pyowm.utils import timestamps

city = input("Введите город: ")
owm = OWM('f6ca5a914137655de9104050055910bf')
mgr = owm.weather_manager()


observation = mgr.weather_at_place(city)
w = observation.weather

temp = w.temperature('celsius')['temp']
wind = w.wind()

print("в городе " + city + " сейчас " + str(temp) + " градусов!")
print("Сила ветра" + str(wind))