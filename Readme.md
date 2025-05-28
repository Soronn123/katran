# 🛡️ Katran – система бронирования авиабилетов  

![Katran Preview](https://github.com/Soronn123/Katran/blob/main/static/favicon.svg)  

**Современная платформа для поиска и бронирования авиабилетов**  
Разработана на Python 3.13.3 с использованием Django и Tailwind CSS  

---

## 🛠 Технологии  
- **Backend**: Python 3.13.3 + Django  
- **Frontend**: Tailwind CSS, HTML5  

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/Soronn123/Katran.git
cd Katran
```

### 2. Создание и активация виртуального окружения
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка окружения (.env)
Создайте файл `.env` в корне проекта и заполните его по примеру:
```ini
SECRET_KEY=ваш_секретный_ключ
DEBUG=False
NPM_BIN_PATH=путь_к_npm
```
> 🔑 **Где взять `SECRET_KEY`?**  
> Можно сгенерировать [здесь](https://djecrety.ir/) или использовать команду:  
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

> 🔑 **Для чего `NPM_BIN_PATH`?**  
> Используется для корректной работы tailwindCss

### 5. Запуск сервера
```bash
python manage.py runserver
```
Откройте в браузере: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ⚙️ Дополнительные команды

### Создание суперпользователя (админка)
```bash
python manage.py createsuperuser
```

### Загрузка тестовых данных
```bash
python manage.py loaddata фикстура.json
```

---

## 📁 Структура проекта
```
Katran/
├── Katran/                 # Основное приложение
├── Accounts/               # Данные пользователей
├── Services/               # Данные товаров и услуг
├── media/                  # Храняться Изображения
├── static/                 # 
├── staticfiles/            # Собранные данные с статик и theme(tailwindCss)
├── templates/              # Шаблоны
├── theme/                  # Стили TailwindCss
├── .env-example/           # Пример .env
├── db.sqlite3              # Готовая база данных
├── manage.py
└── requirements.txt
```

Разработано с ❤️ для безопасности!  
2025 | lieQueen