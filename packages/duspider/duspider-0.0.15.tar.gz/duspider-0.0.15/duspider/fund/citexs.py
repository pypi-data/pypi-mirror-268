# -*- coding: utf-8 -*-
# @project: duspider
# @Author：dyz
# @date：2024/3/28 14:35
# see https://www.citexs.com/nsfc
import json
import logging
import re
import time

from du_aio_tools.rsa import make_md5
from tqdm import tqdm
from parsel import Selector
import base64
from math import ceil
from Crypto.Cipher import AES

from duspider.base import Spider
from duspider.fund.nsfc import NSFCHit

from duspider.tools import get_ua

logger = logging.getLogger(__file__)


def aes_decrypt(text, key):
    """aes 解密"""
    generator = AES.new(key.encode('utf-8'), AES.MODE_ECB)  # ECB模式无需向量iv
    decrpyt_bytes = base64.b64decode(text)
    meg = generator.decrypt(decrpyt_bytes).decode('utf-8')
    return meg[:-ord(meg[-1])]


class Citex(Spider):

    def __init__(self, cookies, key='46ED1180EEA5D5AA'):
        """
        :param cookies: 登录状态后的cookies
        """
        self.key = key  # AES ECB 解密
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'IsLimit': 'true',
            'OpenId': 'o2k1K5owZIVXcLWuWcj1jlSt3w9M',
            'Origin': 'https://www.citexs.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.citexs.com/nsfc',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Source': 'PC',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        super().__init__()
        self.cookies = cookies

        self.search_url = 'https://www.citexs.com/api/Nsfc/NsfcSearch'
        self.pr_search_url = 'https://www.citexs.com/api/Nsfc/ProjectProvinceSearch'
        self.info_url = 'https://kd.nsfc.gov.cn/api/baseQuery/conclusionProjectInfo/'
        self.size = 5
        self.sta = False
        self.gzr_top_list = (
            "面上项目",
            "青年科学基金项目",
            "地区科学基金项目",
            "国际(地区)合作与交流项目",
            "重点项目",
            "专项基金项目",
            "联合基金项目",
            "重大研究计划",
            "应急管理项目",
            "国家杰出青年科学基金",
            "优秀青年科学基金项目",
            "数学天元基金项目",
            "专项项目",
            "重大项目",
            "海外及港澳学者合作研究基金",
            "创新研究群体项目",
            "国家基础科学人才培养基金",
            "国家重大科研仪器研制项目",
            "海外或港、澳青年学者合作研究基金",
            "国际（地区）合作与交流项目",
            "国家重大科研仪器设备研制专项",
            "科学中心项目",
            "工程与材料科学",
            "生命科学"
        )
        self.pr_top_list = (
            "广东省",
            "湖南省",
            "安徽省",
            "浙江省",
            "重庆市",
            "北京市",
            "四川省",
            "湖北省",
            "上海市",
            "河南省",
            "山东省",
            "贵州省",
            "海南省",
            "广州省",
            "黑龙江省",
            "江苏省",
            "福建省",
            "辽宁省",
            "天津市",
            "江西省",
            "西藏自治区",
            "云南省",
            "陕西省",
            "内蒙古自治区",
        )

    async def post(self, url, **kwargs):
        for i in range(self.max_retry):
            try:
                time.sleep(1.5)
                resp = await self.client.post(url,
                                              timeout=self.timeout,
                                              follow_redirects=True,
                                              **kwargs)
                if '访问受限!' in resp.text:
                    time.sleep(300)
                    raise RequestError(url, err=err, retry=i)
                return resp
            except Exception as err:
                time.sleep(0.5)
                if i == self.max_retry - 1:
                    raise RequestError(url, err=err, retry=i)
        return ''

    async def parse_list(self, data_list):
        for row in data_list:
            uid: str  # 数据 id
            ratify_no: str  # 批准号
            project_name: str  # 项目名称
            ratify_no = row.get('ProjectCode', '')
            if ratify_no or row.get('Url', ''):
                uid = row.get('Url', '') if row.get('Url', '') else make_md5('citex' + ratify_no)
            else:
                name = row.get('ProjectName_cn', '') or row.get('ProjectName', '')
                uid = make_md5('citex' + name)
            start_date = row.get('StartDate') or None
            end_date = row.get('EndDate') or None
            start_date, end_date = self.new_date(start_date, end_date)
            item = NSFCHit(
                uid=uid,
                ratify_no=ratify_no,
                project_name=row.get('ProjectName_cn', '') or row.get('ProjectName', ''),
                project_category=row.get('ProjectType', ''),
                project_leader=row.get('Leader', ''),
                approval_year=row.get('YearOfApproval') or None,
                project_funding=row.get('Amount', ''),
                project_unit=row.get('Institution', ''),
                project_keyword_c=row.get('KeyWord', ''),
                project_keyword_e=row.get('EnKeyWord', ''),
                project_apply_code=row.get('Classification', ''),
                report_year=None,
                start_date=start_date,
                end_date=end_date,
                has_report=False,
                project_abstract_c=row.get('CnSummary') or '',
                project_abstract_e=row.get('Summary') or '',
                info=row,
                url=''
            )

            yield item

    def new_date(self, start, end):
        new_start = start
        new_end = end
        if start and len(start) == 4:
            new_start = f'{start}-01-01'
        if end and len(end) == 4:
            new_end = f'{end}-12-31'
        return new_start, new_end

    def all_year(self, start=2000, end=2023):
        for year in range(start, end + 1):
            yield year

    async def overseas_all(self, page=1, desc='海外基金'):
        """所有海外基金"""
        for year in self.all_year():
            js_data = {
                'Rank': 'national',
                'Query': ' ',
                'province': '',
                'institution': '',
                'leader': '',
                'sDate': f'{year}',
                'eDate': f'{year}',
                'sort': 'YearOfApproval',
                'm': page,
                'n': '12',
            }
            data_list, count = await self.post_data(self.search_url, js_data=js_data)

            if page == 1:
                async for row in self.parse_list(data_list['documents']):
                    yield row
                page = 2
            if count >= 10000:
                js_data = {
                    'Rank': 'national',
                    'Query': ' ',
                    'province': '',
                    'institution': '',
                    'leader': '',
                    'sDate': f'{year}',
                    'eDate': f'{year}',
                    'sort': 'YearOfApproval',
                    'm': page,
                    'n': '12',
                }
                data_list, count = await self.post_data(self.search_url, js_data=js_data)
                async for row in self.parse_list(data_list['documents']):
                    yield row
                s_page = 2
                async for row in self.process(js_data, count, top=top, year=year, page=s_page):
                    yield row
                data_list, count = await self.post_data(self.search_url, js_data=js_data)
            else:
                js_data = {
                    'Rank': 'national',
                    'Query': ' ',
                    'province': '',
                    'institution': '',
                    'leader': '',
                    'sDate': f'{year}',
                    'eDate': f'{year}',
                    'sort': 'YearOfApproval',
                    'm': page,
                    'n': '12',
                }
                async for row in self.process(js_data, count, desc=desc):
                    yield row

    async def all_pr(self, page=1, desc='省自然基金'):
        """地方自然科学基金"""
        for year in self.all_year(start=2018, end=2024):

            js_data = {
                'Query': '',
                'province': '',
                'institution': '',
                'leader': '',
                'sDate': f'{year}',
                'eDate': f'{year}',
                'sort': '',
                'm': page,
                'n': '12',
            }

            response = await self.post(self.pr_search_url,
                                       data=js_data,
                                       cookies=self.cookies,
                                       headers=self.headers,
                                       )
            data = response.json()
            data_str = aes_decrypt(data['messages'], key=self.key)
            data_list = json.loads(data_str)
            count = data['count']
            if page == 1:
                async for row in self.parse_list(data_list['documents']):
                    yield row
                page = 2
            if count >= 10000:

                for pr in self.pr_top_list:
                    js_data = {
                        'Query': '',
                        'province': pr,
                        'institution': '',
                        'leader': '',
                        'sDate': f'{year}',
                        'eDate': f'{year}',
                        'sort': '',
                        'm': page,
                        'n': '12',
                    }
                    data_list, count = await self.post_data(self.search_url, js_data=js_data)
                    async for row in self.parse_list(data_list['documents']):
                        yield row
                    s_page = 2
                    async for row in self.process(js_data, count, top=top, desc=desc,
                                                  url=self.pr_search_url,
                                                  page=s_page, year=year):
                        yield row

            else:
                js_data = {
                    'Query': '',
                    'province': '',
                    'institution': '',
                    'leader': '',
                    'sDate': f'{year}',
                    'eDate': f'{year}',
                    'sort': '',
                    'm': page,
                    'n': '12',
                }
                async for row in self.process(js_data, count, desc=desc, url=self.pr_search_url):
                    yield row

    async def all_gzr(self, page=1, desc='国自然'):
        """所有国自然基金"""
        for year in self.all_year(start=2020):
            js_data = {
                'Query': ' ',
                'province': '',
                'institution': '',
                'leader': '',
                'xueke[0]': ' H.医学科学部',
                'xueke[1]': '医学科学部',
                'xueke[2]': '生命科学部',
                'sDate': f'{year}',
                'eDate': f'{year}',
                'sort': '',
                'm': page,
                'n': '12',
                'isTitle': 'true',
            }
            data_list, count = await self.post_data(self.search_url, js_data=js_data)

            if page == 1:
                async for row in self.parse_list(data_list['documents']):
                    yield row
                page = 2
            if count >= 10000:
                for top in self.gzr_top_list:
                    js_data = {
                        'Query': ' ',
                        'province': '',
                        'institution': '',
                        'leader': '',
                        'Tp[0]': top,
                        'xueke[0]': ' H.医学科学部',
                        # 'xueke[1]': '医学科学部',
                        'xueke[1]': '生命科学部',
                        # 'xueke[2]': '生命科学部',
                        'sDate': f'{year}',
                        'eDate': f'{year}',
                        'sort': '',
                        'm': page,
                        'n': '12',
                        'isTitle': 'true',
                    }
                    data_list, count = await self.post_data(self.search_url, js_data=js_data)
                    async for row in self.parse_list(data_list['documents']):
                        yield row
                    s_page = 2
                    async for row in self.process(js_data, count, desc, top=top, year=year, page=s_page):
                        yield row
            else:
                js_data = {
                    'Query': ' ',
                    'province': '',
                    'institution': '',
                    'leader': '',
                    'xueke[0]': ' H.医学科学部',
                    'xueke[1]': '医学科学部',
                    'xueke[2]': '生命科学部',
                    'sDate': f'{year}',
                    'eDate': f'{year}',
                    'sort': '',
                    'm': page,
                    'n': '12',
                    'isTitle': 'true',
                }
                async for row in self.process(js_data, count, desc, year=year, page=page):
                    yield row

    async def post_data(self, url, js_data):
        response = await self.post(url,
                                   data=js_data,
                                   cookies=self.cookies,
                                   headers=self.headers,
                                   )
        data = response.json()

        data_str = aes_decrypt(data['messages'], key=self.key)
        data_list = json.loads(data_str)
        count = data['count']
        return data_list, count

    async def process(self, js_data, count, desc=None, top=None, url=None, year=None, page=None):
        nums = ceil(count / 12)
        desc = f'{desc}-{year}-{count}条-{top}'
        for page_ in tqdm(range(page, nums), desc=desc):
            if page_ >= page:
                js_data["m"] = page_
                url = url or self.search_url
                response = await self.post(url,
                                           data=js_data,
                                           cookies=self.cookies,
                                           headers=self.headers,
                                           )

                data = response.json()
                code = data.get('Code') or data.get('code')
                if str(code) != '200':
                    print(page_, code)
                data_str = aes_decrypt(data['messages'], key=self.key)
                data_list = json.loads(data_str)
                async for row in self.parse_list(data_list['documents']):
                    yield row


async def t():
    cookies = {}
    ct = Citex(cookies=cookies)
    async for row in ct.overseas_all():
        print(row)
        input('aa')


if __name__ == '__main__':
    import asyncio

    asyncio.run(t())
