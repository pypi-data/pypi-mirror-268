from typing import List
import re
from recipe_urls._abstract import AbstractScraper

class RainbowPlantLifeScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "rainbowplantlife.com"

    def scrape(self) -> List[str]:
        try:
            href_links = [a["href"] for a in self.soup.find_all("a", href=True)]
        except (TypeError, AttributeError) as e:
            raise ValueError(f"Failed to extract href links: {e}") from e

        # Filter href links for recipe-specific ones using site-specific regex
        recipe_links = self.filter_links(href_links)

        return recipe_links

    def filter_links(self, href_links: List[str]) -> List[str]:

        # Filter out unwanted url patterns
        unwanted_patterns = [
            "accessibility", 
            "add", 
            "alternatives", 
            "daily", 
            "essential", 
            "equipment", 
            "guide", 
            "grocery", 
            "policy", 
            "recipes",
            "sources",  
            "stories", 
            "tips", 
            "work"
        ]

        # Site-specific regex for RainbowPlantLife
        recipe_pattern = re.compile(r'https://rainbowplantlife\.com/(?![\w-]*\d)[\w-]+-[\w-]+/')

        # Use a set to deduplicate the links while filtering href links for recipe-specific ones
        unique_links_set = set(link for link in href_links if recipe_pattern.search(link) and not any(re.search(pattern, link) for pattern in unwanted_patterns))
        print(f"{len(unique_links_set)} recipe links found for {self.base_url}.")

        # Convert the set back to a list
        return list(unique_links_set)