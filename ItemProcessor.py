import listingAPIClient
from time import sleep


class ItemProcessor:

    def __init__(self, APIKey, failureLimit=3, failureWait=1,retries = True, retryCount=1):

        self.processor = listingAPIClient(APIKey)
        self.failureLimit = failureLimit
        self.failureWait = failureWait
        self.retryItem = retries
        self.retryCount = retryCount

    
    def ProcessItems(self,items):
        
        # ASSUME: [items]
        # ASSUME: items.listingID exists
        failureCount = 0

        for eachItem in items:
            
            response = self.processor.getListing(eachItem.listingID)

            if (response.status_code == '200'):
                #Handle Response
                print(response)

            if (response.status_code == '500'):
                #Handle Reponse
                print(response)
                failureCount += 1
                sleep(self.failureWait)
                
                if (self.retryItem):

                    for count in range(1,self.retryCount):

                        response = self.processor.getListing(eachItem.listingID)

                        if (response.status_code == '200'):
                            #Handle Response
                            print(response)

                        if (response.status_code == '500'):
                            #Handle Reponse
                            print(response)
                            failureCount += 1
                            sleep(self.failureWait)

            
            if (failureCount >= self.failureLimit):
                break










