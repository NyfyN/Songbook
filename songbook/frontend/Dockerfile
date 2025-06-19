FROM node:22

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm i -g pnpm
RUN pnpm i

# Copy the rest of the frontend code
COPY . .

# Build the React application
RUN pnpm run build

# Serve the application
CMD ["npx", "serve", "-s", "build"]
