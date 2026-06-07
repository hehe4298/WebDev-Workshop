from src.categorization.categorizer import categorize_article

def test_categorize_ai():
    title = "New advances in Artificial Intelligence"
    content = "ChatGPT and other neural network models are improving."
    category = categorize_article(title, content)
    assert category == "AI"

def test_categorize_semiconductors():
    title = "TSMC announces new chip process"
    content = "The semiconductor industry is growing."
    category = categorize_article(title, content)
    assert category == "Semiconductors"

def test_categorize_other():
    title = "New movie released"
    content = "A new blockbuster hit theaters today."
    category = categorize_article(title, content)
    assert category == "Other"

def test_categorize_case_insensitive():
    title = "ROBOTICS in modern times"
    content = "Some robots are very advanced."
    category = categorize_article(title, content)
    assert category == "Robotics"
