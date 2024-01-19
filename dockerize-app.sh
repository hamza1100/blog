touch Dockerfile

echo 'FROM python:3' > Dockerfile
echo 'RUN pip3 install django' >> Dockerfile
echo 'COPY . .' >> Dockerfile
echo 'RUN python3 -m pip install Pillow' >> Dockerfile 
echo 'Run python3 manage.py migrate' >> Dockerfile
echo 'CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]' >> Dockerfile

image_tag="blog-app"

sudo docker build -t "$image_tag" .

sudo docker run -p 8000:8000 "$image_tag"