# Binance Futures Testnet Trading Bot

## Overview

This project is a simplified trading bot built in Python that interacts with the Binance Futures Testnet (USDT-M). It allows users to place MARKET and LIMIT orders via CLI with proper logging, validation, and structured code design.

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL sides
* CLI based input using argparse
* Input validation and error handling
* Structured modular code
* Logging of requests, responses, and errors
* Uses Binance Futures Testnet



## Setup Instructions

### 1. Clone repository

git clone <your_repo_link>
cd trading_bot

### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create .env file

Add your Binance Testnet API keys:

API_KEY=
API_SECRET=
BASE_URL=https://testnet.binancefuture.com

## Usage

### Market Order

python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

### Limit Order

python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01 --price 30000

## Logs

All API requests, responses and errors are logged in:
logs/trading_bot.log


