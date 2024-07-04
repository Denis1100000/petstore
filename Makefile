IMAGE_NAME=petstore_autotests


build:
	docker build -t $(IMAGE_NAME) .

run-docker: build
	docker run -d $(IMAGE_NAME):latest

run-tests-allure:
	pytest tests --alluredir=./allure-results
	allure generate -c ./allure-results -o ./allure-report
	allure serve
