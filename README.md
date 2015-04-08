# Technical Test 1 #
## Deploying and running on docker ##
First of all you will need to clone the repo :)
```
git clone https://github.com/temp-omarti/test-1.git
```
When you have the repo locally build the image
```
docker build -t nginx_test .
```
And run it! :)
```
docker run -d -p 80 nginx_test
```
To access with http you will have to know the mapped port:
```
docker ps -l
# take the name, for example reverent_poincare and look at the assignated port
docker port reverent_poincare
```
With this you can start doing requests to your API.
