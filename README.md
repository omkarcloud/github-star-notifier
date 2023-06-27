# GitHub Star Notifier

The GitHub Star Notifier is a Python module that checks for new stars in specified repositories on GitHub and sends notifications via Telegram when someone stars a repository. It utilizes the GitHub API to retrieve star information and the Telegram Bot API for sending messages.

## Features

- Monitors specified repositories for new stars.
- Sends Telegram notifications with someone stars a repository.
- Configurable to monitor multiple repositories simultaneously.
- Runs at a regular interval (every 1 minute by default) to check for new stars.

## Installation


Clone this repository

```bash
git clone https://github.com/omkarcloud/bose-starter my-bose-project
```

Then change into that directory, install dependencies and open vscode:

```bash
cd my-bose-project
python -m pip install -r requirements.txt
code .
```

## Configuration

Before using the GitHub Star Notifier, you need to configure the following parameters:

- `REPOSITORIES`: A list of repositories you want to monitor (in the format `'owner/repo'`).
- `TELEGRAM_BOT_TOKEN`: The token for your Telegram bot.
- `TELEGRAM_CHAT_ID`: The chat ID where you want to receive the notifications.

## Usage

To use the GitHub Star Notifier, follow these steps:

1. Open the `config.py` file.
2. Configure the necessary parameters mentioned in the Configuration section.
3. Run the script by executing the following command:
   ```shell
   python github_star_notifier.py
   ```
4. The notifier will start monitoring the specified repositories and send Telegram messages whenever a new star is detected.

## Customization

- You can adjust the interval between (1 minute by default) star checks by changing the wait time in `config.py`.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
