# -*- coding: utf-8 -*-
import scrapy

class Review(scrapy.Spider):
    name = 'review'
    start_urls = ['https://www.amazon.com/Office-Style-Powered-Desktop-Calculator/product-reviews/B00J1VB2WY/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

    def parse(self, response):
        for review in response.xpath('//div[@id="cm_cr-review_list"]/div[@class="a-section review"]'):
            yield {
                'rating': review.xpath('./div/div/a/i/span[@class="a-icon-alt"]/text()').extract_first().split(' ')[0],
                'review_title': review.xpath('./div/div/a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()').extract_first(),
                # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
                'review_body': review.xpath('./div/div/span[@class="a-size-base review-text"]/text()').extract_first(),
            }
        next = response.xpath('//a[contains(text(),"Next")]/@href').extract_first()
        if next is not None:
            next_page = 'https://www.amazon.com' + next
            yield scrapy.Request(next_page, callback=self.parse)

    # def parse2(self, response):
    #     for quote in response.xpath('//div[@class="review-container"]'):
    #         yield {
    #             'noQuotes': quote.xpath('.//span[@class="noQuotes"]/text()').extract_first(),
    #             'partial_entry': quote.xpath('.//p[@class="partial_entry"]/text()').extract_first(),
    #         }
        # next_page_xxx = response.xpath(
        #     '//div[@class="listContainer hide-more-mobile"]/div[@class="mobile-more"]/div[@class="prw_rup prw_common_responsive_pagination"]/div/a[2]/@href').extract_first()
        # if next_page_xxx is not None:
        #     next_page = 'https://www.tripadvisor.com' + next_page_xxx
        #     yield scrapy.Request(next_page_xxx, callback=self.parse)
        # else:
        #     self.driver.close()

    # def parse(self, response):
    #     yield {
    #         'more': response.xpath('//div[@class="review-container"]/div/div/div/div/div[@class="prw_rup prw_reviews_text_summary_hsx"]/div/p/span[contains(text(),"More")]/@class').extract_first(),
    #     }
        # for quote in response.xpath('//div[@class="review-container"]'):
        #     yield {
        #         'noQuotes': quote.xpath('.//span[@class="noQuotes"]/text()').extract_first(),
        #         'partial_entry': quote.xpath('.//p[@class="partial_entry"]/text()').extract_first(),
        #     }
        # next_page = response.xpath('//div[@class="listContainer hide-more-mobile"]/div[@class="mobile-more"]/div[@class="prw_rup prw_common_responsive_pagination"]/div/a[2]/@href').extract_first()
        # if next_page is not None:
        #     next_page = 'https://www.tripadvisor.com' + next_page
        #     yield scrapy.Request(next_page, callback=self.parse)
