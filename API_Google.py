from yahoo.search.news import NewsSearch
srch = NewsSearch('YahooDemo', query='kittens')
info = srch.parse_results()
info.total_results_available

info.total_results_returned

info.first_result_position

for result in info.results:
    print "'%s', from %s" % (result['Title'], result['NewsSource'])
