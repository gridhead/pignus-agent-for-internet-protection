from virus_total_apis import PublicApi as VirusTotalPublicApi

def fetchapikey():
    apidir = open("virustotal.key")
    apikey = apidir.read()
    apidir.close()
    return apikey

def main(url):
    apikey = fetchapikey()
    vt = VirusTotalPublicApi(apikey)
    response = vt.get_url_report(url)
    if "error" in response.keys():
        totalscn = "NaN"
        positscn = "NaN"
        verbmesg = "Please check your internet connection and the URL for typos and try again"
        scanidty = "Scan ID not fetched"
        scanurle = "Scan URL not fetched"
        scandate = "Scan date not fetched"
        lichtdic = []
        reply = [lichtdic, totalscn, positscn, scanurle, scandate, scanidty, verbmesg]
    else:
        tablcont = response["results"]["scans"]
        scsource = list(tablcont.keys())
        detction, resulted, detailed, tuplsore = [], [], [], ()
        for sites in scsource:
            detction.append(str(tablcont[sites]["detected"]))
            resulted.append(str(tablcont[sites]["result"]).title())
            try:
                detailed.append(str(tablcont[sites]["detail"]))
            except KeyError:
                detailed.append("N/A")
        totalscn = str(response["results"]["total"])
        positscn = str(response["results"]["positives"])
        verbmesg = str(response["results"]["verbose_msg"])
        scanidty = str(response["results"]["scan_id"])
        scanurle = str(response["results"]["url"])
        scandate = str(response["results"]["scan_date"])
        lichtdic = []
        for i in range(len(scsource)):
            tuplsore = (scsource[i], detction[i], resulted[i], detailed[i])
            lichtdic.append(tuplsore)
        reply = [lichtdic, totalscn, positscn, scanurle, scandate, scanidty, verbmesg]
    return reply

if __name__=="__main__":
    print(main("t0xic0der.netlify.com"))