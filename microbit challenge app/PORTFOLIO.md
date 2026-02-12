# Project: micro:bit Challenge Generator

**For: Robotics 101 Portfolio**

## Project Overview

A free, browser-based tool that generates standards-aligned micro:bit coding challenges for elementary and middle school teachers. Built to solve the problem of time-consuming lesson planning while maintaining high-quality, differentiated instruction.

## Problem Statement

Teachers spend 5-15 minutes per class session finding or creating appropriate micro:bit challenges that:
- Match student skill levels (beginner vs experienced)
- Align with grade-appropriate standards (CSTA, NGSS)
- Offer differentiation pathways
- Include clear learning objectives and extension activities

Existing solutions either lack standards alignment, offer generic "one-size-fits-all" challenges, or require paid subscriptions.

## Solution

A single-file web application that:
1. Generates 1-3 random challenges from a library of 60 templates
2. Automatically maps to CSTA and NGSS standards
3. Exports to multiple formats (TXT, PDF, Google Slides)
4. Works offline after initial load
5. Requires zero installation or technical setup

## Technical Implementation

### Stack
- **Frontend**: Pure HTML/CSS/JavaScript (no frameworks)
- **Libraries**: jsPDF (PDF generation), PizZip + Docxtemplater (PPTX)
- **Deployment**: GitHub Pages (static hosting)
- **File Size**: 150KB (fast load on school networks)

### Architecture Decisions

**Why single-file HTML?**
- Teachers can download and run offline
- No npm, build process, or dependencies to manage
- Easy to fork and customize
- Fast deployment (drag & drop to GitHub)

**Why template-based vs AI-generated?**
- Consistent quality and standards alignment
- No API costs or rate limits
- Instant generation (no waiting for LLM)
- Works offline
- Predictable, teacher-vetted content

**Why 60 templates?**
- Balances variety with maintainability
- Covers full curriculum scope (beginner → advanced)
- Low enough duplication risk for typical classroom use
- Expansion path to premium tier (100+)

### Key Features

**Challenge Library (60 templates)**
- Beginner: 13 challenges (inputs, display, sensors)
- Intermediate: 20 challenges (arrays, radio, algorithms)
- Advanced: 15 challenges (ML, networking, distributed systems)

**Smart Filtering**
- Grade level (4th, 5th, 6th)
- Experience level (beginner, experienced)
- Concept detection (keywords → relevant templates)

**Export Formats**
- TXT (copy-paste anywhere)
- PDF 3x5 / 4x6 (print on index cards)
- Google Slides / PowerPoint (import and customize)

**Standards Alignment**
- CSTA K-8 (Computer Science Teachers Association)
- NGSS 3-8 (Next Generation Science Standards)
- Auto-generated based on challenge concepts

**Teacher UX**
- "Copy Prompt" button → saves settings
- "Start Fresh" button → reset on errors
- Helpful tips for iteration workflow
- Tutorial reference CSV (links to MakeCode lessons)

## Impact & Use Cases

**Target Users:**
- Elementary/middle school CS teachers
- Coding club facilitators
- Maker space coordinators
- Homeschool parents

**Usage Scenarios:**
1. **Quick prep**: Generate 3 challenges before class (30 seconds)
2. **Differentiation**: Generate beginner + experienced versions
3. **Remote teaching**: Export as PDFs for at-home activities
4. **Physical materials**: Print on index cards for maker spaces

**Potential Reach:**
- Shareable via single URL (no account required)
- Free forever (no premium features required for basic use)
- Open source (teachers can fork and customize)

## Business Model

**Free Tier (Current)**
- 60 templates
- Core micro:bit features only
- All export formats
- Standards alignment

**Premium Tier (Roadmap)**
- 100+ templates with external components
- LLM-powered custom generation
- Scaffolded unit plans
- Assessment rubrics
- Contact: rucha@indyri.se

## Challenges & Learnings

### Technical Challenges

**Problem**: Generate button broke after first use  
**Cause**: JavaScript error from old/new code mixing during iterative edits  
**Solution**: Complete function rewrite + error handling try-catch blocks  
**Learning**: Single-file apps need extra care during incremental development

**Problem**: Users wanted different challenges with same prompt  
**Cause**: Template selection was deterministic (same keywords → same order)  
**Solution**: Fisher-Yates shuffle algorithm before selection  
**Learning**: Randomization UX > deterministic (even when templates are finite)

**Problem**: Teachers frustrated when tool broke mid-session  
**Cause**: No graceful degradation or recovery path  
**Solution**: "Start Fresh" button + "Copy Prompt" workflow  
**Learning**: Always provide escape hatches in educational tools

### Design Challenges

**Problem**: Template library size (12 vs 60 vs 100+ vs LLM)  
**Decision**: 60 templates as sweet spot  
**Rationale**:
- 12 too small (repetition issues)
- 100+ maintenance nightmare
- LLM requires API costs + complexity
- 60 balances variety, quality, maintenance

**Problem**: Export format preferences vary widely  
**Decision**: Support all common formats (TXT, PDF, PPTX)  
**Rationale**: Teachers use diverse workflows (Google Classroom, Canvas, Notion, physical printouts)

**Problem**: How to communicate limitations (template-based, not AI)  
**Decision**: FAQ section + premium CTA  
**Rationale**: Set expectations while showing upgrade path

## Future Enhancements

### V2 - Python Power User Version
- Local SQLite database (persistent challenge library)
- Custom challenge CRUD (create, edit, delete)
- True LLM integration (Claude API for custom generation)
- Advanced batch operations
- Export/import challenge sets

### Premium Library
- External components (motors, servos, sensors)
- Cross-curricular challenges (math, science, art)
- Full unit plans with learning objectives
- Assessment rubrics and student handouts

### Community Features
- Share custom challenges via URL
- Teacher-contributed challenge marketplace
- Voting/rating system
- Challenge remix/modification

## Portfolio Highlights

**Why This Project Matters**

1. **Solves Real Problem**: Teachers lack time for quality lesson planning
2. **Accessible**: Free, no signup, works offline, zero installation
3. **Standards-Aligned**: Automatic CSTA/NGSS mapping (time-saver)
4. **Scalable**: Single URL serves unlimited teachers
5. **Open Source**: Forkable, customizable, community-driven

**Skills Demonstrated**

- **Full-stack Web Development**: HTML/CSS/JavaScript
- **User-Centered Design**: Teacher workflows, export formats, error recovery
- **Product Strategy**: Free tier + premium roadmap
- **Technical Writing**: Comprehensive README, deployment guide
- **Standards Knowledge**: CSTA, NGSS curriculum mapping
- **Educational Technology**: Pedagogical understanding of differentiation

**Code Quality**

- Single-file architecture (deployable anywhere)
- Comprehensive error handling
- Offline-first design
- Clean, commented JavaScript
- Accessibility considerations

## Links

- **Live Demo**: [GitHub Pages URL - update after deploy]
- **Source Code**: [GitHub Repository URL]
- **Contact**: rucha@indyri.se
- **Portfolio**: indyri.se

## Reflection

This project evolved from a simple random challenge generator to a comprehensive teacher tool through iterative user feedback. Key insights:

1. **Teachers value speed over infinite variety** - 60 well-designed templates beats LLM-generated content for daily use
2. **Escape hatches matter** - "Start Fresh" and "Copy Prompt" saved the UX when technical issues arose
3. **Format flexibility is critical** - Supporting TXT/PDF/PPTX accommodates diverse teacher workflows
4. **Standards alignment is table stakes** - Auto-mapping to CSTA/NGSS transforms from nice-to-have to must-have

Future development will focus on V2 (Python power-user version) with persistent storage, LLM integration, and community features while maintaining the simplicity of V1 for casual users.

---

**Created by Rucha | Robotics 101 Portfolio | 2026**
