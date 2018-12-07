FROM ethereum/client-go:v1.8.19

RUN apk add --update git bash nodejs nodejs-npm perl

WORKDIR /root/api-app

COPY ./api-app /root/api-app

RUN npm install &&\
    npm install -g pm2

ADD start.sh /root/start.sh
ADD app.json /root/api-app/app.json
RUN chmod +x /root/start.sh

ENTRYPOINT /root/start.sh
