# 🎬 Looney Workspace - Docker Deployment Guide

## 🐳 Docker Setup

### Prerequisites
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed (included with Docker Desktop)

### Quick Start

**1. Build and run with Docker Compose:**
```bash
cd /Users/3treeforest/Desktop/DEV
docker-compose up -d
```

**2. Access the app:**
Open your browser to: http://localhost:8080

**3. Stop the container:**
```bash
docker-compose down
```

---

## 📦 Docker Commands

### Build the image manually:
```bash
docker build -t looney-workspace .
```

### Run without docker-compose:
```bash
docker run -d \
  --name looney-workspace \
  -p 8080:80 \
  looney-workspace
```

### View logs:
```bash
docker-compose logs -f
# or
docker logs looney-workspace
```

### Restart container:
```bash
docker-compose restart
# or
docker restart looney-workspace
```

### Stop and remove:
```bash
docker-compose down
# or
docker stop looney-workspace && docker rm looney-workspace
```

---

## 🌐 Deploy to Production

### Change the Port
Edit `docker-compose.yml`:
```yaml
ports:
  - "80:80"  # For port 80 (requires sudo)
  # or
  - "3000:80"  # For port 3000
```

### Run in production mode:
```bash
docker-compose up -d --build
```

---

## ☁️ Deploy to Cloud

### Deploy to AWS (EC2 or ECS)

**EC2 Deployment:**
```bash
# SSH into your EC2 instance
ssh -i your-key.pem ec2-user@your-ip

# Install Docker
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user

# Clone your repo or copy files
# Then run:
docker-compose up -d
```

**ECS Deployment:**
```bash
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URL
docker build -t looney-workspace .
docker tag looney-workspace:latest YOUR_ECR_URL/looney-workspace:latest
docker push YOUR_ECR_URL/looney-workspace:latest

# Create ECS task and service via AWS Console or CLI
```

---

### Deploy to DigitalOcean

**Droplet Deployment:**
```bash
# SSH into droplet
ssh root@your-droplet-ip

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Deploy
git clone YOUR_REPO
cd YOUR_REPO
docker-compose up -d
```

**DigitalOcean App Platform:**
1. Connect your GitHub repo
2. Select "Docker Hub" or "Dockerfile"
3. Set port to 80
4. Deploy!

---

### Deploy to Railway

**Method 1: From GitHub**
1. Push code to GitHub
2. Go to [Railway](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repo
5. Railway auto-detects Dockerfile
6. Deploy! 🚀

**Method 2: Railway CLI**
```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

---

### Deploy to Render

1. Push to GitHub
2. Go to [Render](https://render.com)
3. New → Web Service
4. Connect your repo
5. Select "Docker" as environment
6. Deploy!

---

### Deploy to Fly.io

```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Launch app
flyctl launch

# Deploy
flyctl deploy
```

---

### Deploy to Heroku (with Docker)

```bash
# Login to Heroku
heroku login
heroku container:login

# Create app
heroku create looney-workspace

# Build and push
heroku container:push web
heroku container:release web

# Open app
heroku open
```

---

## 🔒 Security Best Practices

### Add HTTPS with Nginx
Update `nginx.conf` to redirect HTTP to HTTPS:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;

    # ... rest of config
}
```

### Use Docker Secrets
For sensitive data:
```bash
echo "my_secret" | docker secret create my_secret -
```

---

## 📊 Monitoring

### Check container health:
```bash
docker ps
docker inspect looney-workspace
```

### View resource usage:
```bash
docker stats looney-workspace
```

### Health check endpoint:
```bash
curl http://localhost:8080
```

---

## 🔧 Troubleshooting

**Port already in use:**
```bash
# Find process using port
lsof -i :8080
# Kill it
kill -9 PID
# Or change port in docker-compose.yml
```

**Container won't start:**
```bash
# Check logs
docker logs looney-workspace

# Rebuild
docker-compose down
docker-compose up --build
```

**Clear everything and start fresh:**
```bash
docker-compose down -v
docker system prune -a
docker-compose up --build
```

---

## 🎯 Environment Variables

Add to `docker-compose.yml`:
```yaml
environment:
  - TZ=America/New_York
  - NODE_ENV=production
  - CUSTOM_VAR=value
```

---

## 📈 Scaling

### Run multiple instances:
```bash
docker-compose up -d --scale looney-workspace=3
```

### Use nginx load balancer:
```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    depends_on:
      - looney-workspace

  looney-workspace:
    build: .
    deploy:
      replicas: 3
```

---

## 🎬 That's All Folks!

Your Looney Workspace is now containerized and ready to deploy anywhere Docker runs!

**Need help?** Check the logs:
```bash
docker-compose logs -f
```

**Quick Commands Reference:**
```bash
docker-compose up -d          # Start
docker-compose down           # Stop
docker-compose logs -f        # View logs
docker-compose restart        # Restart
docker-compose ps             # Status
```

**Access your app:** http://localhost:8080

Beep beep! 🚗