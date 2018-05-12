import get_news_dataset as news_dataset
import stock as stock
import get_keyword as keyword

# ---------------- Functions ----------------


#--------------------------------------------


# --------------- Main code ---------------

# 
input_firm = "asus"

# Load total news dataset
total_news_dataset = news_dataset.load_news_data()

# Get keywords of both rising and falling news
news_keyword = keyword.get_news_keyword(total_news_dataset,input_firm)

# Use RandomForest predict the new news

# Get the input_firm's keyword
# firm_keyword = keyword.get_firm_keyword(total_news_dataset,input_firm)

# Use the result of RandomForest's prediction to conclude whether the day will rise or fall




# -----------------------------------------