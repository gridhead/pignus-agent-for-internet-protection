from virus_total_apis import PublicApi as VirusTotalPublicApi

def fetchapikey():
    apidir=open("virustotal.key")
    apikey=apidir.read()
    apidir.close()
    return apikey

def main(url):
    apikey = fetchapikey()
    vt = VirusTotalPublicApi(apikey)
    response = vt.scan_url(url)
    reply = []
    if "error" in response.keys():
        respcode="0x01"
        permlink="Report permalink could not be fetched due to an error"
        resource="Resource could not be fetched due to an error"
        scandate="Scan date could not be fetched due to an error"
        scanidty="Scan ID could not be fetched due to an error"
        verbmesg="Please check your internet connection and the URL for typos and try again"
        reply=[respcode,permlink,resource,scandate,scanidty,verbmesg]
    else:
        respcode=str(response["response_code"])
        permlink=str(response["results"]["permalink"])
        resource=str(response["results"]["resource"])
        scandate=str(response["results"]["scan_date"])
        scanidty=str(response["results"]["scan_id"])
        verbmesg=str(response["results"]["verbose_msg"])
        reply=[respcode,permlink,resource,scandate,scanidty,verbmesg]
    return reply

if __name__=="__main__":
    print(main("amazon.ru"))