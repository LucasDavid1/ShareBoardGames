# ShareBoardGames
Platform to share board games on demand

### Instalación

##### Backend:
```
cd Backend/games
pip3 install requirements.txt

cd Backend/games/games
python3 manage.py run serve
```
La API va a estar corriendo en el puerto 8000

##### Frontend:
```
cd Frontend/boardgames
npm install
npm run serve
```
El front va a estar corriendo en el puerto 8080

##### MongoDB Docker

```
docker-compose up
```
