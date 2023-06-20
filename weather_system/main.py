from weather_station import weatherStation
from mobile_app import mobileAppUpdate
from web_app import webAppUpdate
from desktop_app import desktopAppUpdate

if __name__ == '__main__':
    weather_station = weatherStation()

    mobile_app_update = mobileAppUpdate()
    web_app_update = webAppUpdate()
    desktop_app_update = desktopAppUpdate()

    weather_station.add_observer(mobile_app_update)
    weather_station.add_observer(web_app_update)
    weather_station.add_observer(desktop_app_update)

    weather_station.start_monitoring()
