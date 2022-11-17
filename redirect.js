
function redirect() {
    const url = new URL(location.href)
    const params = new URLSearchParams(url.search)
    const query = params.get('q')
    if (query === null) return 
    const queryArray = query.split(' ')
    let foundMatchingBang = false
    let newSearchURL = ''
    const string = queryArray.filter((word, index) => {
        if (word[0] === '!' && lookup[word.slice(1)] !== undefined && !foundMatchingBang) {
            newSearchURL = lookup[word.slice(1)]
            foundMatchingBang = true
            return false
        }
        if (word === '') {
            return false
        }
        return true
    }).join(' ')

    if (foundMatchingBang) {
            location.assign(newSearchURL.replace('{{{s}}}', encodeURIComponent(string)))
    } 
}

redirect()