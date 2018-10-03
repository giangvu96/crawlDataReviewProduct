# -*- coding: utf-8 -*-
import scrapy
#Book
class Review(scrapy.Spider):
    name = 'review'
    # start_urls = ['https://www.amazon.com/Office-Style-Powered-Desktop-Calculator/product-reviews/B00J1VB2WY/ref=cm_cr_getr_d_paging_btm_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1',
    #               'https://www.amazon.com/Differential-Equations-Scientists-Engineers-Mathematics-ebook/product-reviews/B008TVLUTW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber=1']

    start_urls = ['https://www.amazon.com/Know-Why-Caged-Bird-Sings/dp/0345514408/ref=lp_45_1_1?s=books&ie=UTF8&qid=1538571867&sr=1-1']

    def parse(self, response):
        see_all_review = response.xpath('//a[@id="dp-summary-see-all-reviews"]')
        if see_all_review is not None:
            url = 'https://www.amazon.com' + see_all_review.xpath('./@href').extract_first()
            yield scrapy.Request(url, callback=self.parseWithSeeAllReview)
        else:
            for review in response.xpath('//div[@id="cm_cr-review_list"]/div[@class="a-section review"]'):
                yield {
                    'rating': review.xpath('./div/div/a/i/span[@class="a-icon-alt"]/text()').extract_first().split(' ')[
                        0],
                    'review_title': review.xpath(
                        './div/div/a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()').extract_first(),
                    # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
                    'review_body': review.xpath(
                        './div/div/span[@class="a-size-base review-text"]/text()').extract_first(),
                }
            next = response.xpath('//a[contains(text(),"Next")]/@href').extract_first()
            if next is not None:
                next_page = 'https://www.amazon.com' + next
                yield scrapy.Request(next_page, callback=self.parse)

    def parseWithSeeAllReview(self, response):
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
            yield scrapy.Request(next_page, callback=self.parseWithSeeAllReview)
