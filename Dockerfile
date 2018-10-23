FROM nginx:1.15.5-alpine

WORKDIR /usr/share/nginx/html

COPY blog/* ./

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]

