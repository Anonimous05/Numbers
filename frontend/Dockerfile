FROM node:16.10.0

WORKDIR /app

COPY package.json /app

RUN yarn && yarn add react-scripts

COPY . /app

CMD ["yarn", "start"]
