import requests


def get_weather(api_key: str, city: str, country: str) -> None:
    """Данные о погоде.

    Получает текущие данные о погоде для заданного города и страны
    с использованием Weatherbit API.

    Args:
        api_key: Ваш API-ключ от Weatherbit.
        city: Название города.
        country: Код страны (например, 'RU' для России).
    """
    base_url = "https://api.weatherbit.io/v2.0/current"
    params = {
        "city": city,
        "country": country,
        "key": api_key,
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        if "data" in weather_data and len(weather_data["data"]) > 0:
            weather = weather_data["data"][0]
            print(f"Погода в {city}, {country}:")
            print(f"Температура: {weather['temp']}°C")
            print(f"Ощущается как: {weather['app_temp']}°C")
            print(f"Описание: {weather['weather']['description']}")
            print(f"Влажность: {weather['rh']}%")
            print(f"Скорость ветра: {weather['wind_spd']} м/с")
            print(f"Направление ветра: {weather['wind_cdir_full']}")
        else:
            print(f"Не удалось получить данные о погоде для {city}, {country}.")
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")


def main() -> None:
    """
    Основная функция для выполнения запроса и вывода данных о погоде.
    """
    api_key = "bd05567eb32b4bfb87a82aa8d48cf768"
    city = "Moscow"
    country = "RU"
    get_weather(api_key, city, country)


if __name__ == "__main__":
    main()
