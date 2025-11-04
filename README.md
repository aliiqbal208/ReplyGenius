# 🚀 ReplyGenius

A privacy-focused Chrome extension that helps you generate professional AI-powered comments for LinkedIn posts.

## ✨ Features

### 🎨 **37+ Customizable Tones**
Choose from 8 categories to match your style:
- **Professional** (4): Professional, Formal, Corporate, Authoritative
- **Friendly & Social** (4): Friendly, Casual, Conversational, Warm
- **Supportive & Positive** (5): Supportive, Encouraging, Cheerful, Enthusiastic, Optimistic
- **Analytical & Thoughtful** (5): Inquisitive, Analytical, Thoughtful, Insightful, Critical
- **Creative & Engaging** (5): Funny, Witty, Creative, Inspirational, Motivational
- **Empathetic & Understanding** (3): Empathetic, Sympathetic, Respectful
- **Direct & Clear** (3): Concise, Straightforward, Assertive
- **Specialized** (5): Educational, Diplomatic, Humble, Grateful, Curious

### 🤖 **24+ AI Models**
Support for multiple AI providers:
- **OpenAI**: GPT-4.1, GPT-4o, O1, O3-Mini, O4-Mini, GPT-3.5 Turbo
- **Anthropic**: Claude 3 Opus, Sonnet, Haiku, Claude 3.5 Sonnet
- **Google**: Gemini Pro, Gemini 1.5 Pro, Gemini 1.5 Flash
- **Meta**: Llama 3.1 (70B, 8B), Llama 3.2 90B
- **Mistral**: Large, Medium, Small

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

### From Chrome Web Store (Coming Soon)
Will be available in the Chrome Web Store once published.

### Manual Installation
1. Download or clone this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable **Developer mode** (toggle in top right)
4. Click **Load unpacked**
5. Select the extension directory
6. Navigate to LinkedIn and start using!

---

## 🎯 How to Use

### On LinkedIn Feed:
1. **Find a post** you want to comment on
2. **Click "✨ Generate Comment"** button on the post
3. **Choose your tone** (37 options available)
4. **Select AI model** (24+ models to choose from)
5. **(Optional)** Add hints to guide the response
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
- ✅ Sends **anonymous user data** (not your real identity)
- ✅ Your name, email, and profile are protected
- ✅ Only post content is shared (required for AI)
- ✅ No tracking or user profiling

### What Gets Sent to API:
- LinkedIn post content (needed for AI to understand context)
- Your optional hints (if you provide them)
- Selected tone and model
- Anonymous user data (dummy information)

### What Does NOT Get Sent:
- ❌ Your real LinkedIn profile URL
- ❌ Your real name
- ❌ Your real email address
- ❌ Your LinkedIn ID

### Security Status:
- ✅ Privacy Mode: **ACTIVE**
- ✅ Anonymous Data: **ENABLED**
- ✅ HTTPS Encryption: **ENABLED**
- ⚠️ Recommended: Apply additional security fixes (see SECURITY_FIXES.md)

---

## ⚙️ Configuration

### API Endpoint
The extension uses a pre-configured n8n webhook endpoint. To use your own:

1. Edit `content.js`
2. Find `API_CONFIG` object (around line 126)
3. Update the `URL` property:
```javascript
const API_CONFIG = {
    URL: 'https://your-api-endpoint.com/webhook',
    MAX_RETRIES: 2,
    TIMEOUT_MS: 10000
};
```

### API Requirements:
Your endpoint should accept POST requests with:
```json
{
  "caption": "post content",
  "hint": "optional hint",
  "tone": "professional",
  "model": "gpt-4.1-nano"
}
```

And return:
```json
{
  "comment": "generated comment text"
}
```

---

## 🛠️ Development

### Project Structure
```
linkedin-comment/
├── manifest.json       # Extension configuration
├── content.js         # Main logic (LinkedIn integration)
├── background.js      # Service worker
├── popup.html/js      # Extension popup UI
├── icons/            # Extension icons
└── README.md         # This file
```

### Debug Mode
- Press **Ctrl+Shift+D** on LinkedIn to enable debug mode
- Open Chrome DevTools (F12) to see console logs
- Check Network tab to monitor API calls

### Testing
1. Make code changes
2. Go to `chrome://extensions/`
3. Click reload icon on the extension
4. Test on LinkedIn feed
5. Check console for errors

---

## 📋 Requirements

- Chrome browser (v88+)
- Active internet connection
- LinkedIn account
- Access to API endpoint (default provided)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new tones or AI models
- Improve privacy features
- Fix bugs or add features
- Submit pull requests

---

## ⚠️ Important Notes

### For Users:
- Always review and personalize AI-generated comments
- Use appropriate tones for different contexts
- Don't rely solely on AI - add your own perspective
- Be authentic in your LinkedIn engagement

### For Developers:
- This extension requires an API endpoint
- Default endpoint is pre-configured (n8n webhook)
- Privacy mode sends anonymous data by default
- Extension works on `linkedin.com` only

---

## 🐛 Troubleshooting

### Extension not working?
1. Check if you're on `linkedin.com`
2. Reload the extension in `chrome://extensions/`
3. Check browser console for errors (F12)
4. Verify internet connection

### No "Generate Comment" button?
1. Refresh the LinkedIn page
2. Check if the post is commentable
3. Enable debug mode (Ctrl+Shift+D)

### API errors?
1. Check network connection
2. Verify API endpoint is accessible
3. Check browser console for error details

---

## 📄 License

MIT License - Feel free to use and modify

---

## 🙏 Acknowledgments

- Powered by multiple AI providers (OpenAI, Anthropic, Google, Meta, Mistral)
- Built with privacy and security in mind
- Community-driven development

---

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Version:** 1.2  
**Status:** ✅ Active  
**Privacy:** 🔒 Protected  
**Last Updated:** November 4, 2025 