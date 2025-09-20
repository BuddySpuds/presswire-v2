# GitHub MCP Integration for PressWire v2

## Overview

GitHub MCP (Model Context Protocol) provides enhanced control over GitHub operations, CI/CD pipelines, and deployment automation for PressWire v2.

## Features Enabled

### 1. **GitHub Integration**
- Automated issue management
- Pull request automation
- Branch protection rules
- Release management
- Webhook configuration

### 2. **CI/CD Pipeline**
- Automated testing on every push
- Docker container building and registry
- Deployment to Digital Ocean
- Playwright E2E testing

### 3. **Digital Ocean Deployment**
- Automated app deployment
- Environment variable management
- Health checks and monitoring
- Automatic rollback on failure

## Setup Instructions

### Prerequisites

1. **GitHub Personal Access Token**
   - Go to: https://github.com/settings/tokens/new
   - Create token with scopes:
     - `repo` - Full repository control
     - `workflow` - Update GitHub Actions
     - `write:packages` - Upload Docker images

2. **Digital Ocean Access Token**
   - Go to: https://cloud.digitalocean.com/account/api/tokens
   - Generate new token with write access

3. **GitHub CLI Installation**
   ```bash
   # macOS
   brew install gh

   # Ubuntu/Debian
   sudo apt install gh
   ```

### Quick Setup

Run the automated setup script:
```bash
./setup-github-mcp.sh
```

This script will:
1. Install GitHub CLI if needed
2. Authenticate with GitHub
3. Set up repository secrets
4. Push code to GitHub
5. Configure CI/CD pipeline

### Manual Setup

#### 1. Authenticate with GitHub CLI
```bash
gh auth login
```

#### 2. Set Repository Secrets
```bash
# Supabase credentials
gh secret set SUPABASE_URL --body="your-supabase-url"
gh secret set SUPABASE_KEY --body="your-supabase-key"

# Digital Ocean credentials
gh secret set DIGITALOCEAN_ACCESS_TOKEN --body="your-do-token"
gh secret set DO_APP_ID --body="your-app-id"
```

#### 3. Push to GitHub
```bash
git add .
git commit -m "Add GitHub MCP configuration"
git push -u origin main
```

## MCP Configuration

The `mcp-config.json` file defines:
- GitHub server configuration
- Digital Ocean integration
- Playwright test settings
- CI/CD pipeline configuration

## GitHub Actions Workflow

The workflow (`.github/workflows/ci-cd.yml`) includes:

### Test Stage
- Runs Python tests
- Validates code quality
- Checks dependencies

### Build Stage
- Builds Docker container
- Pushes to GitHub Container Registry
- Tags with commit SHA

### Deploy Stage (main branch only)
- Deploys to Digital Ocean
- Updates environment variables
- Verifies deployment health

### Playwright Stage
- Runs E2E browser tests
- Captures screenshots on failure
- Generates test reports

## Digital Ocean App Configuration

### Create App
1. Go to: https://cloud.digitalocean.com/apps
2. Click "Create App"
3. Connect GitHub repository
4. Configure:
   - Name: `presswire-v2`
   - Region: Choose nearest
   - Branch: `main`
   - Autodeploy: Enable

### Environment Variables
Set in Digital Ocean App Platform:
```
SUPABASE_URL=your-url
SUPABASE_KEY=your-key
APP_ENV=production
APP_DEBUG=false
```

### Deployment Settings
- Instance: Basic ($5/month for testing)
- Scaling: 1-3 instances
- Health check: `/health`
- Port: 8000

## Using GitHub MCP

### Create Issue
```bash
gh issue create --title "Bug: Description" --body "Details"
```

### Create Pull Request
```bash
gh pr create --title "Feature: New feature" --body "Description"
```

### View Deployment Status
```bash
gh run list
gh run view
```

### Trigger Manual Deployment
```bash
gh workflow run ci-cd.yml
```

## Monitoring

### GitHub Actions
- URL: https://github.com/BuddySpuds/presswire-v2/actions
- View build logs
- Check deployment status

### Digital Ocean
- URL: https://cloud.digitalocean.com/apps
- Monitor app health
- View deployment logs
- Check resource usage

## Troubleshooting

### Push Permission Denied
```bash
gh auth refresh
gh auth status
```

### Secrets Not Working
```bash
gh secret list
gh secret set SECRET_NAME
```

### Deployment Failing
1. Check GitHub Actions logs
2. Verify Digital Ocean app settings
3. Check environment variables
4. Review app logs in DO dashboard

## Advanced Features

### Auto-scaling
Configure in Digital Ocean:
- Min instances: 1
- Max instances: 5
- CPU threshold: 70%
- Memory threshold: 80%

### Custom Domains
1. Add domain in DO app settings
2. Configure DNS:
   - A record → DO app IP
   - CNAME → app URL

### SSL Certificates
- Automatically managed by Digital Ocean
- Force HTTPS in app settings

## Best Practices

1. **Branch Protection**
   - Require PR reviews
   - Require status checks
   - Dismiss stale reviews

2. **Secrets Management**
   - Never commit secrets
   - Use GitHub secrets
   - Rotate tokens regularly

3. **Deployment**
   - Test in staging first
   - Use gradual rollout
   - Monitor after deployment

## Support

- GitHub Issues: https://github.com/BuddySpuds/presswire-v2/issues
- Documentation: /docs
- Digital Ocean Support: https://www.digitalocean.com/support/