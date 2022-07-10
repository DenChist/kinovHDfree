# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Не создаем .pyc файлы
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
   && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install gcc python3-dev musl-dev -y
RUN pip install --upgrade pip
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
ADD . .
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt