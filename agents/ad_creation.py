# 2. Ad Creation Agent (agents/ad_creation.py)
# This agent generates dynamic ad content, such as copy and creatives, based on the target audience and product type. It uses the LLM to optimize ad copy generation.

# agents/ad_creation.py

from models.llm import generate_ad_copy

class AdCreationAgent:
    def __init__(self, product_type, target_audience):
        self.product_type = product_type
        self.target_audience = target_audience

    def create_ad(self):
        # Use LLM to generate ad copy and creatives
        ad_copy = generate_ad_copy(self.product_type, self.target_audience)
        ad_data = {
            "product_type": self.product_type,
            "target_audience": self.target_audience,
            "ad_copy": ad_copy
        }
        return ad_data
