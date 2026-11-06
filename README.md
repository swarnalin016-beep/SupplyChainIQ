# SupplyChainIQ: Autonomous Supply Chain Decision Agent
Agentic Chase, Mission 02

## What it does
- Analyses sales history and average daily demand
- Detects stockout risk using stock, demand and supplier lead time
- Compares suppliers on cost and delivery time
- Calculates reorder quantity with 20% safety stock
- Generates a procurement plan with two strategies (Fast vs Economy)

## Run
python supplychainiq.py

## Example
15 units in stock, demand 10/day, lead time 5 days: demand during lead time is 50, so shortfall is 35 units. The agent flags CRITICAL and recommends an order.

## Limitations
Assumes constant demand and fixed safety stock. Next step: real ERP data and an LLM chat layer.
AI agent that detects stockout risk, compares suppliers, and generates procurement plans. Agentic Chase Mission 02.
