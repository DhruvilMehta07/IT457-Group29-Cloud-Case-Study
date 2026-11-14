#!/bin/bash
# Stage B deployment on a fresh Ubuntu 24.04 EC2 machine.
# Run these steps over SSH as the ubuntu user. Log out and back in after step 1
# so the docker group change applies, then run the rest.
set -e

# 1. Install the tools
sudo apt update
sudo apt install -y docker.io docker-compose-v2 git curl nginx postgresql-client
sudo usermod -aG docker ubuntu

# --- log out and log in again here ---

# 2. Get the code and start the app and its database in containers
git clone https://github.com/DhruvilMehta07/IT457-Group29-Cloud-Case-Study.git
cd IT457-Group29-Cloud-Case-Study
STAGE=B-ec2 docker compose -f docker/docker-compose.yml up --build -d

# 3. Check the app on the machine
docker compose -f docker/docker-compose.yml ps
curl -s http://localhost:8080/health

# 4. Put Nginx in front on port 80
sudo cp infra/nginx-telemetry.conf /etc/nginx/sites-available/telemetry
sudo ln -sf /etc/nginx/sites-available/telemetry /etc/nginx/sites-enabled/telemetry
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
# A plain reload did not drop the default site for us, a restart did.
sudo systemctl restart nginx
curl -s http://localhost/health
