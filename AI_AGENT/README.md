# EMAIL AI AGENT
###### _

I wanted experiment with different LLM's that my computer can take. 

This project uses the Ollama - qwen3:8b model to interpret emails and do certain tasks like read emails, and categorize them. I plan to also add a web-based GUI using react

### Connect Agent to E-Mail Inbox

To connect the AI AGENT to an email (in this case, I used a gmail account, but anything like yahoo etc. goes) inbox list just 
- Enable IMAP on your gmail account
- Create a Google App Password
- Create a local `.env` file
- Input gmail account and Google App Password as follows

```.env
IMAP_HOST=imap.gmail.com
IMAP_PORT=993
IMAP_USER='[gmail account]'
IMAP_PASSWORD='[gmail app password]'
```

### To run this program:

``` Windows Powershel 
$ cd AI_AGENT
$ uv install
$ uv run main.py
```

