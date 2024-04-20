import random

def get_random_headline():
    # In place of these headlines, you should ideally have a mechanism to fetch real headlines from a news source
    headlines = [
        "Scientists make breakthrough in renewable energy research",
        "Global leaders gather for climate change summit",
        "New study shows promising results for cancer treatment",
        "SpaceX launches mission to explore Mars",
        "Major tech company announces breakthrough in artificial intelligence",
        "World Health Organization declares new global health emergency",
        "Stock markets rally following positive economic indicators",
        "United Nations releases report on human rights violations in conflict zones",
        "International efforts underway to address refugee crisis",
        "Researchers develop new vaccine for infectious disease",
        "Nobel Prize awarded to scientists for groundbreaking discovery",
        "World leaders sign historic peace agreement",
        "Scientists warn of alarming rise in sea levels",
        "New book becomes instant bestseller",
        "Global initiative launched to combat poverty",
        "Breaking: Major earthquake strikes region, relief efforts underway",
        "Renowned artist's latest work receives critical acclaim",
        "Humanitarian organization wins prestigious award for relief efforts",
        "Global cybersecurity summit addresses emerging threats",
        "Breakthrough in quantum computing promises revolutionary advancements"
    ]
    return random.choice(headlines)

if __name__ == "__main__":
    random_headline = get_random_headline()
    print(random_headline)
