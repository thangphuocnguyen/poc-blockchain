FROM node:8-alpine

WORKDIR /app
COPY . /app

RUN npm install
RUN npm install -g grunt-cli
RUN grunt

EXPOSE 3000

CMD ["npm", "start"]
