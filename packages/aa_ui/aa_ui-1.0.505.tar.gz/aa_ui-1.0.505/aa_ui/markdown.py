import os

from aa_ui.logger import logger

# Default aa_ui.md file created if none exists
DEFAULT_MARKDOWN_STR = """# Welcome to aa_ui! 🚀🤖

Hi there, Developer! 👋 We're excited to have you on board. aa_ui is a powerful tool designed to help you prototype, debug and share applications built on top of LLMs.

## Useful Links 🔗

- **Documentation:** Get started with our comprehensive [aa_ui Documentation](https://docs.aa_ui.io) 📚
- **Discord Community:** Join our friendly [aa_ui Discord](https://discord.gg/k73SQ3FyUh) to ask questions, share your projects, and connect with other developers! 💬

We can't wait to see what you create with aa_ui! Happy coding! 💻😊

## Welcome screen

To modify the welcome screen, edit the `aa_ui.md` file at the root of your project. If you do not want a welcome screen, just leave this file empty.
"""


def init_markdown(root: str):
    """Initialize the aa_ui.md file if it doesn't exist."""
    aa_ui_md_file = os.path.join(root, "aa_ui.md")

    if not os.path.exists(aa_ui_md_file):
        with open(aa_ui_md_file, "w", encoding="utf-8") as f:
            f.write(DEFAULT_MARKDOWN_STR)
            logger.info(f"Created default aa_ui markdown file at {aa_ui_md_file}")


def get_markdown_str(root: str, language: str):
    """Get the aa_ui.md file as a string."""
    translated_aa_ui_md_path = os.path.join(root, f"aa_ui_{language}.md")
    default_aa_ui_md_path = os.path.join(root, "aa_ui.md")

    if os.path.exists(translated_aa_ui_md_path):
        aa_ui_md_path = translated_aa_ui_md_path
    else:
        aa_ui_md_path = default_aa_ui_md_path
        logger.warning(
            f"Translated markdown file for {language} not found. Defaulting to aa_ui.md."
        )

    if os.path.exists(aa_ui_md_path):
        with open(aa_ui_md_path, "r", encoding="utf-8") as f:
            aa_ui_md = f.read()
            return aa_ui_md
    else:
        return None
