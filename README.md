# FaceDetector

Установка библиотек
pip install -r requirements.txt

Создать файл .env с содержимым
AWS_ACCESS_KEY=
AWS_SECRET_KEY=
AWS_REGION=


Запуск сервера
python manage.py runserver


Пример запроса curl
curl -i -X POST \
   -H "Content-Disposition:attachment; filename=*" \
   -H "Content-Type:image/jpeg" \
   --data-binary '@./images/man_face.jpeg' \
 'http://localhost:8000/api/facedetect/'

Фото должно быть формата .jpg или .png

