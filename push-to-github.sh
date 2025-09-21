#!/bin/bash

echo "🚀 PressWire v2 - GitHub Push Helper"
echo "====================================="

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo -e "${YELLOW}This script will help you push your code to GitHub${NC}"
echo ""

# Method selection
echo "Choose your authentication method:"
echo "1) Personal Access Token (Recommended - 2 minutes)"
echo "2) GitHub CLI re-authentication"
echo "3) SSH Key"
echo ""
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo -e "${YELLOW}Personal Access Token Method${NC}"
        echo "=============================="
        echo ""
        echo "Steps:"
        echo "1. Open this URL: https://github.com/settings/tokens/new"
        echo "2. Token name: 'PressWire Push'"
        echo "3. Select scopes:"
        echo "   ✅ repo (all checkboxes)"
        echo "   ✅ workflow"
        echo "4. Click 'Generate token'"
        echo "5. COPY THE TOKEN (you won't see it again!)"
        echo ""
        read -p "Paste your token here: " TOKEN

        if [ -z "$TOKEN" ]; then
            echo -e "${RED}No token provided. Exiting.${NC}"
            exit 1
        fi

        echo ""
        echo "Pushing to GitHub..."
        git push https://$TOKEN@github.com/BuddySpuds/presswire-v2.git main

        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ Successfully pushed to GitHub!${NC}"
            echo ""
            echo "Repository: https://github.com/BuddySpuds/presswire-v2"
            echo "Actions: https://github.com/BuddySpuds/presswire-v2/actions"
        else
            echo -e "${RED}❌ Push failed. Please check your token and try again.${NC}"
        fi
        ;;

    2)
        echo ""
        echo -e "${YELLOW}GitHub CLI Authentication${NC}"
        echo "========================="
        echo ""
        echo "This will open your browser for authentication."
        echo "IMPORTANT: Grant ALL requested permissions!"
        echo ""
        read -p "Press Enter to continue..."

        gh auth login --web --scopes repo,workflow,admin:org

        if [ $? -eq 0 ]; then
            echo ""
            echo "Configuring git to use GitHub CLI..."
            gh auth setup-git

            echo "Pushing to GitHub..."
            git push -u origin main

            if [ $? -eq 0 ]; then
                echo -e "${GREEN}✅ Successfully pushed to GitHub!${NC}"
            else
                echo -e "${RED}❌ Push failed. Trying token method...${NC}"
                echo ""
                echo "The GitHub CLI method failed. Please use option 1 (Personal Access Token) instead."
            fi
        else
            echo -e "${RED}❌ Authentication failed${NC}"
        fi
        ;;

    3)
        echo ""
        echo -e "${YELLOW}SSH Key Method${NC}"
        echo "=============="
        echo ""

        # Check for existing SSH key
        if [ -f ~/.ssh/id_ed25519.pub ]; then
            echo "Found existing SSH key."
            echo "Copying to clipboard..."
            pbcopy < ~/.ssh/id_ed25519.pub
            echo -e "${GREEN}✅ SSH key copied to clipboard${NC}"
        else
            echo "No SSH key found. Generating one..."
            read -p "Enter your email: " EMAIL
            ssh-keygen -t ed25519 -C "$EMAIL" -f ~/.ssh/id_ed25519 -N ""
            pbcopy < ~/.ssh/id_ed25519.pub
            echo -e "${GREEN}✅ SSH key generated and copied to clipboard${NC}"
        fi

        echo ""
        echo "Steps:"
        echo "1. Go to: https://github.com/settings/keys"
        echo "2. Click 'New SSH key'"
        echo "3. Title: 'PressWire Dev Machine'"
        echo "4. Paste the key (already in clipboard)"
        echo "5. Click 'Add SSH key'"
        echo ""
        read -p "Press Enter after adding the key to GitHub..."

        echo ""
        echo "Switching to SSH remote..."
        git remote set-url origin git@github.com:BuddySpuds/presswire-v2.git

        echo "Testing SSH connection..."
        ssh -T git@github.com

        echo ""
        echo "Pushing to GitHub..."
        git push -u origin main

        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ Successfully pushed to GitHub!${NC}"
        else
            echo -e "${RED}❌ Push failed. Please verify SSH key was added correctly.${NC}"
        fi
        ;;

    *)
        echo -e "${RED}Invalid choice. Exiting.${NC}"
        exit 1
        ;;
esac

echo ""
echo "================================"
echo "After successful push, check:"
echo "• Repository: https://github.com/BuddySpuds/presswire-v2"
echo "• Actions: https://github.com/BuddySpuds/presswire-v2/actions"
echo "• Settings: https://github.com/BuddySpuds/presswire-v2/settings"
echo ""
echo "The CI/CD pipeline will automatically start!"
echo "================================"