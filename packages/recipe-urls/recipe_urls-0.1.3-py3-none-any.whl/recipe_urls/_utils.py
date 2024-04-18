from typing import Optional
from urllib.parse import urlparse

def get_site_origin(base_url: str) -> Optional[str]:
    site_origins = [
        'abuelascounter.com', 
        'www.acouplecooks.com', 
        'addapinch.com', 
        'www.afghankitchenrecipes.com', 
        'www.allrecipes.com', 
        'www.ambitiouskitchen.com', 
        'www.archanaskitchen.com', 
        'www.averiecooks.com',
        'bakingmischief.com',
        'www.baking-sense.com',
        'barefootcontessa.com',
        'www.bbc.co.uk',  
        'www.bettycrocker.com', 
        'www.bigoven.com', 
        'bluejeanchef.com', 
        'www.bonappetit.com', 
        'www.bongeats.com',
        'www.bowlofdelicious.com', 
        'www.budgetbytes.com', 
        'carlsbadcravings.com', 
        'www.castironketo.net', 
        'www.cdkitchen.com', 
        'chefsavvy.com', 
        'www.closetcooking.com', 
        'cookieandkate.com',
        'copykat.com', 
        'www.countryliving.com',
        'creativecanning.com',  
        'www.davidlebovitz.com', 
        'www.delish.com', 
        'domesticate-me.com', 
        'downshiftology.com', 
        'www.eatingbirdfood.com', 
        'www.eatingwell.com', 
        'www.eatliverun.com', 
        'eatsmarter.com', 
        'www.eatwell101.com', 
        'eatwhattonight.com', 
        'elavegan.com', 
        'www.ethanchlebowski.com', 
        'www.errenskitchen.com', 
        'www.epicurious.com', 
        'www.farmhouseonboone.com', 
        'www.fifteenspatulas.com', 
        'www.finedininglovers.com', 
        'fitmencook.com', 
        'fitslowcookerqueen.com', 
        'www.food.com',
        'food52.com',
        'www.foodandwine.com', 
        'www.foodnetwork.com', 
        'www.foodrepublic.com', 
        'www.forksoverknives.com', 
        'forktospoon.com', 
        'www.gimmesomeoven.com', 
        'goodfooddiscoveries.com', 
        'www.goodhousekeeping.com', 
        'www.gonnawantseconds.com',
        'www.greatbritishchefs.com', 
        'www.halfbakedharvest.com', 
        'handletheheat.com', 
        'headbangerskitchen.com', 
        'heatherchristo.com',  
        'www.hellofresh.com',
        'www.hersheyland.com',
        'hostthetoast.com', 
        'im-worthy.com', 
        'www.indianhealthyrecipes.com', 
        'insanelygoodrecipes.com', 
        'inspiralized.com', 
        'izzycooking.com', 
        'www.jamieoliver.com',
        'jimcooksfoodgood.com', 
        'joyfoodsunshine.com',  
        'www.justataste.com', 
        'justbento.com', 
        'www.justonecookbook.com', 
        'www.kingarthurbaking.com', 
        'leanandgreenrecipes.net',
        'lifestyleofafoodie.com',  
        'littlespicejar.com', 
        'livelytable.com', 
        'lovingitvegan.com', 
        'ninjatestkitchen.eu', 
        'cooking.nytimes.com', 
        'ohsheglows.com', 
        'www.onceuponachef.com', 
        'www.paleorunningmomma.com', 
        'www.persnicketyplates.com', 
        'www.pickuplimes.com',
        'www.platingpixels.com', 
        'rachlmansfield.com',
        'rainbowplantlife.com', 
        'reciperunner.com', 
        'sallysbakingaddiction.com', 
        'simple-veganista.com', 
        'www.simplywhisked.com', 
        'www.tasteofhome.com', 
        'tasty.co'
    ]

    if isinstance(base_url, str):

        # If https:// is not specified
        for site_origin in site_origins:
            if site_origin == base_url:
                return site_origin

        # If https:// is specified
        parsed_url = urlparse(base_url).hostname
        for site_origin in site_origins:
            if site_origin == parsed_url:
                return site_origin

        raise ValueError(f"URL '{base_url}' is not supported.")

    else:
        raise ValueError(f"URL format '{type(base_url)}' is not supported.")
