# 7. Machine Learning Agent (agents/machine_learning.py)
# This agent leverages past data to predict and improve campaign performance over time, refining targeting and bidding strategies.

# agents/machine_learning.py

from models.llm import predict_campaign_performance

class MachineLearningAgent:
    def __init__(self, past_campaign_data):
        self.past_campaign_data = past_campaign_data

    def predict_performance(self):
        # Use LLM to predict future campaign performance based on past data
        predicted_performance = predict_campaign_performance(self.past_campaign_data)
        return predicted_performance
