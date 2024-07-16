This Python script serves as a project to gather information about the electric vehicle company Canoo from various online sources. The project is divided into three main parts:

1. Basic Information Extraction from Wikipedia:

Utilizes the BeautifulSoup library to scrape and parse information from Canoo's Wikipedia page.
Extracts basic details from a specific table on the Wikipedia page, such as the company's founding date, key people, products, and other relevant information.
Creates a Pandas DataFrame and exports the data to an Excel file named 'basic_info.xlsx'.

2.Competitor Analysis from growjo.com:

Scrapes data on Canoo's competitors from the growjo.com website.
Cleans and organizes the competitor data into a Pandas DataFrame.
Removes unnecessary columns, fixes formatting issues, and exports the final competitor data to an Excel file named 'Canoo_competitors.xlsx'.
Google Custom Search API for Web Search:

3. Implements a script that uses Google Custom Search API to perform a web search for a specified query (in this case, 'Query').

Cleans the query string to create a valid filename for the Excel output.
Makes requests to the API in multiple iterations, retrieving search results in batches.
Normalizes the JSON data into a Pandas DataFrame and exports the results to an Excel file named based on the cleaned query string.


Notes:

1. Before running the Google Custom Search API section, you need to replace 'Your API_KEY' and 'Your SEARCH_ENGINE_ID' with your actual API key and custom search engine ID.
2. The 'Query' parameter in the script can be modified to any search query of interest.
3. The final output will be Excel files containing information about Canoo, its competitors, and search results related to the specified query.
4. This project showcases web scraping techniques, data manipulation using Pandas, and integration with a web search API to gather comprehensive information about a specific topic, in this case, the company Canoo.




