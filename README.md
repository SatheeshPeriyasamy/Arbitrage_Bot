# Arbitrage Bot

## Description
Arbitrage Bot is an automated trading bot that identifies and exploits price discrepancies between spot and futures cryptocurrency markets on the Binance platform. It leverages Flask for its dashboard and asyncio for real-time operations, enabling users to monitor and control trading activities effectively.

## Features
- **Real-Time Trading**: Utilizes websockets for live market data fetching.
- **User-Friendly Dashboard**: Flask-powered web interface for easy monitoring and control.
- **Arbitrage Strategies**: Targets opportunities between spot and futures markets.
- **Secure**: Uses environment variables for API key management to enhance security.

## Installation

### Prerequisites
- Python 3.7 or later
- pip (Python package installer)

### Setup
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/Arbitrage_Bot.git
cd Arbitrage_Bot
```
Clone the repository to your local machine:
```bash
pip install -r requirements.txt
```
## Configuration
Set up the necessary environment variables:
```bash
export BINANCE_API_KEY='your_binance_api_key_here'
export BINANCE_API_SECRET='your_binance_api_secret_here'
```
For Windows, use set instead of export.

## Usage
Start the application:
```bash
python app.py
```
Navigate to http://localhost:5000 in your web browser to access the dashboard.
