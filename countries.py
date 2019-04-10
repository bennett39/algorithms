import argparse
import requests


parser = argparse.ArgumentParser(description='Get information about countries.')
parser.add_argument('country', metavar='country', type=str, nargs='+',
                    help='The name or partial name of a country')

args = parser.parse_args()
country = ' '.join(vars(args)['country'])
url = "https://restcountries.eu/rest/v2/name/" + country
r = requests.get(url)

for country in r.json():
    print(f"\n------\n{country['name']} ({country['nativeName']})\n------")
    if country['capital']:
        print(f"Capital: {country['capital']}")
    if country['population']:
        print(f"Population: {country['population']}")
    if country['area']:
        print(f"Area: {country['area']}")
    if country['population'] and country['area']:
        print(f"Population Density {country['population'] / country['area']}")
    if country['languages']:
        print(f"Languages:")
        for language in country['languages']:
            print(f"\t{language['name']}")
