# 🎬 Looney Workspace

> "That's all folks... or is it?" - A feature-packed, Notion-like collaboration workspace with personality!

A completely self-contained, single-file web application that turns your browser into a powerful productivity hub inspired by Looney Tunes aesthetics.

## ✨ Features

### 🧮 Productivity Tools
- **Calculator** - Full-featured calculator with keyboard support
- **Markdown Notes** - Live markdown editor with preview mode
- **Todo List** - Task management with checkboxes and persistence
- **Pomodoro Timer** - Focus timer with customizable presets (5, 15, 25 minutes)

### 💻 Developer Tools
- **Code Playground** - Run JavaScript code in the browser with live output
- **JSON Formatter** - Format and minify JSON with error handling

### 🎨 Creative Tools
- **Drawing Canvas** - Freehand drawing with color picker and brush size
- **Color Picker** - Visual color selection with hex code copy

### 🔗 Utilities
- **Quick Links** - Customizable bookmark grid with popular sites pre-loaded
- **Weather Widget** - Weather display (demo/mockup)

## 🚀 Quick Start

1. **Open the file:**
   ```bash
   open looney-workspace.html
   ```
   Or just double-click the file!

2. **Add widgets** from the sidebar menu

3. **Start working!** All your data auto-saves to browser localStorage

## 🎯 Key Technologies

- **Pure HTML/CSS/JavaScript** - No dependencies, no build process
- **LocalStorage API** - Automatic workspace persistence
- **Canvas API** - Drawing functionality
- **Marked.js** - Markdown rendering
- **Highlight.js** - Code syntax highlighting
- **Font Awesome** - Beautiful icons
- **CSS Grid & Flexbox** - Responsive layout

## 🎨 Widget Library

| Widget | Description | Icon |
|--------|-------------|------|
| Calculator | Basic arithmetic with keyboard support | 🧮 |
| Notes | Markdown editor with live preview | 📝 |
| Todo List | Check off tasks, mark complete | ✅ |
| Code Playground | Execute JavaScript in browser | 💻 |
| Drawing Canvas | Freehand drawing with colors | 🎨 |
| Pomodoro Timer | Focus timer with presets | ⏱️ |
| Quick Links | Bookmarks grid | 🔗 |
| Weather | Weather display | 🌤️ |
| JSON Formatter | Format/minify JSON | 📋 |
| Color Picker | Visual color selection | 🎨 |

## 🔧 Usage

### Adding Widgets
Click any widget button in the sidebar to add it to your workspace. Multiple instances supported!

### Removing Widgets
Click the × button in the top-right corner of any widget.

### Saving
- **Auto-save**: Workspace saves automatically as you work
- **Manual save**: Press `Ctrl+S` (or `Cmd+S` on Mac)
- **Clear all**: Use "Clear All" button in topbar (with confirmation)

### Keyboard Shortcuts
- `Ctrl/Cmd + S` - Save workspace
- Calculator supports number keys, operators, Enter (=), Escape (clear)

## 💾 Data Persistence

All data is stored in your browser's localStorage:
- Widget layout and types
- Todo list items
- Notes content
- Code editor content
- Drawing canvas (not yet implemented, but coming soon!)

**Note**: Data is stored per-browser. Clearing browser data will reset the workspace.

## 🌟 Features in Detail

### Calculator Widget
- Basic operations: +, −, ×, ÷
- Decimal support
- Keyboard input
- Clear and backspace functions
- Error handling

### Notes Widget
- **Edit mode**: Plain text markdown editor
- **Preview mode**: Rendered markdown with formatting
- Auto-saves as you type
- Supports:
  - Headings
  - Bold/italic
  - Lists
  - Code blocks
  - Links

### Todo List
- Add tasks with Enter key
- Check/uncheck completion
- Delete individual tasks
- Visual strike-through for completed items
- Hover to show delete button

### Code Playground
- JavaScript execution in isolated environment
- Custom console.log capturing
- Error handling with friendly messages
- Language selector (JavaScript, Python, HTML, CSS - only JS executes)
- Clear and run buttons

### Drawing Canvas
- Color picker
- Adjustable brush size (1-20px)
- Smooth drawing with mouse
- Clear canvas button
- Save as PNG

### Pomodoro Timer
- Display in MM:SS format
- Start/Pause/Reset controls
- Quick presets: 5, 15, 25 minutes
- Alert when time is up

## 🎭 Design Philosophy

**Looney Tunes Aesthetic**: Playful, colorful, fun but functional
- Gradient backgrounds
- Smooth animations
- Bouncing icons
- Friendly error messages

**Single-File Architecture**: Everything in one HTML file for maximum portability

**Zero Dependencies (Core)**: Uses CDN for:
- Font Awesome (icons)
- Marked.js (markdown)
- Highlight.js (syntax highlighting)

**Progressive Enhancement**: Works offline after initial load (with CDN assets cached)

## 🚧 Future Enhancements

- [ ] Drag-and-drop widget repositioning
- [ ] Widget resizing
- [ ] Export/import workspace as JSON
- [ ] Real weather API integration
- [ ] Collaborative features (WebRTC)
- [ ] More widgets:
  - Spreadsheet
  - Mind map
  - Music player
  - RSS reader
  - Git client
  - Terminal emulator
- [ ] Dark mode toggle
- [ ] Custom themes
- [ ] Cloud sync (Firebase/Supabase)
- [ ] Mobile app (PWA)

## 🐛 Known Issues

- Drawing canvas doesn't persist between sessions (coming soon)
- Code playground only executes JavaScript
- Weather widget is demo data only
- No widget drag-and-drop yet

## 🤝 Contributing Ideas

This is a single-file app, but here are ways to extend it:

1. **Add new widgets**: Copy the widget template structure
2. **Improve existing widgets**: Enhance functionality
3. **Add themes**: Create color scheme variants
4. **Integrate APIs**: Weather, news, stocks, etc.

## 📝 Widget Development Guide

To add a new widget:

```javascript
// 1. Add to widgetTemplates object
widgetTemplates.myWidget = {
    title: '🎯 My Widget',
    content: `
        <div>Your HTML here</div>
    `
};

// 2. Add button in sidebar HTML
<button class="widget-button" onclick="addWidget('myWidget')">
    <i class="fas fa-icon"></i>
    <span>My Widget</span>
</button>

// 3. Add initialization logic if needed
function initializeWidget(type, id) {
    if (type === 'myWidget') {
        // Setup code here
    }
}
```

## 🎬 Credits

- **Inspired by**: Notion, Trello, Google Keep
- **Theme**: Looney Tunes (Warner Bros.)
- **Icons**: Font Awesome
- **Markdown**: Marked.js
- **Syntax Highlighting**: Highlight.js

## 📄 License

MIT - Do whatever you want with it!

---

**That's all folks!** 🎬

Made with ❤️ and a lot of ☕

*"Beep beep!"* - Road Runner