release:
	cat head.js dict/bang_full.js redirect.js > release.js

dict:
	cd dict && python3 get_dict.py