# 🚀 ReplyGenius

A privacy-focused Chrome extension that helps you generate professional AI-powered comments for LinkedIn posts.

## 🎯 Quick Start

```bash
# 1. Clone the repository
git clone <repository-url>
cd linkedin-comment

# 2. Configure your OpenAI API key
cp config.example.js config.js
# Edit config.js and add your API key from https://platform.openai.com/api-keys

# 3. Load in Chrome
# Go to chrome://extensions/ → Enable Developer Mode → Load Unpacked → Select folder

# 4. Use on LinkedIn!
# Visit linkedin.com and click "✨ Generate Comment" on any post
```

**Need an API key?** Get one free at [OpenAI Platform](https://platform.openai.com/api-keys)

---

## ✨ Features

### 🎨 **21 Focused Tones**
Choose from 7 categories designed for professional LinkedIn engagement:
- **Professional** (3): Professional, Formal, Authoritative
- **Friendly** (3): Friendly, Casual, Conversational
- **Supportive** (2): Supportive, Encouraging
- **Analytical** (5): Inquisitive, Analytical, Thoughtful, Insightful, Suggestive
- **Engaging** (3): Witty, Creative, Inspirational
- **Direct** (2): Concise, Straightforward
- **Respectful** (3): Respectful, Diplomatic, Curious

### 🤖 **OpenAI Models**
Powered by OpenAI's latest models:
- **GPT-4 Turbo**: Most capable, best for complex responses
- **GPT-4o**: Optimized for speed and quality
- **GPT-4o Mini**: Fast and efficient, great for most use cases
- **GPT-4**: Original flagship model
- **GPT-3.5 Turbo**: Quick and cost-effective

### 🔒 **Privacy-First Design**
- Sends anonymous/dummy user data (your identity is protected)
- Only shares post content (required for AI)
- No tracking or profiling

### 💡 **Easy to Use**
- Automatically detects LinkedIn posts
- "✨ Generate Comment" button on every post
- One-click copy to clipboard
- Optional hints for customization
- Debug mode (Ctrl+Shift+D)

---

## 📥 Installation

### Prerequisites
- Chrome browser (or Chromium-based browser)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Manual Installation

1. **Clone or Download**
   ```bash
   git clone <repository-url>
   cd linkedin-comment
   ```

2. **Configure API Key**
   ```bash
   # Copy the example config file
   cp config.example.js config.js
   
   # Edit config.js and add your OpenAI API key
   # Replace 'sk-your-openai-api-key-here' with your actual key
   ```

3. **Install Extension in Chrome**
   - Open Chrome and go to `chrome://extensions/`
   - Enable **Developer mode** (toggle in top right)
   - Click **Load unpacked**
   - Select the `linkedin-comment` directory
   - Extension installed! ✅

4. **Start Using**
   - Navigate to [LinkedIn](https://linkedin.com)
   - Find any post and click "✨ Generate Comment"
   - Choose your tone and generate!

### From Chrome Web Store (Coming Soon)
Will be available in the Chrome Web Store once published.

---

## 🎯 How to Use

### On LinkedIn Feed:
1. **Find a post** you want to comment on
2. **Click "✨ Generate Comment"** button on the post
3. **Choose your tone** (21 focused options available)
4. **AI auto-selects best OpenAI model** for that tone
5. **(Optional)** Manually select different OpenAI model
6. **Click "Generate"** and wait for AI magic ✨
7. **Copy** the generated comment
8. **Paste** into LinkedIn's comment box
9. **Edit** as needed and post!

### Tips for Best Results:
- Match the tone to your relationship with the post author
- Use hints to add specific context or perspectives
- Try different models to find your preferred style
- Always review and personalize before posting

---

## 🔒 Privacy & Security

### Privacy Mode (Built-in)
Your extension is configured with **privacy-first defaults**:
- ✅ Only sends post content to OpenAI (required for AI)
- ✅ Your LinkedIn profile data stays private
- ✅ No tracking or user profiling
- ✅ Direct API calls to OpenAI (no third-party servers)

### What Gets Sent to OpenAI:
- LinkedIn post content (needed for context)
- Your selected tone and model
- Your optional hints (if provided)

### What Does NOT Get Sent:
- ❌ Your real LinkedIn profile URL
- ❌ Your real name
- ❌ Your real email address
- ❌ Your LinkedIn ID

### Security Status:
- ✅ Privacy Mode: **ACTIVE**
- ✅ Direct OpenAI API: **ENABLED**
- ✅ HTTPS Encryption: **ENABLED**
- ⚠️ Keep your API key secure (don't share publicly)

---

## ⚙️ Configuration

### OpenAI API Key Setup

**Important:** You must configure your OpenAI API key before using the extension.

#### Step 1: Get Your API Key
- Visit [OpenAI Platform](https://platform.openai.com/api-keys)
- Sign in or create an account
- Click "Create new secret key"
- Copy your API key (starts with `sk-proj-...` or `sk-...`)

#### Step 2: Configure the Extension
```bash
# In the extension directory
cp config.example.js config.js
```

Then edit `config.js`:
```javascript
const CONFIG = {
  OPENAI_API_KEY: 'sk-proj-your-actual-api-key-here'  // ← Paste your key here
};
```

#### Step 3: Load/Reload Extension
- Open Chrome: `chrome://extensions/`
- Click the reload icon (🔄) on ReplyGenius
- ✅ Extension ready!

### Security Notes
- `config.js` is git-ignored (never committed)
- Keep your API key private
- Never share `config.js` publicly
- Use `config.example.js` as a template for others

### API Requirements
- ✅ Valid OpenAI API key with available credits
- ✅ Internet connection for API calls
- ✅ Access to OpenAI models (GPT-4, GPT-3.5, etc.)

---

## 🛠️ Development

### Project Structure
```
linkedin-comment/
├── manifest.json       # Extension configuration
├── content.js         # Main logic (LinkedIn integration)
├── background.js      # Service worker
├── popup.html/js      # Extension popup UI
## 🛠️ Development

### Project Structure
```
linkedin-comment/
├── manifest.json       # Extension configuration
├── content.js         # Main logic & LinkedIn integration
├── background.js      # Service worker
├── popup.html/js      # Extension popup UI
├── config.example.js  # Config template (committed to git)
├── config.js          # Your API key (git-ignored, create this!)
├── .gitignore         # Ignores config.js for security
├── icons/            # Extension icons
└── README.md         # Documentation
```

### First Time Setup for Developers
```bash
# Clone the repository
git clone <repo-url>
cd linkedin-comment

# Create your config file
cp config.example.js config.js

# Add your OpenAI API key to config.js
# Then load the extension in Chrome
```

### Debug Mode
- Press **Ctrl+Shift+D** on LinkedIn to toggle debug mode
- Open Chrome DevTools (F12) to see detailed logs
- Check Network tab to monitor OpenAI API calls
- Console shows request/response details

### Testing
1. Make code changes
2. Go to `chrome://extensions/`
3. Click reload (🔄) icon on ReplyGenius
4. Test on LinkedIn feed
5. Check browser console for errors

### Environment Files
- **`config.example.js`**: Template file (committed to git)
- **`config.js`**: Your actual API key (git-ignored, never commit this!)

---

## 📋 Requirements

- Chrome browser (v88+) or Chromium-based browser
- Active internet connection
- **OpenAI API key with credits** ([Get one here](https://platform.openai.com/api-keys))
- LinkedIn account

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Setup for Contributors
```bash
# Fork and clone the repo
git clone <your-fork-url>
cd linkedin-comment

# Create your config file (not tracked by git)
cp config.example.js config.js

# Add your OpenAI API key to config.js
# Load extension in Chrome and test your changes
```

### Adding New Features
1. **New Tones:** Edit `TONE_CONFIG` in `content.js`
2. **New Models:** Edit `GPT_MODELS` in `content.js` (OpenAI only)
3. Test thoroughly on LinkedIn
4. Submit a pull request

### Code Guidelines
- Keep API key in `config.js` (never hardcode)
- Maintain privacy-first approach
- Test with different post types
- Document significant changes

---

## ⚠️ Important Notes

### For Users:
- ✅ Always review and personalize AI-generated comments
- ✅ Use appropriate tones for different contexts
- ✅ Add your own perspective and authenticity
- ⚠️ **Never share your `config.js` file or API key**

### For Developers:
- 🔑 Extension requires OpenAI API key in `config.js`
- 🌐 API calls made directly to OpenAI (no intermediary)
- 🔒 Privacy mode: only post content sent to AI
- 📍 Extension works on `linkedin.com` only
- 🚫 `config.js` is git-ignored for security

---

## 🐛 Troubleshooting

### Extension not working?
1. ✅ Verify you're on `linkedin.com`
2. ✅ Check `config.js` exists with your API key
3. ✅ Reload extension: `chrome://extensions/` → click 🔄
4. ✅ Open console (F12) to check for errors
5. ✅ Verify internet connection

### No "Generate Comment" button?
1. Refresh the LinkedIn page (Ctrl+R / Cmd+R)
2. Check if the post allows comments
3. Enable debug mode (Ctrl+Shift+D) to see logs
4. Try scrolling - buttons appear as posts load

### API Errors?
1. **"Please configure your OpenAI API key"**
   - Copy `config.example.js` to `config.js`
   - Add your API key to `config.js`
   - Reload extension

2. **401 Unauthorized**
   - API key is invalid or expired
   - Get new key from [OpenAI Platform](https://platform.openai.com/api-keys)

3. **429 Rate Limit**
   - Out of API credits or hitting rate limits
   - Check usage at [OpenAI Platform](https://platform.openai.com/usage)

4. **Network errors**
4. **Network errors**
   - Check internet connection
   - Verify OpenAI services are up
   - Try again in a few moments

### Still having issues?
- Enable debug mode: Press **Ctrl+Shift+D** on LinkedIn
- Open browser console (F12) for detailed error logs
- Check the Network tab for failed API requests

---

## 📄 License

MIT License - Feel free to use and modify

---

## 🙏 Acknowledgments

- Powered by [OpenAI's GPT models](https://openai.com)
- Built with privacy and security in mind
- Community-driven development

---

## 📞 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check the [Troubleshooting](#-troubleshooting) section
- Enable debug mode for detailed logs

---

## 📦 Quick Start Checklist

- [ ] Clone repository
- [ ] Copy `config.example.js` to `config.js`
- [ ] Add OpenAI API key to `config.js`
- [ ] Load extension in Chrome (`chrome://extensions/`)
- [ ] Visit LinkedIn and test on a post
- [ ] Generate your first AI comment! 🎉

---

**Version:** 1.2  
**Status:** ✅ Active Development  
**Privacy:** 🔒 API Key Protected  
**Last Updated:** November 18, 2025 