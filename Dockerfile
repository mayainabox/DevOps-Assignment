# Use the Alpine Linux base image
FROM alpine:latest

# Install Nginx
RUN apk add --update nginx

# Copy your HTML files to the web root
COPY ./html /usr/share/nginx/html

# Expose ports
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
