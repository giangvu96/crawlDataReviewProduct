# -*- coding: utf-8 -*-
import scrapy
#Book


class Review(scrapy.Spider):
    name = 'review'
    start_urls = [
        'https://www.amazon.com/gp/product/B0785GSH3H/ref=s9_acsd_top_hd_bw_bBEUMd_cr_x__w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=W3TF5TMQ96MY2A2KWHSK&pf_rd_r=W3TF5TMQ96MY2A2KWHSK&pf_rd_t=101&pf_rd_p=880f6efe-1f80-5bd2-8adc-c0fe3131ecad&pf_rd_p=880f6efe-1f80-5bd2-8adc-c0fe3131ecad&pf_rd_i=165993011',
      ]
    # start_urls = ['https://www.amazon.com/s/ref=lp_7072561011_nr_n_0?fst=as%3Aoff&rh=n%3A2335752011%2Cn%3A%212335753011%2Cn%3A7072561011%2Cn%3A2407748011&bbn=7072561011&ie=UTF8&qid=1538584000&rnid=7072561011']
    # def parse(self, response):
    #     # searchResults = response.xpath('//div[@id="search-results"]')
    #     mainResults = response.xpath('//div[@id="mainResults"]')
    #     if mainResults is not None:
    #         for list in mainResults.xpath('./ul/li'):
    #             link = list.xpath('./div/div[@class="a-row a-spacing-mini"]/div[@class="a-row a-spacing-none sx-line-clamp-4"]/a/@href').extract_first()
    #             if link is not None:
    #                 yield {
    #                     'link': link
    #                 }
    #
    #         next = response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()
    #         if next is not None:
    #             next_page = 'https://www.amazon.com' + next
    #             yield scrapy.Request(next_page, callback=self.parse)
    #
    #     #     next = response.xpath('//a[contains(text(),"Next")]/@href').extract_first()
    #     #     if next is not None:
    #     #         next_page = 'https://www.amazon.com' + next
    #     #         yield scrapy.Request(next_page, callback=self.parse)

    def parse(self, response):
        see_all_review = response.xpath('//a[@id="dp-summary-see-all-reviews"]/@href').extract_first()
        if see_all_review is not None:
            url = 'https://www.amazon.com' + see_all_review
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
