from virus_total_apis import PublicApi as VirusTotalPublicApi
import time

def fetchapikey():
    apidir=open("virustotal.key")
    apikey=apidir.read()
    apidir.close()
    return apikey

def getwhoisres(response):
    try:
        return str(response["results"]["response_code"])
    except KeyError:
        return "N/A"

def getwhoitime(response):
    try:
        return str(response["results"]["whois_timestamp"])
    except KeyError:
        return "N/A"

def getdnsrecdt(response):
    try:
        return str(response["results"]["dns_records_date"])
    except KeyError:
        return "N/A"

def getsubdomsi(response):
    subdomsi=[]
    try:
        for item in response["results"]["domain_siblings"]:
            toopayle=(item,)
            subdomsi.append(toopayle)
    except KeyError:
        pass
    try:
        for item in response["results"]["subdomains"]:
            toopayle=(item,)
            subdomsi.append(toopayle)
    except KeyError:
        pass
    return subdomsi

def getwhoisdat(response):
    whotulst=[]
    whoisdat=response["results"]["whois"]
    whoisdat=whoisdat.split("\n")
    for i in range(len(whoisdat)):
        whoisdat[i]=whoisdat[i].split(": ")
    for i in range(len(whoisdat)):
        toopayle=(whoisdat[i][0], whoisdat[i][1])
        whotulst.append(toopayle)
    return whotulst

def getresolute(response):
    resolute=[]
    for item in response["results"]["resolutions"]:
        toopayle=(item["last_resolved"], item["ip_address"])
        resolute.append(toopayle)
    return resolute

def main(url):
    apikey=fetchapikey()
    vt=VirusTotalPublicApi(apikey)
    response = vt.get_domain_report(url)
    if "error" in response.keys():
        apiresco="NaN"
        whoisres="NaN"
        subdomsi=[]
        resolute=[]
        whotulst=[]
        whoitime="WhoIs timestamp not found"
        dnsrecdt="DNS record date not found"
        scandate="Scan date not found"
        verbmesg="Please check your internet connection and the URL for typos and try again"
        reply = [apiresco, whoisres, subdomsi, resolute, whotulst, whoitime, dnsrecdt, scandate, verbmesg]
    else:
        apiresco=str(response["response_code"])
        whoisres=str(getwhoisres(response))
        whoitime=str(getwhoitime(response))
        dnsrecdt=str(getdnsrecdt(response))
        subdomsi=getsubdomsi(response)
        whotulst=getwhoisdat(response)
        resolute=getresolute(response)
        scandate=str(time.ctime(int(time.time())))
        verbmesg=response["results"]["verbose_msg"]
        print("\n")
        print(apiresco)
        print(whoisres)
        print(subdomsi)
        print(resolute)
        print(whotulst)
        print(whoitime)
        print(dnsrecdt)
        print(scandate)
        print(verbmesg)
        reply=[apiresco,whoisres,subdomsi,resolute,whotulst,whoitime,dnsrecdt,scandate,verbmesg]
    return reply

if __name__=="__main__":
    print(main("t0xic0der.netlify.com"))