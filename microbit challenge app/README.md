# micro:bit Challenge Generator

**A free web tool for teachers to generate standards-aligned micro:bit coding challenges for grades 4-6.**

🔗 **[Live Demo](https://yourusername.github.io/microbit-challenge-generator/)** *(update after deploying)*

![Screenshot](screenshot.png)

## Overview

The micro:bit Challenge Generator helps teachers create customized coding challenges for elementary and middle school students. With 60 built-in templates spanning beginner to advanced difficulty, it generates random, standards-aligned challenges in seconds.

**Perfect for:**
- Quick pre-class prep (generate 1-3 challenges in under 30 seconds)
- Differentiation (beginner vs experienced, grade 4/5/6)
- Remote teaching (download as PDFs or slides)
- Maker spaces and coding clubs

## Features

### ✨ Core Features
- **60 Challenge Templates** - Beginner (13), Intermediate (20), Advanced (15)
- **Grade-Level Adaptation** - Automatically adjusts for 4th, 5th, or 6th grade
- **Experience Levels** - Beginner and experienced options
- **Standards-Aligned** - Automatic CSTA and NGSS K-8 standards mapping
- **Random Shuffling** - Get different challenges with same settings
- **Offline Capable** - Works without internet after first load

### 📥 Export Formats
- **TXT** - Plain text for copying anywhere
- **PDF (3x5)** - Print on 3x5 index cards
- **PDF (4x6)** - Print on 4x6 index cards  
- **Google Slides/PowerPoint** - Import into presentations

### 📖 Teacher Tools
- **Tutorial Reference** - CSV mapping challenges to MakeCode tutorials
- **Copy Prompt Feature** - Save your settings for quick regeneration
- **Start Fresh Button** - Reset when things break

### 🎓 Concepts Covered
**Beginner:** Inputs, display, sensors, variables, loops, conditionals, random, time  
**Intermediate:** Arrays, strings, radio (2-5 micro:bits), data logging, math, multi-player games  
**Advanced:** State machines, algorithms, machine learning basics, networking, protocols, distributed computing

## Quick Start

### Option 1: Use Online (Easiest)
1. Visit the [live demo](https://yourusername.github.io/microbit-challenge-generator/)
2. Select grade level and experience
3. Click "Generate Challenges"
4. Download in your preferred format

### Option 2: Download and Run Locally
1. Download `microbit_challenge_generator.html`
2. Double-click to open in any web browser
3. Works offline after first load
4. No installation required

### Option 3: Fork and Customize
1. Fork this repository
2. Edit `microbit_challenge_generator.html` to add your own challenges
3. Deploy to GitHub Pages (see below)

## Challenge Library

60 templates across three difficulty levels covering core CS concepts and advanced topics.

**View full library breakdown in the app** or see detailed list in [CHALLENGES.md](CHALLENGES.md)

## Standards Alignment

All challenges are mapped to:
- **CSTA** (Computer Science Teachers Association) K-8
- **NGSS** (Next Generation Science Standards) 3-8

Standards codes appear at the bottom of each generated challenge.

## GitHub Pages Deployment

### First Time Setup

1. **Fork this repository**
2. **Enable GitHub Pages**
   - Settings → Pages
   - Source: Deploy from branch  
   - Branch: `main`, Folder: `/`
3. **Access your site**
   - `https://yourusername.github.io/microbit-challenge-generator/`

### Updating Content

Edit `microbit_challenge_generator.html` → Auto-deploys in 1-2 minutes

## Customization

Add your own challenges by editing the `challengeLibrary` array. See [CONTRIBUTING.md](CONTRIBUTING.md) for format details.

## Technical Details

- **Single File**: One HTML file, no build process
- **Client-Side**: No server required
- **Dependencies**: jsPDF, PizZip, Docxtemplater (via CDN)
- **Size**: ~150KB

## Limitations

**Current Version (Free):**
- 60 templates (template-based, not AI-generated)
- Core micro:bit features only (no external components)
- 1-5 micro:bits maximum

**Premium Version (Coming Soon):**
Join waitlist: **rucha@indyri.se**

## Troubleshooting

**Generate button stops working?** → Click "Start Fresh"  
**Want more than 3 challenges?** → Generate multiple batches and combine

## License

MIT License - Free to use, modify, and distribute.

## About

Created by Rucha for the teaching community.

**Contact:** rucha@indyri.se  
**Portfolio:** [indyri.se](https://indyri.se)

---

*Part of the Robotics 101 portfolio*
