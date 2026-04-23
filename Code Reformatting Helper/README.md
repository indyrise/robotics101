# Code Highlighter for Handouts

A lightweight tool to highlight code with line numbers for printing student handouts.

## How to Use

1. **Open the file** — Double-click `code-highlighter.html` in your browser
2. **Paste your code** in the textarea
3. **Select the language** (C++, Python, JavaScript, etc.)
4. **Click "Generate Preview"** — syntax highlighting appears
5. **Print** — Cmd/Ctrl+P, save as PDF, or print directly

## What it Does

- Syntax highlighting using highlight.js (atom-one-light theme)
- Line numbers (small, gray, right-aligned)
- Clean white background for printing
- Works offline after first load

## Technical Notes

- Uses `hljs.highlight()` to generate colored HTML (not `highlightElement()`)
- Line numbers are added by splitting highlighted output into lines and wrapping each in a flex container
- Inline styles preserve highlighting through the splitting process
- CSS `@media print` hides editor, shows only preview

## Why This Works (The Hack)

The challenge was getting highlight.js to work with line numbers without losing syntax colors. Most approaches (plugins, CSS counters) interfere with highlight.js's color injection. 

**The solution:** 
1. Let highlight.js generate the full colored HTML
2. Split that HTML by newlines
3. Wrap each line in a flex container with a line number
4. This preserves all the color spans that highlight.js injected

## No Dependencies

- Pure HTML/CSS/JavaScript
- Highlight.js loaded via CDN
- Works in any modern browser