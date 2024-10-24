# Stage 1: Build React app
FROM node:16-alpine AS build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./

RUN npm install --force

COPY frontend/. .

RUN npm run build

