# Stage 1: Build Vue.js App
FROM node:14 AS builder

WORKDIR /

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Stage 2: Serve the built app using Nginx
FROM nginx:alpine

# Remove the default Nginx welcome page
RUN rm -rf /usr/share/nginx/html/*

# Copy the built app from the builder stage to the Nginx container
COPY --from=builder /dist /usr/share/nginx/html

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]
