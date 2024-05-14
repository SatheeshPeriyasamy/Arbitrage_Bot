from flask import Flask, render_template, redirect, url_for, request
import threading
import asyncio
import arbitrage_bot

app = Flask(__name__)
bot_thread = None
stop_event = threading.Event()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', transactions=arbitrage_bot.transactions, bot_running=bot_thread.is_alive() if bot_thread else False)

@app.route('/start', methods=['POST'])
def start_bot():
    global bot_thread, stop_event
    if not bot_thread or not bot_thread.is_alive():
        stop_event.clear()
        bot_thread = threading.Thread(target=lambda: asyncio.run(arbitrage_bot.monitor_markets(stop_event)))
        bot_thread.start()
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop_bot():
    global stop_event
    if bot_thread and bot_thread.is_alive():
        stop_event.set()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
