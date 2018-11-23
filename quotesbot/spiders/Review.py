# -*- coding: utf-8 -*-
import scrapy
#Book
import json

def getUrlElectronic():
    urlArray = []
    with open('urlElectronic.json') as f:
        data = json.load(f)
    # for x in data:
    #     urlArray.append(x["review"])
    for i in range(100):
        url = data[i+91]["review"].split('/dp')
        middle = '/product-reviews'
        after = '/ref=cm_cr_dp_d_hist_3?ie=UTF8&filterByStar=three_star&reviewerType=all_reviews#reviews-filter-bar'
        urlArray.append(url[0] + middle + url[1] + after )
    return urlArray

def getUrlBook():
    urlArray = []
    with open('url_100_Book_Young_Adult.json') as f:
        data = json.load(f)
    for x in data:
        url = x["review"].split('/dp')
        middle = '/product-reviews'
        after3 = '/ref=cm_cr_dp_d_hist_3?ie=UTF8&filterByStar=three_star&reviewerType=all_reviews#reviews-filter-bar'
        after2 = '/ref=cm_cr_dp_d_hist_2?ie=UTF8&filterByStar=two_star&reviewerType=all_reviews#reviews-filter-bar'
        after1 = '/ref=cm_cr_dp_d_hist_1?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews#reviews-filter-bar'
        # urlArray.append(url[0] + middle + url[1] + after2 )
        urlArray.append(url[0] + middle + url[1] + after3 )
    return urlArray

class Review(scrapy.Spider):
    name = 'review'
    # start_urls = getUrlElectronic()
    start_urls = getUrlBook()

    #review_book_01.json
    # start_urls = [
    #     'https://www.amazon.com/gp/product/0451524934/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0553380168/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0375725784/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0374531269/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0553213458/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0671894412/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/068484267X/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0385739869/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_r=RCYSA1GJ80XYA8EX0Y30&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #   ]
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

    #review_book_02.json
    # start_urls = [
    #     'https://www.amazon.com/gp/product/037570504X/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/1451626657/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0375815260/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0061124958/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_p=fc70d3c2-a39b-4dc5-8432-ecb429c303dc&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0810993139/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0441013597/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/1451673310/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0679785892/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    # ]

    # review_book_03.json
    # start_urls = [
    #     'https://www.amazon.com/gp/product/0316176494/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0061958271/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0679410430/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0307389731/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_p=36c4efe0-e91b-4e14-b48c-1e660bcfb258&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0316776963/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0312427735/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0812976533/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0393324818/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/037571457X/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0679756450/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0199535566/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0618249060/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    # ]
    # review_book_04.json
    # start_urls = [
    #     'https://www.amazon.com/gp/product/0812983580/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0345350685/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0375842209/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/1594483299/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_p=20edff09-04d3-4c05-8f94-1125395019e2&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0312421273/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0375725601/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0307594009/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    # ]

    # review_book_05.json
    # start_urls = [
    #     'https://www.amazon.com/gp/product/0140361227/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/1400052181/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0394757688/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/1400030846/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0684853949/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0061577073/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0394720245/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0312427565/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0307387895/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0743297334/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #     'https://www.amazon.com/gp/product/0618706410/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_r=CTBAF9980TE80TNNWGKH&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    # ]

    # review_book_06.json
    # start_urls = [
    #    'https://www.amazon.com/gp/product/0399226907/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #    'https://www.amazon.com/gp/product/0763622427/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #    'https://www.amazon.com/gp/product/0385474547/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #    'https://www.amazon.com/gp/product/0802135196/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #    'https://www.amazon.com/gp/product/0446310786/ref=s9_acsd_al_bw_c_x_2_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-8&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_r=3F65P73QCCJT5AN54NT3&pf_rd_t=101&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_p=cb862b66-0681-48c9-af0d-9c438ad0ed0b&pf_rd_i=8192263011',
    #     ]

    # review_book_08.json
    # start_urls = [
    #     'https://www.amazon.com/Book-Thief-Markus-Zusak/product-reviews/0375842209/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews'
    # ]

    # review_book_09.json


    # start_urls = getUrl()
    #url from 16 - 18
    # start_urls = [
    #       'https://www.amazon.com/NETGEAR-N300-Range-Extender-EX2700/product-reviews/B00L0YLRUW/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #       'https://www.amazon.com/HP-CN051AN-140-Cartridges-Officejet/product-reviews/B005BZNE2A/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #       'https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/product-reviews/B0756CYWWD/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     ]

    a=0
    # start_urls = getUrl()
    #url from 13 - 15
    # start_urls = [
    #         'https://www.amazon.com/Protector-Compatible-Tempered-Anti-Scratch-Friendly/product-reviews/B01LXZDPDR/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #         'https://www.amazon.com/amFilm-iPhone-Screen-Protector-Tempered/product-reviews/B01415QHYW/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #         'https://www.amazon.com/AmazonBasics-Everyday-Alkaline-Batteries-8-Pack/product-reviews/B00MH4QM1S/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #    ]

    #url from 7 - 12
    # start_urls = [
    #     'https://www.amazon.com/Roku-Express-More-Powerful-Streaming/product-reviews/B075XN1NZC/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Intel-i7-8700K-Desktop-Processor-Unlocked/product-reviews/B07598VZR8/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Samsung-MicroSD-Adapter-MB-ME128GA-AM/product-reviews/B06XWZWYVP/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Brother-Cartridge-TN660-Replacement-Replenishment/product-reviews/B00LJO8EQS/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Elements-Portable-External-Drive-WDBU6Y0020BBK-WESN/product-reviews/B06W55K9N6/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/PlayStation-Pro-1TB-Console-Redemption-4/product-reviews/B07HHWJMGF/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    # ]


    #url from 1 - 6
    # start_urls = [
    #     'https://www.amazon.com/Samsung-500GB-Internal-MZ-76E500B-AM/product-reviews/B0781Z7Y3S/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Maxboost-Protector-Tempered-Advanced-Accurate/product-reviews/B073DLZWX7/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Sandisk-Ultra-128GB-Micro-Adapter/product-reviews/B073JYC4XM/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Nintendo-Switch-Neon-Red-Blue-Joy/product-reviews/B01MUAGZ49/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/Google-WiFi-system-3-Pack-replacement/product-reviews/B01MAW2294/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    #     'https://www.amazon.com/AmazonBasics-Nylon-Braided-Lightning-Cable/product-reviews/B01F9RH0R4/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews',
    # ]

    #url 0
    # start_urls = ['https://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-Count/product-reviews/B00MNV8E0C/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews123']

    # def parse(self, response):
    #     see_all_review = response.xpath('//a[@id="dp-summary-see-all-reviews"]/@href').extract_first()
    #     if see_all_review is not None:
    #         url = 'https://www.amazon.com' + see_all_review
    #         yield scrapy.Request(url, callback=self.parseWithSeeAllReview)
    #     else:
    #         for review in response.xpath('//div[@id="cm_cr-review_list"]/div[@class="a-section review"]'):
    #             rating = review.xpath('./div/div/a/i/span[@class="a-icon-alt"]/text()').extract_first().split(' ')[0]
    #             review_title = review.xpath(
    #                 './div/div/a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()').extract_first()
    #             review_body = review.xpath('./div/div/span[@class="a-size-base review-text"]/text()').extract()
    #             yield {
    #                 'rating': rating,
    #                 'review_title': review_title,
    #                 # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
    #                 'review_body': ' '.join(review_body),
    #             }
    #         next = response.xpath('//div[@id="cm_cr-pagination_bar"]/ul/li/a[contains(text(),"Next")]/@href').extract_first()
    #         print(next)
    #         if next is not None:
    #             next_page = 'https://www.amazon.com' + next
    #             yield scrapy.Request(next_page, callback=self.parseWithSeeAllReview)
    #
    # def parseWithSeeAllReview(self, response):
    #     for review in response.xpath('//div[@id="cm_cr-review_list"]/div[@class="a-section review"]'):
    #         rating = review.xpath('./div/div/a/i/span[@class="a-icon-alt"]/text()').extract_first().split(' ')[0]
    #         review_title = review.xpath('./div/div/a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()').extract_first()
    #         review_body = review.xpath('./div/div/span[@class="a-size-base review-text"]/text()').extract()
    #         yield {
    #             'rating': rating,
    #             'review_title': review_title,
    #             # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
    #             'review_body': ' '.join(review_body),
    #         }
    #     next = response.xpath(
    #         '//div[@id="cm_cr-pagination_bar"]/ul/li/a[contains(text(),"Next")]/@href').extract_first()
    #     if next is not None:
    #         next_page = 'https://www.amazon.com' + next
    #         yield scrapy.Request(next_page, callback=self.parseWithSeeAllReview)
    b=3
    # url from 29 - 58 critical
    # start_urls = [
    #     'https://www.amazon.com/Energizer-Batteries-Battery-Alkaline-E91DP2-24/product-reviews/B079GXSFPB/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/AmazonBasics-High-Speed-HDMI-Cable-1-Pack/product-reviews/B014I8SSD0/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Wireless-Qi-Certified-Charging-Compatible-Qi-Enabled/product-reviews/B079KZ49PJ/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Energizer-Batteries-Battery-Alkaline-E91BP-24/product-reviews/B004U429AQ/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Fujitsu-ScanSnap-iX500-Duplex-Scanner/product-reviews/B01G3JYVYM/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-Tri-color-Original-Cartridges-Officejet/product-reviews/B00WR23VRI/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-23-8-inch-Adjustment-Speakers-VH240a/product-reviews/B072M34RQC/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-Cartridge-Tri-Color-Cartridges-CR259FN/product-reviews/B003YT6RNS/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Logitech-Widescreen-Calling-Recording-Desktop/product-reviews/B006JH8T3S/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/SanDisk-Ultra-UHS-I-Memory-SDSDUNC-064G-GN6IN/product-reviews/B0143IIP4W/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-Original-Cartridge-F6U19AN-OfficeJet/product-reviews/B01B6QGJ42/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/GoPro-HERO7-Black-Waterproof-Streaming-Stabilization/product-reviews/B07GDGZCCH/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Roku-Streaming-Stick-Player-Wireless/product-reviews/B075XLWML4/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Wyze-Indoor-Wireless-Camera-Vision/product-reviews/B076H3SRXG/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Scotch-Thermal-Laminating-100-Pack-TP3854-100/product-reviews/B007VBXB48/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-N9K27AN-140-Original-Cartridges/product-reviews/B01AV8PPOQ/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Acer-Aspire-i3-8130U-Memory-E5-576-392H/product-reviews/B079TGL2BZ/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-CN045AN-140-Cartridge-Officejet/product-reviews/B005BZNEMK/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-Original-Cartridge-F6U64AN-OfficeJet/product-reviews/B00WJDWGA8/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/AmazonBasics-Everyday-Alkaline-Batteries-12-Pack/product-reviews/B00MH4QKP6/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-Original-Cartridge-C2P05AN-Officejet/product-reviews/B00L1G7LBI/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Enhanced-Splashproof-Portable-Bluetooth-Radiator/product-reviews/B010OYASRG/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Nintendo-Switch-Gray-Joy/product-reviews/B01LTHP2ZK/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/AmazonBasics-Everyday-Alkaline-Batteries-12-Pack/product-reviews/B00MH4QI26/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/PopSockets-Collapsible-Stand-Phones-Tablets/product-reviews/B00UY1YTGG/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Magma-4/product-reviews/B01MD19OI2/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/NETGEAR-R6700-Nighthawk-Gigabit-Ethernet/product-reviews/B00R2AZLD2/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/TP-Link-Extender-External-Antennas-TL-WA855RE/product-reviews/B0195Y0A42/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/AmazonBasics-6-Sheet-Cross-Cut-Credit-Shredder/product-reviews/B00HFJWKWK/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/AMD-Ryzen-Processor-Wraith-Cooler/product-reviews/B07B428M7F/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Logitech-M510-Wireless-Computer-Mouse/product-reviews/B003NR57BY/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Brother-Monochrome-HL-L2350DW-Two-Sided-Replenishment/product-reviews/B0763WDSYZ/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Nulaxy-Wireless-Bluetooth-Transmitter-Smartphones/product-reviews/B018E0I01I/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Texas-Instruments-TI-84-Graphing-Calculator/product-reviews/B00TFYYWQA/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Samsung-T5-Portable-SSD-MU-PA500B/product-reviews/B073GZBT36/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Corsair-Vengeance-3000MHz-Desktop-Memory/product-reviews/B0134EW7G8/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/VicTsing-Wireless-Portable-Receiver-Adjustable/product-reviews/B013WC0P2A/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    # ]

    # url from 59 - 88 critical
    c=4
    #from 59 - 90
    # start_urls = [
    #     'https://www.amazon.com/Panasonic-Headphones-RP-HJE120-K-Ergonomic-Comfort-Fit/product-reviews/B003EM8008/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/DualShock-Wireless-Controller-PlayStation-Black-4/product-reviews/B01LWVX2RG/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Belkin-BE112230-08-12-Outlet-Power-Protector/product-reviews/B000J2EN4S/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Microsoft-PD9-00003-Surface-Dock/product-reviews/B0163HP38W/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Magnetic-WizGear-Universal-Swift-Snap-Technology/product-reviews/B01G0X56YU/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Sceptre-E248W-19203R-Monitor-Speakers-Metallic/product-reviews/B0773ZY26F/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Nintendo-Joy-Neon-Pink-Green-switch/product-reviews/B078GZM4H8/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Compatible-Screen-Protector-Tempered-Anti-scratch/product-reviews/B07GVCV1CL/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Besiva-Braided-Charging-Syncing-Compatible/product-reviews/B07D71GJ1M/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Trianium-Protector-Designed-Tempered-Alignment/product-reviews/B073TVN87X/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Brother-Cartridge-TN760-Replacement-Replenishment/product-reviews/B075X6C5ZW/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/AmazonBasics-High-Capacity-Rechargeable-Batteries-Pre-charged/product-reviews/B00HZV9WTM/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-Tri-color-Cartridge-F6U63AN-Officejet/product-reviews/B00WJDWG3A/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Sony-WH1000XM3-Canceling-Headphones-WH-1000XM3/product-reviews/B07G4MNFS1/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/AmazonBasics-Letter-Laminating-11-5in-100-pack/product-reviews/B00BWU3HNY/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Roku-Ultra-Streaming-Enhanced-Headphone/product-reviews/B075XMZMWY/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Apple-MQD22LL-A-TV-4K/product-reviews/B075NCMLYL/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Spigen-Ultra-Hybrid-Designed-iPhone/product-reviews/B07GTCC5X2/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Fitbit-Versa-Smart-Aluminium-Included/product-reviews/B07B48SQGT/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Intel-i5-8400-Desktop-Processor-Cores/product-reviews/B0759FGJ3Q/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Blue-NAND-500GB-SSD-WDS500G2B0A/product-reviews/B073SBZ8YH/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Anker-Qi-Certified-Ultra-Slim-Compatible-PowerPort/product-reviews/B0756Z8X82/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Sabrent-4-Port-Individual-Switches-HB-UM43/product-reviews/B00JX1ZS5O/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-CF226A-Original-Cartridge-Laserjet/product-reviews/B015H31W60/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/HP-OfficeJet-8710-Wireless-Printing/product-reviews/B01CJNMRG0/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Energizer-Batteries-Battery-Alkaline-E92DP2-24/product-reviews/B079GS4YQS/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Logitech-910-001799-Wireless-Trackball-M570/product-reviews/B0043T7FXE/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #     'https://www.amazon.com/Logitech-MK320-Wireless-Desktop-Keyboard/product-reviews/B003VAGXZC/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews',
    #      ]

    d=5
    # from 91 - 191

    def parse(self, response):
        see_all_review = response.xpath('//a[@id="dp-summary-see-all-reviews"]/@href').extract_first()
        if see_all_review is not None:
            url = 'https://www.amazon.com' + see_all_review
            yield scrapy.Request(url, callback=self.parseWithSeeAllReview)
        else:
            for review in response.xpath('//div[@id="cm_cr-review_list"]/div[@class="a-section review"]'):
                rating = review.xpath('./div/div/a/i/span[@class="a-icon-alt"]/text()').extract_first().split(' ')[0]
                review_title = review.xpath(
                    './div/div/a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()').extract_first()
                review_body = review.xpath('./div/div/span[@class="a-size-base review-text"]/text()').extract()
                review_helpful = review.xpath('./div/div/div/span/div/span[@data-hook="helpful-vote-statement"]/text()').extract_first()
                yield {
                    'rating': rating,
                    'review_title': review_title,
                    # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
                    'review_body': ' '.join(review_body),
                    'review_helpful': review_helpful and (review_helpful.split(' ')[0] =="One" and "1" or review_helpful.split(' ')[0]) or "0"
                }
            next = response.xpath('//div[@id="cm_cr-pagination_bar"]/ul/li/a[contains(text(),"Next")]/@href').extract_first()
            print(next)
            if next is not None:
                next_page = 'https://www.amazon.com' + next
                yield scrapy.Request(next_page, callback=self.parseWithSeeAllReview)

    def parseWithSeeAllReview(self, response):
        for review in response.xpath('//div[@id="cm_cr-review_list"]/div[@class="a-section review"]'):
            rating = review.xpath('./div/div/a/i/span[@class="a-icon-alt"]/text()').extract_first().split(' ')[0]
            review_title = review.xpath('./div/div/a[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()').extract_first()
            review_body = review.xpath('./div/div/span[@class="a-size-base review-text"]/text()').extract()
            review_helpful = review.xpath(
                './div/div/div/span/div/span[@data-hook="helpful-vote-statement"]/text()').extract_first()
            yield {
                'rating': rating,
                'review_title': review_title,
                # # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
                'review_body': ' '.join(review_body),
                'review_helpful': review_helpful and (
                            review_helpful.split(' ')[0] == "One" and "1" or review_helpful.split(' ')[0]) or "0"
            }
        next = response.xpath(
            '//div[@id="cm_cr-pagination_bar"]/ul/li/a[contains(text(),"Next")]/@href').extract_first()
        if next is not None:
            next_page = 'https://www.amazon.com' + next
            yield scrapy.Request(next_page, callback=self.parseWithSeeAllReview)
