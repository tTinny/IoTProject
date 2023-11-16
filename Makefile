run:
	sudo docker run --restart always --name emqx_subscribe -d emqx_data_subscribe

build:
	sudo docker build -t emqx_data_subscribe .

rebuild:
	sudo docker rm -f emqx_subscribe 
	sudo docker build -t emqx_data_subscribe .
	sudo docker run --restart always --name emqx_subscribe -d emqx_data_subscribe

logs:
	sudo docker logs -f emqx_subscribe