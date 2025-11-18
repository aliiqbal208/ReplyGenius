// Configuration file for ReplyGenius
// Copy this file to config.js and add your actual API key

const CONFIG = {
  OPENAI_API_KEY: 'sk-your-openai-api-key-here'
};

// Export for use in extension
if (typeof module !== 'undefined' && module.exports) {
  module.exports = CONFIG;
}
