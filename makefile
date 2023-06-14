release: head.js dict/bang_full.js redirect.js dict/patch.yaml
	cat head.js dict/bang_full.js redirect.js > release.js

dict: dict/patch.yaml
	cd dict && python3 get_dict.py