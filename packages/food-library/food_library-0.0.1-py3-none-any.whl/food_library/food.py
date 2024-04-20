def foodquote():
    import random  
    quotes = [
        "Life is uncertain. Eat dessert first.",
        "Good food is good mood.",
        "There is no love sincerer than the love of food.",
        "All you need is love. But a little chocolate now and then doesn't hurt.",
        "Cooking is love made visible.",
        "One cannot think well, love well, sleep well, if one has not dined well.",
        "Food is symbolic of love when words are inadequate.",
        "People who love to eat are always the best people.",
        "Laughter is brightest in the place where the food is.",
        "Food is the ingredient that binds us together.",
        "The only thing I like better than talking about food is eating.",
        "The secret ingredient is always love.",
        "Food tastes better when you eat it with your family.",
        "Eating is a necessity but cooking is an art.",
        "Happiness is homemade.",
        "There is no sincerer love than the love of food.",
        "First we eat, then we do everything else."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    random_quote = foodquote()
    print(random_quote)
