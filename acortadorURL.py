import pyshorteners

url_largo = 'https://www.brightlabs.com.mx/cursodeprogramacionenpython'
s = pyshorteners.Shortener()
url_corto = s.tinyurl.short(url_largo)
print(url_corto)