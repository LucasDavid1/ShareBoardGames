FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install -y python3-pip

WORKDIR /app

COPY . /app

RUN apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*

RUN apt install nodejs
RUN apt install npm
RUN npm install ./Frontend/boardgames
RUN pip3 install --no-cache-dir -r /app/Backend/games/requirements.txt

RUN docker-compose up
CMD ["python3", "app/upload_data.py"]

RUN python3 app/Backend/games/games/manage.py runserver
CMD ["npm run serve", "app/Frontend/boardgames"]