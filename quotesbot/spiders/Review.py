# -*- coding: utf-8 -*-
import scrapy
#Book


class Review(scrapy.Spider):
    name = 'review'
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
    start_urls = [
        'https://www.amazon.com/gp/product/014242417X/ref=s9_acsd_al_bw_c_x_4_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=B8H01NV732GDSJPRGQGV&pf_rd_r=B8H01NV732GDSJPRGQGV&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
        'https://www.amazon.com/gp/product/0439023521/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=B8H01NV732GDSJPRGQGV&pf_rd_r=B8H01NV732GDSJPRGQGV&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011',
        'https://www.amazon.com/gp/product/038549081X/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-7&pf_rd_r=B8H01NV732GDSJPRGQGV&pf_rd_r=B8H01NV732GDSJPRGQGV&pf_rd_t=101&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_p=304f5707-70c1-4855-8358-2c7b11a639b9&pf_rd_i=8192263011'
    ]

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
                yield {
                    'rating': rating,
                    'review_title': review_title,
                    # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
                    'review_body': ' '.join(review_body),
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
            yield {
                'rating': rating,
                'review_title': review_title,
                # 'color': review.xpath('//a[@class="a-size-mini a-link-normal a-color-secondary"]/text()').extract_first(),
                'review_body': ' '.join(review_body),
            }
        next = response.xpath(
            '//div[@id="cm_cr-pagination_bar"]/ul/li/a[contains(text(),"Next")]/@href').extract_first()
        if next is not None:
            next_page = 'https://www.amazon.com' + next
            yield scrapy.Request(next_page, callback=self.parseWithSeeAllReview)
