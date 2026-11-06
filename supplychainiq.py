import math

# name: (stock, last-7-days sales, {supplier: (unit_cost, lead_days)})
DATA = {
  "Laptop":   (15,  [10,12,9,11,10,8,10], {"A": (500, 5), "B": (470, 9)}),
  "Mouse":    (200, [20,22,18,21,19,20,20], {"A": (8, 4),   "B": (7, 7)}),
  "Keyboard": (40,  [5,5,5,5,5,5,5],      {"A": (20, 6),  "B": (18, 10)}),
}
REVIEW_DAYS, SAFETY = 7, 0.2   # order covers lead time + 7 days + 20% safety stock

def plan(stock, avg, cost, lead):
    safety = math.ceil(SAFETY * avg * lead)
    qty = max(0, math.ceil(avg * (lead + REVIEW_DAYS) + safety - stock))
    short = max(0, lead - stock / avg) * avg      # units lost while waiting
    return qty, qty * cost, round(short)

rows = []
for name, (stock, sales, sups) in DATA.items():
    avg = sum(sales) / len(sales)                 # tool 1: sales history analysis
    cover = stock / avg                           # days of stock left
    min_lead = min(l for _, l in sups.values())
    status = ("CRITICAL" if cover < min_lead
              else "WATCH" if cover < 1.5 * min_lead else "OK")   # tool 2: stockout risk
    rows.append((cover, name, stock, avg, status, sups))

print("=== SupplyChainIQ Procurement Plan ===")
for cover, name, stock, avg, status, sups in sorted(rows):       # most urgent first
    print(f"\n{name}: stock={stock}, avg demand={avg:.0f}/day, cover={cover:.1f} days -> {status}")
    if status == "OK":
        print("  Action: no order needed")
        continue
    # tool 3: supplier comparison, two strategies
    for label, key in (("Fast", lambda s: s[1][1]), ("Economy", lambda s: s[1][0])):
        sid, (cost, lead) = min(sups.items(), key=key)
        qty, total, short = plan(stock, avg, cost, lead)         # tool 4: reorder calculation
        print(f"  {label:8} Supplier {sid}: order {qty} units, cost Rs {total:,}, lead {lead}d, stockout units {short}")