# AdFlux Agentic Engine

![Screenshot_2025-01-06_at_10 57 30_AM-removebg-preview](https://github.com/user-attachments/assets/9b4967a7-dd94-4916-88dd-0ca8b711ea90)

## Overview
This AdFlux Agentic Engine is a agentic workflow benefits from llms and advertising foundation model that combines both the general process of a digital advertising system and the specific steps to optimize the display of the best ads to users. The goal is to improve performance by ensuring that ads are highly relevant, well-timed, and continuously optimized for both user engagement and advertiser conversion goals.


### Key Features:
- **Modular Agent Design**: This allows for flexible improvements and extensions, making the system adaptable to different needs.
- **LLM Integration**: The system uses LLMs to generate dynamic content and provide data-driven insights.
- **Real-Time Optimization**: Automated adjustments based on user interactions and campaign performance.
- **Machine Learning**: Predictive capabilities to optimize future campaigns.


## Usage

### 1. Setup Campaign
The CampaignSetupAgent initializes the campaign by defining the objective, target audience, ad format, budget, and bidding strategy. It uses LLMs to suggest campaign recommendations.

```bash
from agents.campaign_setup import CampaignSetupAgent

# Example of initializing the campaign
campaign_agent = CampaignSetupAgent("Increase Sales", {"age": 25, "location": "US", "interest": "tech"}, "video", 1000, "CPC")
campaign_data = campaign_agent.setup_campaign()
```

### 2. Create Ad
The AdCreationAgent generates ad creatives dynamically based on product type and target audience. It uses LLMs to create optimized ad copy.

```bash
from agents.ad_creation import AdCreationAgent

# Example of creating an ad
ad_creation_agent = AdCreationAgent("Tech Gadgets", {"age": 25, "location": "US"})
ad_data = ad_creation_agent.create_ad()
```

### 3. Run Auction
The AdAuctionAgent runs the ad auction, adjusting bids and relevance in real-time based on user data.

```bash
from agents.ad_auction import AdAuctionAgent

# Example of running the auction
ad_auction_agent = AdAuctionAgent(0.75, 0.85, {"interest": "tech"})
auction_result = ad_auction_agent.run_auction()
```

### 4. Track Performance
The PerformanceTrackingAgent tracks key performance metrics like CTR, CPC, and ROAS.

```bash
from agents.performance_tracking import PerformanceTrackingAgent

# Example of tracking ad performance
performance_tracking_agent = PerformanceTrackingAgent(ad_data["ad_copy"])
performance_data = performance_tracking_agent.track_performance()
```

### 5. Optimize Campaign
The OptimizationAgent uses real-time data to optimize campaign strategies, including adjusting bids, creatives, and targeting.

```bash
from agents.optimization import OptimizationAgent

# Example of optimizing campaign
optimization_agent = OptimizationAgent(campaign_data, performance_data)
optimized_campaign = optimization_agent.optimize_campaign()
```

### 6. Process Feedback
The FeedbackAgent processes feedback and adjusts campaign strategies based on performance data.

```bash
from agents.feedback import FeedbackAgent

# Example of processing feedback
feedback_agent = FeedbackAgent(ad_data, performance_data, optimized_campaign)
updated_ad_data, updated_campaign_data = feedback_agent.process_feedback()
```

### 7. Machine Learning Integration
The MachineLearningAgent learns from past campaigns and predicts future performance to improve targeting and bidding strategies.

```bash
from agents.machine_learning import MachineLearningAgent

# Example of predicting performance
machine_learning_agent = MachineLearningAgent(past_campaign_data)
predicted_performance = machine_learning_agent.predict_performance()
```

### 8. Main Execution
Run the entire process by executing the main.py script, which orchestrates all the agents.
```bash
python main.py
```

### **How to Extend**:
You can extend this system by adding more agent types, creating new models, or integrating additional LLM-based services for specialized tasks such as sentiment analysis or enhanced personalization.


## More Related Models

- **[AdFlux Engine](https://github.com/SJ9VRF/AdFlux-Engine)**: AdFlux Engine is a Foundation Model based Advertisement Simulator designed to predict and simulate user behavior (clicks and views) based on historical interaction data. Leveraging cutting-edge architectures like LAVA, Decision Transformers, Gato, and MuZero, AdFlux Engine helps optimize ad placements, enhance user engagement, and maximize conversion rates by including Reinforcement Learning from Human Feedback. Built with modularity and scalability in mind, AdFlux Engine combines the latest advancements in NLP, reinforcement learning, sequence modeling and RLHF.

- **[AdFlux PersonaTaste Engine](https://github.com/SJ9VRF/AdFlux-PersonaTaste-Engine)**: Enhancing AdFlux by incorporating persona-based tastes into AdFlux advertising Foundation Model, utilizing user behavior history such as shopping data or web clicks. The PersonaTaste Engine is designed to simulate more personalized user interactions by adapting to individual preferences, optimizing ad placements for better engagement.

