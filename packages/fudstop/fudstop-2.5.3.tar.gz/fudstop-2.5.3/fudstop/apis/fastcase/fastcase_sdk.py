import asyncio
import httpx




class FastcaseSDK:
    def __init__(self):
        self.cookie = { 
            'Cookie': '_ga=GA1.3.1563370264.1705805803; _ga_8C39DM76B2=GS1.1.1709609683.2.0.1709609683.0.0.0; _ga_0X3Z0RSVQY=GS1.1.1711574911.15.0.1711574915.0.0.0; _ga_2V6G2TT2M3=GS1.1.1711850980.12.0.1711850980.0.0.0; _gid=GA1.3.1103897038.1712936361; _gid=GA1.2.1103897038.1712936361; __utmc=232144587; _ga_2V6G2TT2M3=GS1.1.1713106849.35.0.1713106849.0.0.0; _gat=1; __utma=232144587.1563370264.1705805803.1713054651.1713106852.12; __utmz=232144587.1713106852.12.12.utmcsr=sll.texas.gov|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=232144587.1.10.1713106852; ezproxy=XPwau6jsM7t1ukj; ezproxyl=XPwau6jsM7t1ukj; ezproxyn=XPwau6jsM7t1ukj; _gat_gtag_UA_224789_10=1; _ga_QCWE37JRKM=GS1.1.1713106847.30.1.1713106860.47.0.0; _ga=GA1.2.1563370264.1705805803'
        }


    async def get_cases(self, query:str):
        payload = {"q":f"\"{query}\"","library":[19048,19049],"jdxType":[{"type":"Cases","jdx":["TX"]},{"type":"Constitutions","jdx":["TX"]}],"jdxLibraries":"[{\"jdx\":\"U.S. Cir. Ct., D. Tex.\",\"libraries\":[19048]},{\"jdx\":\"U.S. Dist. Ct., D. Tex.\",\"libraries\":[19049]}]","selectedJurisdictions":["TX"],"skip":20,"ignoreRegex":True}

        endpoint = f"https://fc7-fastcase-com.ezproxy.sll.texas.gov:2443/searchApi/search/results"

        async with httpx.AsyncClient(headers=self.cookie, verify=False) as client:
            data = await client.post(endpoint, json=payload)

            data = data.json()
