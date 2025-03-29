from sqlalchemy.orm import Session
from app.db.models import City


def create_popular_russian_cities(db: Session):
    cities = [
        "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
        "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону",
        "Уфа", "Красноярск", "Пермь", "Воронеж", "Волгоград",
        "Краснодар", "Саратов", "Тюмень", "Тольятти", "Ижевск"
    ]

    for city_name in cities:
        if not db.query(City).filter(City.city_name == city_name).first():
            db_city = City(city_name=city_name)
            db.add(db_city)
    db.commit()