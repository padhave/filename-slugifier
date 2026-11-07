import re, sys, unicodedata
text = unicodedata.normalize("NFKD", " ".join(sys.argv[1:])).encode("ascii", "ignore").decode()
print(re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-"))
