# modules/tech_detect.py

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


from Wappalyzer import Wappalyzer, WebPage

def detect(domain):
    try:
        url = f"http://{domain}"
        webpage = WebPage.new_from_url(url, timeout=10)
        wappalyzer = Wappalyzer.latest()
        technologies = wappalyzer.analyze_with_versions_and_categories(webpage)
        return technologies
    except Exception as e:
        return {"error": str(e)}
