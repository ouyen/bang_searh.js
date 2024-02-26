release: head.js dict/bang_full.js redirect.js dict/patch.yaml
	cd dict && python3 get_dict.py
	cd ..
	cat head.js dict/bang_full.js redirect.js > release.js
	sed -i "s|// @version[[:space:]]\+1.0|&`date +'%y%m%d'`|g"  release.js 

dict: dict/patch.yaml
	cd dict && python3 get_dict.py