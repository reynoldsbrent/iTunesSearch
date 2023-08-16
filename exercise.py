import requests

# Function to perform the iTunes search
def itunes_search(search_term):
    base_url = "https://itunes.apple.com/search"
    params = {
        "term": search_term,
        "entity": "album"
    }
    
    # Send GET request to the iTunes Search Service
    response = requests.get(base_url, params=params)
    # Parse the response as JSON
    data = response.json()
    return data

# Main program
def main():
    # Get the search term from the user
    search_term = input("Please enter a search term: ")
    # Perform the iTunes search
    search_results = itunes_search(search_term)
    
    # Get the total number of search results
    result_count = search_results["resultCount"]
    print(f"The search returned {result_count} results.")
    
    # Iterate through each result and print artist, album, and track count
    results = search_results["results"]
    for result in results:
        artist_name = result["artistName"]
        album_name = result["collectionName"]
        track_count = result["trackCount"]
        
        print(f"Artist: {artist_name} - Album: {album_name} - Track Count: {track_count}")

# Entry point of the program
if __name__ == "__main__":
    main()