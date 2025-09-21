import requests
import re

# Function to extract MediaFire download link from AdFoc.us URL

def extract_mediafire_link(adfoc_url):
    try:
        # Send a GET request to the AdFoc.us URL
        response = requests.get(adfoc_url)
        response.raise_for_status()  # Check for HTTP errors

        # Use regex to find MediaFire link in the response text
        mediafire_link_pattern = re.compile(r'(https?://www\.mediafire\.com/download/[^\s]+)')
        mediafire_link = mediafire_link_pattern.search(response.text)

        if mediafire_link:
            return mediafire_link.group(0)  # Return the first match
        else:
            return "No MediaFire link found."
    except Exception as e:
        return str(e)

# Example usage
if __name__ == '__main__':
    adfoc_url = input('Enter the AdFoc.us URL: ')
    print('Extracted MediaFire link:', extract_mediafire_link(adfoc_url))