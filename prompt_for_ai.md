# Role
You are a Senior Python Backend Developer and DevOps Engineer specialized in GitHub Actions and automation.

# Context
I am building a project called `teams-daily-briefing`. 
This is a serverless Python bot that runs on GitHub Actions to send daily stock market briefings to a Microsoft Teams channel via Webhook.

Here is the `README.md` that defines the project specifications:

---
# 📈 Teams Daily Briefing

A serverless Python bot that sends automated stock market briefings (or any custom messages) to a Microsoft Teams channel.

Powered by **GitHub Actions**, it runs on a schedule but **smartly skips weekends and South Korean public holidays**.

> **Note:** This project is designed to be forked and configured without writing any code.

## ✨ Features

* **Serverless:** Runs entirely on GitHub Actions (Free tier friendly).
* **Smart Scheduling:** Configured to run at **09:30 KST** (UTC 00:30).
* **Holiday Aware:** Uses `pytimekr` to automatically skip execution on weekends and Korean national holidays.
* **Secure:** Sensitive Webhook URLs are managed via GitHub Secrets.
* **Customizable:** Target stock tickers are managed via GitHub Variables.

---

## 🚀 Quick Start Guide

Follow these steps to set up your own notification bot.

### 1. Fork this Repository
Click the **Fork** button at the top right of this page to create a copy of this repository in your own GitHub account.

### 2. Generate Teams Webhook URL (Important)
Microsoft Teams now uses the **"Workflows"** app to handle incoming webhooks.

### 3. Configure GitHub Secrets & Variables
You need to store your Webhook URL securely and define which stocks to track.

#### A. Add Webhook URL (Secret)
1.  Go to your forked repository on GitHub.
2.  Navigate to **Settings** > **Secrets and variables** > **Actions**.
3.  Under the **Secrets** tab, click **New repository secret**.
4.  **Name:** `TEAMS_WEBHOOK_URL`
5.  **Secret:** Paste the Webhook URL you copied in Step 2.
6.  Click **Add secret**.

#### B. Add Stock Tickers (Variable)
1.  Stay in the same menu, but switch to the **Variables** tab.
2.  Click **New repository variable**.
3.  **Name:** `TARGET_STOCKS`
4.  **Value:** Enter stock codes separated by commas (e.g., `005930,035420,000660`).
5.  Click **Add variable**.

### 4. Enable the Workflow
By default, GitHub Actions might be disabled on forked repositories.

1.  Go to the **Actions** tab in your repository.
2.  Click the button **"I understand my workflows, go ahead and enable them"**.
3.  The bot is now active! It will run automatically at 09:30 KST on workdays.

---

## 🛠️ How to Test Manually
You don't have to wait until tomorrow morning to see if it works.

1.  Go to the **Actions** tab.
2.  Select **Daily Stock Alert** from the left sidebar.
3.  Click the **Run workflow** dropdown button on the right.
4.  Click **Run workflow**.
5.  Check your Teams channel for the message.

---

## 📅 Scheduling & Timezone
* The workflow is defined in `.github/workflows/daily_alert.yml`.
* **Cron Syntax:** `30 0 * * 1-5`
    * This corresponds to **00:30 UTC**, which is **09:30 KST**.
* **Holiday Logic:** The Python script (`src/main.py`) explicitly checks for Korean holidays using the `pytimekr` library and exits gracefully if it is a holiday.

## 🤝 Contributing
Feel free to submit Pull Requests to add new features or improve the message formatting!

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---

# Task
Based on the README above, please implement the full source code structure.
The code must be modular, production-ready, and error-proof.

# Requirements & File Structure

Please generate the following files:

1. **`src/main.py`** (Entry Point)
   - Load environment variables (`TEAMS_WEBHOOK_URL`, `TARGET_STOCKS`).
   - Use `pytimekr` to check if today is a South Korean public holiday.
   - If it is a holiday or weekend, exit successfully without sending a message.
   - If it is a workday, call modules to fetch data and send the message.
   - Use `logging` instead of `print`.

2. **`src/market_data.py`** (Data Fetching)
   - Create a function `get_stock_price(ticker_list)`.
   - Use `finance-datareader` library (or `yfinance`) to get real-time data for KOSPI/KOSDAQ stocks.
   - Return a structured dictionary or list with stock name, current price, and change rate.

3. **`src/message_builder.py`** (UI/UX)
   - Create a function `create_teams_payload(stock_data)`.
   - **Important:** Do NOT use simple text. Use **Microsoft Teams Adaptive Cards (JSON)** for a professional look.
   - Include a title, a table or list of stocks, and color-coded indicators (Red for up, Blue for down - *Note: In Korea, Red is up, Blue is down*).

4. **`.github/workflows/daily_alert.yml`** (CI/CD)
   - Schedule: Cron `30 0 * * 1-5` (09:30 KST).
   - Define `TEAMS_WEBHOOK_URL` as a secret and `TARGET_STOCKS` as a variable.

5. **`requirements.txt`**
   - Include `requests`, `pytimekr`, `finance-datareader` (or equivalent).

# Constraints
- Keep the code clean and follow PEP8 standards.
- Add docstrings to all functions.
- Handle exceptions (e.g., if stock API fails, send an error message to Teams or log it).