from HiveWebCrawler.Crawler import WebCrawler



CrawlerToolkit = WebCrawler()

request_data = CrawlerToolkit.send_request(target_url="https://www.hurriyet.com.tr/bizeulasin/")


if not request_data["success"]:
    print(request_data["message"])
    exit(1)
    


crawled_links = CrawlerToolkit.crawl_phone_number_from_response_href(response_text=request_data["data"])


if not crawled_links["success"]:
    print(request_data["message"])
    exit(1)
    

print(crawled_links.keys())


for single_list in crawled_links["data_array"]:
    print(single_list)
