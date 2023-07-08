<p align="center">
  <img src="https://www.omkar.cloud/images/favicon/prod/favicon-256x256.png" alt="omkar" />
</p>
  <div align="center" style="margin-top: 0;">
  <h1>✨ GitHub Star Notifier ✨</h1>
  <!-- <p>💦 Enjoy the Rain of Google Maps Leads 💦</p> -->
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="github-star-notifier forks" src="https://img.shields.io/github/forks/omkarcloud/github-star-notifier?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/github-star-notifier?style=for-the-badge&color=yellow" />
  </a>
  <a href="#">
    <img alt="github-star-notifier License" src="https://img.shields.io/github/license/omkarcloud/github-star-notifier?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/github-star-notifier/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/github-star-notifier?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/github-star-notifier.svg" width="80px" height="28px" alt="View" />
</p>

---

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
