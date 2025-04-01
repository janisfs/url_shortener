# URL Shortener

Сервис для сокращения URL-адресов, разработанный с использованием FastAPI.

## Запуск с использованием Docker

### Предварительные требования

- Установленный Docker
- Установленный Docker Compose (обычно входит в состав Docker Desktop)

### Шаги для запуска

1. Клонируйте репозиторий:

 git clone <https://github.com/janisfs/url_shortener.git>
 cd url_shortener

2.Запустите контейнер с помощью Docker Compose:

docker-compose up -d

3.Сервис будет доступен по адресу: <http://localhost:8000>
Документация API: <http://localhost:8000/docs>

### Использование

-Для создания короткой ссылки отправьте POST-запрос на <http://localhost:8000/> с параметром url
-Пример с использованием curl:

curl -X POST "<http://localhost:8000/?url=google.com>"

-Или используйте Swagger UI по адресу <http://localhost:8000/docs>

### Остановка контейнера

docker-compose down

### requirements.txt

Если вы уже создали Docker-контейнер и он успешно работает, то ваш текущий файл requirements.txt содержит все необходимые зависимости. Однако, если вы планируете добавлять новые функции, которые требуют дополнительных библиотек, не забудьте обновить requirements.txt.

После обновления requirements.txt вам нужно будет пересобрать Docker-образ:

docker-compose up -d --build
