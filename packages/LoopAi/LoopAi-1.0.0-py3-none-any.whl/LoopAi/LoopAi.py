import requests

class Ai:
    def __init__(self):
        self.base_url = "https://dev-the-dark-lord0.pantheonsite.io/wp-admin/js/Apis/"
    
    def make_request(self, endpoint, query):
        formatted_query = "%20".join(query.split())
        response = requests.get(self.base_url + endpoint + f"?message={formatted_query}")
        if response.status_code == 200:
            cleaned_response = response.text.replace("\n", " ")
            return cleaned_response
        else:
            return f"Error: {response.status_code}"
    
    def gemini(self, query):
        return self.make_request("Gemini.php", query)
    
    def worm(self, query):
        return self.make_request("WormGpt.php", query)
    
    def loop(self, query):
        return self.make_request("LoopGpt.php", query)
    
    def blackbox(self, mode, query):
        mode = mode.lower()
        modes = ["python", "java", "html", "android", "flutter", "javascript"]
        if mode not in modes:
            return "Unknown mode"
        
        endpoint = f"BlackBoxAi.php?mode={mode}&message="
        return self.make_request(endpoint, query)