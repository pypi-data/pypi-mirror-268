from pathlib import Path

from setuptools import setup


DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="webchatgpt",
    version="0.3.0",
    license="GNU v3",
    author="Smartwa",
    maintainer="Smartwa",
    author_email="simatwacaleb@proton.me",
    description="Reverse Engineering of ChatGPT Web-Version",
    packages=["WebChatGPT"],
    url="https://github.com/Simatwa/WebChatGPT",
    project_urls={
        "Bug Report": "https://github.com/Simatwa/WebChatGPT/issues/new",
        "Homepage": "https://github.com/Simatwa/WebChatGPT",
        "Source Code": "https://github.com/Simatwa/WebChatGPT",
        "Issue Tracker": "https://github.com/Simatwa/WebChatGPT/issues",
        "Download": "https://github.com/Simatwa/WebChatGPT/releases",
        "Documentation": "https://github.com/Simatwa/WebChatGPT/blob/main/docs/README.md",
    },
    entry_points={
        "console_scripts": [
            "webchatgpt = WebChatGPT.console:main",
            "wbc = WebChatGPT.console:main",
        ],
    },
    install_requires=[
        "requests==2.31.0",
        "python-dotenv==1.0.0",
        "click==8.1.3",
        "rich==13.3.4",
        "clipman==3.1.0",
        "pyperclip==1.8.2",
    ],
    python_requires=">=3.10",
    keywords=[
        "chatgpt",
        "webchatgpt",
        "gpt",
        "chatgpt-cli",
        "chatgpt-sdk",
        "chatgpt-api",
    ],
    long_description=Path.open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Free For Home Use",
        "Intended Audience :: Customer Service",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
