FROM oven/bun:1.2.22

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN bun install


# Copy the rest of the frontend code
COPY . .

# Build the React application
RUN bun run dev

# Serve the application
CMD ["bunx", "serve", "-s", "dist" "-l" "3000"]