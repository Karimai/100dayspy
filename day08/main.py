def calculate_love_score(love, lover):
    first_measurement = 'true'
    second_measurement = 'love'
    first_measure = 0
    second_measure = 0
    for name in [love, lover]:
        first_measure += sum(1 for ch in name if ch.lower() in first_measurement)
        second_measure += sum(1 for ch in name if ch.lower() in second_measurement)
    
    print(f"Love Score = {first_measure}{second_measure}")
    

if __name__ == "__main__":
    calculate_love_score("Angela Yu", "Jack Bauer")
    calculate_love_score("Kanye West", "Kim Kardashian")


