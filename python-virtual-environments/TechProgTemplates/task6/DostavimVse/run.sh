./wait-for-it.sh db:3306 --timeout=90
./mvnw spring-boot:run -P init-base
./mvnw spring-boot:run -P web-app
