# Publishing to GitHub Pages

## Step-by-Step Guide

### 1. Create GitHub Account (if needed)
- Go to [github.com](https://github.com)
- Click "Sign up"
- Choose free plan

### 2. Create New Repository

**Option A: Upload Files Manually**
1. Click "+" icon (top right) → "New repository"
2. Name: `microbit-challenge-generator`
3. Description: "Free web tool for micro:bit coding challenges"
4. Public repository
5. ✅ Check "Add a README file"
6. Click "Create repository"
7. Click "Add file" → "Upload files"
8. Drag `microbit_challenge_generator.html` into upload area
9. Click "Commit changes"

**Option B: Use GitHub Desktop (Easier for Future Updates)**
1. Download [GitHub Desktop](https://desktop.github.com/)
2. File → New Repository
3. Name: `microbit-challenge-generator`
4. Choose local path
5. Click "Create Repository"
6. Copy `microbit_challenge_generator.html` and `README.md` into folder
7. Commit → Publish to GitHub

### 3. Enable GitHub Pages

1. Go to your repository on github.com
2. Click "Settings" tab (top right)
3. Scroll down to "Pages" in left sidebar
4. Under "Source":
   - Branch: `main` (or `master`)
   - Folder: `/ (root)`
5. Click "Save"
6. Wait 2-3 minutes

### 4. Access Your Live Site

Your site will be at:
```
https://YOUR-USERNAME.github.io/microbit-challenge-generator/
```

Example: `https://ruchaindyrise.github.io/microbit-challenge-generator/`

### 5. Update README with Live Link

1. Edit README.md on GitHub
2. Replace `yourusername` with your actual GitHub username
3. Commit changes

## Updating Your Site

### Method 1: Edit Directly on GitHub
1. Go to your repository
2. Click on `microbit_challenge_generator.html`
3. Click pencil icon (Edit)
4. Make changes
5. Scroll down → Commit changes
6. Wait 1-2 minutes for site to update

### Method 2: GitHub Desktop
1. Make changes to local file
2. Open GitHub Desktop
3. See changes listed
4. Write commit message
5. Click "Commit to main"
6. Click "Push origin"
7. Site updates in 1-2 minutes

## Custom Domain (Optional)

Want to use your own domain?

1. Buy domain (GoDaddy, Namecheap, etc.)
2. In domain settings, add CNAME record:
   - Host: `www` or `@`
   - Points to: `YOUR-USERNAME.github.io`
3. In GitHub repo Settings → Pages
   - Custom domain: `yourdomain.com`
   - ✅ Enforce HTTPS

## Troubleshooting

**404 Error?**
- Wait 5 minutes after enabling Pages
- Check branch is set to `main` or `master`
- Verify repository is public

**Changes not showing?**
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Wait 2-3 minutes after commit
- Check GitHub Actions tab for build status

**Mixed content errors?**
- Ensure all CDN links use `https://`
- Check browser console (F12) for specific errors

## Best Practices

1. **Always test locally first** (open HTML file in browser)
2. **Write clear commit messages** ("Fixed PDF export bug" not "update")
3. **Keep backups** (download HTML file periodically)
4. **Version your changes** (add version number to commits)

## Sharing Your Tool

Once published, share with:
- **Teachers**: Direct link to live site
- **Workshops**: Add to presentation slides
- **Portfolio**: Link from your teaching website
- **Social Media**: Tweet with #microbit #edtech

Example tweet:
```
Just published a free micro:bit challenge generator for teachers! 
60 standards-aligned challenges for grades 4-6. 
🔗 https://YOUR-USERNAME.github.io/microbit-challenge-generator/
#microbit #edtech #coding
```

## Need Help?

- GitHub Pages Docs: [docs.github.com/pages](https://docs.github.com/pages)
- Contact: rucha@indyri.se
