# 10. Main Script to Run the Agents (main.py)
# The main script coordinates all the agents in a workflow.

# main.py

from agents.campaign_setup import CampaignSetupAgent
from agents.ad_creation import AdCreationAgent
from agents.ad_auction import AdAuctionAgent
from agents.performance_tracking import PerformanceTrackingAgent
from agents.optimization import OptimizationAgent
from agents.feedback import FeedbackAgent
from agents.machine_learning import MachineLearningAgent
from utils.logger import log

def main():
    # Step 1: Setup Campaign
    campaign_agent = CampaignSetupAgent("Increase Sales", {"age": 25, "location": "US", "interest": "tech"}, "video", 1000, "CPC")
    campaign_data = campaign_agent.setup_campaign()
    log("Campaign Setup Complete.")

    # Step 2: Create Ad
    ad_creation_agent = AdCreationAgent("Tech Gadgets", {"age": 25, "location": "US"})
    ad_data = ad_creation_agent.create_ad()
    log("Ad Creation Complete.")

    # Step 3: Run Auction
    ad_auction_agent = AdAuctionAgent(0.75, 0.85, {"interest": "tech"})
    auction_result = ad_auction_agent.run_auction()
    log(f"Auction Result: {auction_result}")

    # Step 4: Track Performance
    performance_tracking_agent = PerformanceTrackingAgent(ad_data["ad_copy"])
    performance_data = performance_tracking_agent.track_performance()
    log(f"Performance Data: {performance_data}")

    # Step 5: Optimize Campaign
    optimization_agent = OptimizationAgent(campaign_data, performance_data)
    optimized_campaign = optimization_agent.optimize_campaign()
    log(f"Optimized Campaign: {optimized_campaign}")

    # Step 6: Process Feedback
    feedback_agent = FeedbackAgent(ad_data, performance_data, optimized_campaign)
    updated_ad_data, updated_campaign_data = feedback_agent.process_feedback()
    log(f"Feedback Processed: Updated Ad Data and Campaign Data.")

if __name__ == "__main__":
    main()
