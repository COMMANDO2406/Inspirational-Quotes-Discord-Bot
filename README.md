# Inspirational-Quotes-Bot
quick install:
```python
pip install -r requirements.txt
```
# Examples
![image](https://github.com/user-attachments/assets/86241e82-03e1-4aff-b2d5-52749d6e2710)


## Todo
  - update docs in [usage.md](Docs/usage.md)
  - create documentation for code
  - create tests

# Structure:
```
Inspirational-Quotes-Bot/
├── requirements.txt                          # Lists Python dependencies
├── setup.py                                  # Setup for python dependencies
├── Background-Images/                        # Folder for background images
│   └── ...
├── quotes/                                   # Folder for inspirational quotes
│   ├── inspirational_from_quotable.json      # File of quotes
│   ├── populate_quotes.py                    # Fetches quotes from JSON file
│   └── ... (one file per source)
├── src/
│   ├── __init__.py    
│   ├── bot.py                                # Script for discord bot
|   ├── config.py                             # Set password for discord bot
│   └── image_gen.py                          # Main script for the inspirational quotes
├── docs/
│   └── usage.md                              # Documentation for using the bot (to write)
├── tests/
│   └── test_sample.py                        # Test sample
├── fonts/
│   └── JetBrainsMonoNerdFont-Medium.ttf      # Font for quotes
├── outputs/                                  # Sample output
│   └── Output.png                            # Image of sample output
└── web/                                      # Code for the web version (to implement)
```

# Credit
https://www.pexels.com/search/quote%20background%20blank/?orientation=landscape
