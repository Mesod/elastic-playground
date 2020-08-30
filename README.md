# elastic-playground

### Installation

Install the dependencies and devDependencies and start the server.

```sh
$ docker start
$ docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.5.2
$ pip install -r requirements.txt
$ 
```
