# Golf.com's Top Public Golf Courses
------------
Script to parse data from Golf.com's top 100 public courses, using Google's API to add additional data
TODO: visualize data on webpage using Google Map with markers

## Setup
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


