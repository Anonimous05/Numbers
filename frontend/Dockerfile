FROM node:16.10.0

WORKDIR /app

COPY package.json .

RUN yarn

COPY . .

CMD ["yarn", "start"]
