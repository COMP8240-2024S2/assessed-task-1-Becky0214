import wikipedia

# Define the actor's name
actor_name = "TomCruise"

# Fetch the Wikipedia page content for the actor
try:
    page_content = wikipedia.page(actor_name).content
    word_count = len(page_content.split())
    
    print(f"Actor: {actor_name}")
    print(f"Page word count: {word_count} words")
    
    # Check if the page contains at least 500 words
    if word_count >= 500:
        # Save the content to a file
        with open("wikipedia.txt", "w", encoding="utf-8") as file:
            file.write(page_content)
        print("Content saved to wikipedia.txt")
    else:
        print("The Wikipedia page has fewer than 500 words, so the content will not be saved.")
        
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Disambiguation page found for {actor_name}: {e.options}")
except wikipedia.exceptions.PageError:
    print(f"Page not found for {actor_name}")

