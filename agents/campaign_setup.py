# agents/campaign_setup.py
# 1. Campaign Setup Agent (agents/campaign_setup.py)
# This agent is responsible for setting up the campaign, including defining the objective, target audience, ad formats, and budget. It uses an LLM to recommend optimal strategies.

from models.llm import generate_campaign_recommendations

class CampaignSetupAgent:
    def __init__(self, objective, target_audience, ad_format, budget, bidding_strategy):
        self.objective = objective
        self.target_audience = target_audience
        self.ad_format = ad_format
        self.budget = budget
        self.bidding_strategy = bidding_strategy

    def setup_campaign(self):
        # Use LLM to generate recommendations based on objective and target audience
        campaign_details = generate_campaign_recommendations(self.objective, self.target_audience)
        campaign_data = {
            "objective": self.objective,
            "target_audience": self.target_audience,
            "ad_format": self.ad_format,
            "budget": self.budget,
            "bidding_strategy": self.bidding_strategy,
            "llm_recommendations": campaign_details
        }
        return campaign_data
