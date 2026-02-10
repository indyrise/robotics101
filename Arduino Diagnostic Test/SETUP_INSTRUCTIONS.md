# Adding the Arduino Diagnostic Test to robotics101

## Your new repo structure

```
robotics101/
├── arduino/
│   └── libraries/
│       └── Acebott/              # (existing)
├── tools/
│   └── arduino-diagnostic/       # ← NEW
│       ├── src/
│       │   ├── App.jsx
│       │   └── main.jsx
│       ├── index.html
│       ├── package.json
│       ├── vite.config.js
│       └── README.md
└── README.md                     # ← UPDATED
```

## Steps

### 1. Clone your repo (if you haven't already)

```bash
git clone https://github.com/indyrise/robotics101.git
cd robotics101
```

### 2. Copy the `tools/` folder into your repo

Download the files I created and place the entire `tools/` folder
at the root of your repo, next to the existing `arduino/` folder.

### 3. Verify it runs

```bash
cd tools/arduino-diagnostic
npm install
npm run dev
```

Visit http://localhost:5173 — you should see the exam start screen.

### 4. Commit and push

```bash
cd ../..
git add .
git commit -m "Add Arduino certification diagnostic test"
git push
```

### 5. (Optional) Deploy to GitHub Pages

To make the test accessible at a URL like
`https://indyrise.github.io/robotics101/tools/arduino-diagnostic/`:

1. Go to your repo → Settings → Pages
2. Under "Build and deployment", set Source to **GitHub Actions**
3. Create `.github/workflows/deploy.yml` with this content:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Build diagnostic app
        run: |
          cd tools/arduino-diagnostic
          npm install
          npm run build

      - name: Prepare pages
        run: |
          mkdir -p _site/tools/arduino-diagnostic
          cp -r tools/arduino-diagnostic/dist/* _site/tools/arduino-diagnostic/

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3

  deploy:
    needs: build-and-deploy
    runs-on: ubuntu-latest
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
    steps:
      - uses: actions/deploy-pages@v4
```

4. Commit and push. The test will be live within a couple minutes.
