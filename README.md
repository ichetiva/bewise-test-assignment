# Bewise test assignment

### Running:
1. Rename `.example.env` to `.env` and setting it
2. Create docker network (just once)
```
docker network create bewise
```
3. Build and run docker compose
```
docker-compose build
docker-compose up
```
4. Go to API: http://localhost:8080/

### Example with curl creates 10 questions:
```
curl -X 'POST' \
  'http://localhost:8080/api/questions/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 10
}'
```
