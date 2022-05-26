import requests

class listingAPIClient:

    def __init__(self, APIKey):
        apikey = apikey

        self.headers = {"apikey":apikey}

        # Predefined Headers


    def getListing(self, listingID):
        baseHost = "https://www.domain.com.au"
        URLEndpoint = "/v2/listing/"+listingID

        response = requests.get(baseHost+URLEndpoint, headers=self.headers)

        status = response.status_code

        # Success
        if (status == '200'):
            return response.text
        
        # Unauthorized
        elif (status == '401'):
            return response.errors

        # Not Found
        elif (status == '404'):
            return response.errors

        # Internal Server Error
        elif (status == '500'):
            return {"status":500,"error":"An Unknown Error Occured."}

        # Network Errrs or URL incorrect
        elif (status == '0'):
            return {"status":0,"error":"Website could not be reached."}
        else:
            # Handle
            return response.errors




