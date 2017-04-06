def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

arg = ["It's very runny, sir.",
           "It's really very, VERY runny, sir."]

kw = {'naren':'Dinodaur'}

cheeseshop("Limburger", *arg, **kw)