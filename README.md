# Golf.com's Top Public Golf Courses

Web page to explore [Golf.com's top 100 public courses](https://golf.com/travel/courses/best-public-golf-courses-top-100-you-can-play-2020-21/)

## Fetch Data
* Get Google API Key [here](https://console.cloud.google.com/project/_/apiui/credential?_ga=2.188521064.153410142.1620194316-1220513884.1542082721)
    - Will need to specifically enable Geocoding API in [Developer Console](https://console.developers.google.com/) > Google Maps > APIs > Geocoding API
    - Will need to enable billing [here](https://console.cloud.google.com/billing?_ga=2.160027005.1955764839.1620197454-1220513884.1542082721)
    - set env variable to your API key
        ```bash
        export GOOGLE_GEOCODE_API_KEY=`your key here`
        ```
* Install requirements
    ```bash
    pip3 install -r requirements.txt
    ```


