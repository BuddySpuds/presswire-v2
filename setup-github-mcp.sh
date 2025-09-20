#!/bin/bash

echo "🚀 GitHub MCP Setup for PressWire v2"
echo "===================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${YELLOW}GitHub CLI not found. Installing...${NC}"

    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install gh
    else
        # Linux
        curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
        sudo apt update
        sudo apt install gh
    fi
fi

echo -e "${GREEN}✅ GitHub CLI is installed${NC}"

# Authenticate with GitHub
echo ""
echo "Authenticating with GitHub..."
gh auth status &> /dev/null

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}Not authenticated. Starting login process...${NC}"
    gh auth login
else
    echo -e "${GREEN}✅ Already authenticated with GitHub${NC}"
fi

# Create repository secrets
echo ""
echo "Setting up GitHub repository secrets..."
echo -e "${YELLOW}We need to set up the following secrets:${NC}"
echo "1. SUPABASE_URL"
echo "2. SUPABASE_KEY"
echo "3. DIGITALOCEAN_ACCESS_TOKEN"
echo "4. DO_APP_ID"

# Read .env file if it exists
if [ -f .env ]; then
    echo -e "${GREEN}Found .env file. Reading Supabase credentials...${NC}"
    source .env

    # Set Supabase secrets
    if [ ! -z "$SUPABASE_URL" ]; then
        gh secret set SUPABASE_URL --body="$SUPABASE_URL"
        echo -e "${GREEN}✅ Set SUPABASE_URL${NC}"
    fi

    if [ ! -z "$SUPABASE_KEY" ]; then
        gh secret set SUPABASE_KEY --body="$SUPABASE_KEY"
        echo -e "${GREEN}✅ Set SUPABASE_KEY${NC}"
    fi
fi

# Prompt for Digital Ocean credentials
echo ""
echo -e "${YELLOW}Digital Ocean Setup${NC}"
echo "You'll need:"
echo "1. A Digital Ocean Access Token"
echo "2. Your Digital Ocean App ID (after creating the app)"
echo ""
read -p "Enter your Digital Ocean Access Token (or press Enter to skip): " DO_TOKEN

if [ ! -z "$DO_TOKEN" ]; then
    gh secret set DIGITALOCEAN_ACCESS_TOKEN --body="$DO_TOKEN"
    echo -e "${GREEN}✅ Set DIGITALOCEAN_ACCESS_TOKEN${NC}"
fi

read -p "Enter your Digital Ocean App ID (or press Enter to skip): " DO_APP_ID

if [ ! -z "$DO_APP_ID" ]; then
    gh secret set DO_APP_ID --body="$DO_APP_ID"
    echo -e "${GREEN}✅ Set DO_APP_ID${NC}"
fi

# Push to GitHub
echo ""
echo "Pushing repository to GitHub..."

# Add all changes
git add .

# Commit GitHub Actions and MCP config
git commit -m "Add GitHub Actions CI/CD and MCP configuration

- GitHub Actions workflow for CI/CD
- MCP configuration for GitHub, Digital Ocean, and Playwright
- Automated testing and deployment pipeline"

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Successfully pushed to GitHub!${NC}"

    # Get repository URL
    REPO_URL=$(gh repo view --json url -q .url)

    echo ""
    echo "================================"
    echo -e "${GREEN}🎉 Setup Complete!${NC}"
    echo "================================"
    echo ""
    echo "Repository: $REPO_URL"
    echo "Actions: $REPO_URL/actions"
    echo ""
    echo "Next steps:"
    echo "1. Go to $REPO_URL/settings/secrets/actions to verify secrets"
    echo "2. Create a Digital Ocean app at https://cloud.digitalocean.com/apps"
    echo "3. Update DO_APP_ID secret with your app ID"
    echo "4. Push any change to trigger the CI/CD pipeline"
else
    echo -e "${RED}❌ Failed to push to GitHub${NC}"
    echo "You may need to:"
    echo "1. Set up GitHub authentication: gh auth login"
    echo "2. Or manually push: git push -u origin main"
fi

echo ""
echo "MCP Features Enabled:"
echo "✅ GitHub Issues and PRs"
echo "✅ GitHub Actions CI/CD"
echo "✅ Digital Ocean Deployment"
echo "✅ Playwright E2E Testing"