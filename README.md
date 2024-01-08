# Проект: blog_project

Создание сайт-блога на главной странице которого будет отображаться список постов. 
Администраторы сайта могут создавать новые посты. При нажатии на пост пользователь 
будет перенаправлен на отдельную страницу, где будет отображаться выбранный пост
и комментарии, оставленные под ним. Комментарии могут оставлять
любые зарегистрировавшиеся пользователи

## Запуск проекта

Для запуска проекта нужно запустить сервер backend в терминале pycharm командой в папке проекта:
python manage.py runserver запустить серверную часть по адресу: http://127.0.0.1:8000/ -для работы с api.
или в в настройке  Edit configurations.
Далее нужно запустить приложение фронтенда в папке фронтенда командой: npm run dev
Запустить приложение фронтенда по адресу: http://localhost:5173/

На главной странице зарегистрироваться и войти на страницу http://localhost:5173/posts под своим логином.
На странице можно создавать посты только пользователям с допуском. Выбираете пост и комментируете.

### Предварительные требования

Предварительно нужно загрузить сдедующие приложения:

- Установите Node.js с официального сайта Node.js (https://nodejs.org/).
- NPM (Node Package Manager) - устанавливается вместе с Node.js
- Остальное взять из зависимостей файла requirements.txt

### Установка

1. Склонировать репозиторий на  компьютере: 


   git clone https://github.com/Eduard6315/blog_website