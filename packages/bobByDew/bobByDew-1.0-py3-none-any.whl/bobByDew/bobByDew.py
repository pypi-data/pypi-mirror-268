import asyncio
import json
import websockets
from datetime import datetime
import curses


# Setup curses color pairs
def setup_curses_colors():
  curses.start_color()
  curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
 
async def get_snapshot(websocket):
  snapshot_request = {
      "method": "SUBSCRIBE",
      "params": ["btcusdt@depth20@100ms"],
      "id": 1
  }
  await websocket.send(json.dumps(snapshot_request))
  while True:
    response = await websocket.recv()
    data = json.loads(response)
    if "result" not in data:
      return data


def calculate_metrics(bids, asks):
  highest_bid = max(float(bid[0]) for bid in bids)
  lowest_ask = min(float(ask[0]) for ask in asks)
  spread = lowest_ask - highest_bid

  bid_weights = [float(bid[0]) * float(bid[1]) for bid in bids]
  ask_weights = [float(ask[0]) * float(ask[1]) for ask in asks]
  bid_volume = sum(float(bid[1]) for bid in bids)
  ask_volume = sum(float(ask[1]) for ask in asks)

  weighted_avg_bid = sum(bid_weights) / bid_volume if bid_volume else 0
  weighted_avg_ask = sum(ask_weights) / ask_volume if ask_volume else 0

  order_flow_imbalance = bid_volume - ask_volume

  return {
      "spread": spread,
      "weighted_avg_bid": weighted_avg_bid,
      "weighted_avg_ask": weighted_avg_ask,
      "total_volume": bid_volume + ask_volume,
      "order_flow_imbalance": order_flow_imbalance
  }


def update_order_book_line(stdscr, y, x, text, color_pair=None):
  stdscr.move(y, x)
  stdscr.clrtoeol()
  if color_pair:
    stdscr.addstr(y, x, text, color_pair)
  else:
    stdscr.addstr(y, x, text)


def print_order_book_snapshot(stdscr, order_book, previous_data):
  # Static labels and headers are only printed once, outside this function to reduce flicker
  bids = [(bid[0], bid[1]) for bid in order_book.get('bids', [])][:10]
  asks = [(ask[0], ask[1]) for ask in order_book.get('asks', [])][:10]
  metrics = calculate_metrics(bids, asks)
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  # Update dynamic data only
  metrics_info = [
      f"Timestamp: {timestamp}", f"Spread: {metrics['spread']:.2f}",
      f"Weighted Avg Bid: {metrics['weighted_avg_bid']:.2f}",
      f"Weighted Avg Ask: {metrics['weighted_avg_ask']:.2f}",
      f"Total Volume: {metrics['total_volume']:.2f}",
      f"Order Flow Imbalance: {metrics['order_flow_imbalance']:.2f}"
  ]
  for idx, line in enumerate(metrics_info):
    update_order_book_line(stdscr, idx, 0, line)

  for i, (price, quantity) in enumerate(bids, start=1):
    price = float(price)
    quantity = float(quantity)
    text = f"{price:.8f}  {quantity:.8f}"
    if previous_data['bids'].get(price, 0) != quantity:
      update_order_book_line(stdscr, 7 + i, 0, text, curses.color_pair(1))
    else:
      update_order_book_line(stdscr, 7 + i, 0, text)

  for i, (price, quantity) in enumerate(asks, start=1):
    price = float(price)
    quantity = float(quantity)
    text = f"{price:.8f}  {quantity:.8f}"
    if previous_data['asks'].get(price, 0) != quantity:
      update_order_book_line(stdscr, 21 + i, 0, text, curses.color_pair(2))
    else:
      update_order_book_line(stdscr, 21 + i, 0, text)

  stdscr.refresh()


def setup_static_display(stdscr):
  # Print static titles and headers once to avoid flicker
  stdscr.addstr(7, 0, "Current Bids:")
  stdscr.addstr(21, 0, "Current Asks:")
  stdscr.refresh()


def async_wrapper(stdscr):
  setup_curses_colors()
  setup_static_display(stdscr)
  loop = asyncio.get_event_loop()
  loop.run_until_complete(stream_order_book(stdscr))


async def stream_order_book(stdscr):
  previous_data = {"bids": {}, "asks": {}}
  async with websockets.connect(
      "wss://stream.binance.us:9443/ws") as websocket:
    order_book = await get_snapshot(websocket)
    previous_data['bids'] = {
        float(bid[0]): float(bid[1])
        for bid in order_book.get('bids', [])
    }
    previous_data['asks'] = {
        float(ask[0]): float(ask[1])
        for ask in order_book.get('asks', [])
    }
    print_order_book_snapshot(stdscr, order_book, previous_data)

    async for message in websocket:
      update = json.loads(message)
      if "bids" in update and "asks" in update:
        update['bids'] = [(float(price), float(quantity))
                          for price, quantity in update['bids']]
        update['asks'] = [(float(price), float(quantity))
                          for price, quantity in update['asks']]
        print_order_book_snapshot(stdscr, update, previous_data)
        previous_data['bids'] = {
            price: quantity
            for price, quantity in update['bids']
        }
        previous_data['asks'] = {
            price: quantity
            for price, quantity in update['asks']
        }


def main():
  curses.wrapper(async_wrapper)


if __name__ == "__main__":
  main()
