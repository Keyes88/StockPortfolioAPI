import os
from datetime import datetime

# 30 stocks — real closing prices from Dec 4, 2025 (no internet ever needed)
MY_PORTFOLIO = [
    {"symbol":"AAPL","shares":15,"buy":170.00,"now":228.68},
    {"symbol":"MSFT","shares":12,"buy":320.00,"now":428.90},
    {"symbol":"GOOGL","shares":10,"buy":130.00,"now":183.42},
    {"symbol":"AMZN","shares":8,"buy":145.00,"now":201.34},
    {"symbol":"NVDA","shares":5,"buy":450.00,"now":141.54},
    {"symbol":"TSLA","shares":7,"buy":300.00,"now":357.09},
    {"symbol":"META","shares":10,"buy":380.00,"now":573.89},
    {"symbol":"AMD","shares":25,"buy":100.00,"now":156.13},
    {"symbol":"NFLX","shares":6,"buy":480.00,"now":689.21},
    {"symbol":"DIS","shares":20,"buy":110.00,"now":118.55},
    {"symbol":"JPM","shares":15,"buy":145.00,"now":198.42},
    {"symbol":"V","shares":10,"buy":240.00,"now":298.71},
    {"symbol":"PYPL","shares":18,"buy":90.00,"now":78.42},
    {"symbol":"ADBE","shares":4,"buy":580.00,"now":612.34},
    {"symbol":"INTC","shares":30,"buy":45.00,"now":42.18},
    {"symbol":"GME","shares":20,"buy":25.00,"now":38.91},
    {"symbol":"AMC","shares":50,"buy":12.00,"now":8.72},
    {"symbol":"PLTR","shares":40,"buy":22.00,"now":42.11},
    {"symbol":"NIO","shares":35,"buy":38.00,"now":5.92},
    {"symbol":"SOFI","shares":60,"buy":14.00,"now":17.83},
    {"symbol":"HOOD","shares":25,"buy":35.00,"now":38.21},
    {"symbol":"COIN","shares":8,"buy":220.00,"now":298.45},
    {"symbol":"RIVN","shares":15,"buy":100.00,"now":18.92},
    {"symbol":"LCID","shares":30,"buy":40.00,"now":3.21},
    {"symbol":"PFE","shares":40,"buy":38.00,"now":28.71},
    {"symbol":"MRNA","shares":12,"buy":180.00,"now":48.32},
    {"symbol":"XOM","shares":20,"buy":95.00,"now":118.92},
    {"symbol":"CVX","shares":15,"buy":140.00,"now":162.34},
    {"symbol":"SHOP","shares":10,"buy":110.00,"now":98.45},
    {"symbol":"CSCO","shares":25,"buy":52.00,"now":58.71},
]

def check_stock():
    s = input("\nEnter symbol: ").strip().upper()
    for stock in MY_PORTFOLIO:
        if stock["symbol"] == s:
            gain = stock["now"] - stock["buy"]
            pct = gain / stock["buy"] * 100
            color = "92m" if gain >= 0 else "91m"
            print(f"\n{stock['symbol']} → ${stock['now']:,.2f}   \033[{color}{gain:+.2f} ({pct:+$ 
            return
    print("Not in portfolio\n")
    
  def generate_portfolio():
    total = sum(s["now"] * s["shares"] for s in MY_PORTFOLIO)
    cards = ""
    for s in MY_PORTFOLIO:
        value = s["now"] * s["shares"]
        gain = value - s["buy"] * s["shares"]
        cls = "pos" if gain >= 0 else "neg"
        cards += f'<div class="card"><div class="sym">{s["symbol"]}</div><div class="price">${s["$
    
    html = f'''<!DOCTYPE html><html><head><meta charset="utf-8"><title>Colin Keyes Portfolio</tit$
<style>body{{font-family:system-ui;background:#0f2027;color:#eee;padding:20px}}
.c{{max-width:1500px;margin:auto;background:#fff;color:#000;border-radius:20px;padding:40px;box-s$
h1{{text-align:center;color:#1e3c72;font-size:3em}}.grid{{display:grid;grid-template-columns:repe$
.card{{background:#f9f9f9;padding:25px;border-radius:15px;text-align:center;box-shadow:0 8px 25px$
.sym{{font-size:2em;font-weight:bold;color:#1e3c72}}.price{{font-size:1.8em;font-weight:bold}}
.pos{{background:#d4edda;color:green;padding:8px;border-radius:8px}}
.neg{{background:#f8d7da;color:red;padding:8px;border-radius:8px}}</style></head><body>
<div class="c"><h1>Colin Keyes – 30 Stocks</h1>  
<p style="text-align:center;color:#666">Dec 4, 2025</p><div class="grid">{cards}</div>
<h2 style="text-align:center;margin-top:50px;color:#1e3c72;font-size:2.8em">Total: ${total:,.2f}<$
    with open("portfolio.html","w") as f: f.write(html)
    print("\nOpening portfolio.html …\n")
    os.system("open portfolio.html")
    
while True:   
    print("═" * 55)
    print("   COLIN KEYES – 30-STOCK PORTFOLIO")
    print("═" * 55)
    print("1. Check stock price")
    print("2. View full portfolio")
    print("3. Quit")
    c = input("\nChoose 1-3: ")
    if c == "1": check_stock()
    elif c == "2": generate_portfolio()
    elif c in ["3","q"]: print("Done!"); break


