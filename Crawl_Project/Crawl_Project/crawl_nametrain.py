urls=["https://www.artencraft.be/nl/sony-aka-cap1-statief-380412.html","https://www.artencraft.be/nl/sony-chest-mount-harness-aka-cmh1-211464.html","https://www.bol.com/nl/p/clip-head-mount/9200000054665877"]
done = []
    retailer_name={}
    for i in urls:
        domain_name = urlparse(i).netloc
        try:
            retailer_name[str(domain_name)]
        except:
            retailer_name[str(domain_name)] = domain_name
        if  i=="":
            urls.pop(urls.index(i))
        else:
            i = i + "\n"
            done.append(i)
    done_final = [done[x:x + 10] for x in range(0, len(done), 10)]
    print(done_final)
    print(retailer_name)