# 6. Feedback Agent (agents/feedback.py)
# This agent processes feedback from campaign performance and adjusts strategies accordingly.

# agents/feedback.py

from models.llm import process_feedback

class FeedbackAgent:
    def __init__(self, ad_data, performance_data, campaign_data):
        self.ad_data = ad_data
        self.performance_data = performance_data
        self.campaign_data = campaign_data

    def process_feedback(self):
        # Use LLM to process feedback and adjust strategies
        updated_ad_data, updated_campaign_data = process_feedback(self.ad_data, self.performance_data, self.campaign_data)
        return updated_ad_data, updated_campaign_data
