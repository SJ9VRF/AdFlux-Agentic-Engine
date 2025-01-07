# 5. Optimization Agent (agents/optimization.py)
# This agent dynamically optimizes ad campaigns by adjusting bids, creatives, or targeting based on real-time performance data.

# agents/optimization.py

from models.llm import optimize_campaign

class OptimizationAgent:
    def __init__(self, campaign_data, performance_data):
        self.campaign_data = campaign_data
        self.performance_data = performance_data

    def optimize_campaign(self):
        # Use LLM to optimize campaign in real-time
        optimized_campaign = optimize_campaign(self.campaign_data, self.performance_data)
        return optimized_campaign
