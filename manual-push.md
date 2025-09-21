# Manual Push Instructions

The automated push is encountering permission issues. Here's how to push manually:

## Option 1: GitHub Personal Access Token (Recommended)

1. **Create a new Personal Access Token:**
   - Go to: https://github.com/settings/tokens/new
   - Name: "PressWire Push Token"
   - Select scopes:
     - ✅ repo (all)
     - ✅ workflow
   - Click "Generate token"
   - **COPY THE TOKEN NOW** (you won't see it again)

2. **Push using the token:**
   ```bash
   git push https://YOUR_TOKEN@github.com/BuddySpuds/presswire-v2.git main
   ```
   Replace `YOUR_TOKEN` with the token you just copied.

## Option 2: Use GitHub Desktop

1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your GitHub account
3. Add this repository (File → Add Local Repository)
4. Click "Publish Repository" or "Push origin"

## Option 3: Re-authenticate GitHub CLI

1. **Logout and login again with full permissions:**
   ```bash
   gh auth logout
   gh auth login
   ```

2. When prompted:
   - Choose: GitHub.com
   - Protocol: HTTPS
   - Authenticate: Login with a web browser
   - **IMPORTANT**: When browser opens, grant ALL requested permissions

3. **After login, push again:**
   ```bash
   git push -u origin main
   ```

## Option 4: SSH Key Setup

1. **Generate SSH key (if you don't have one):**
   ```bash
   ssh-keygen -t ed25519 -C "your-email@example.com"
   ```

2. **Add SSH key to GitHub:**
   ```bash
   pbcopy < ~/.ssh/id_ed25519.pub
   ```
   - Go to: https://github.com/settings/keys
   - Click "New SSH key"
   - Paste the key
   - Save

3. **Switch to SSH and push:**
   ```bash
   git remote set-url origin git@github.com:BuddySpuds/presswire-v2.git
   git push -u origin main
   ```

## After Successful Push

Once pushed, your repository will have:
- ✅ All code uploaded
- ✅ GitHub Actions CI/CD ready
- ✅ Secrets configured (SUPABASE_URL, SUPABASE_KEY)

Next steps:
1. Go to: https://github.com/BuddySpuds/presswire-v2/actions
2. Check if the CI/CD workflow is running
3. Set up Digital Ocean app and add DO_APP_ID secret

## Current Repository Status

- **Local commits**: Ready to push
- **Repository**: https://github.com/BuddySpuds/presswire-v2
- **Secrets set**: SUPABASE_URL, SUPABASE_KEY
- **Workflow**: CI/CD pipeline configured