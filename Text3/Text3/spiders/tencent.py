import scrapy
from Text3.items import Text3Item


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = []
    start_urls = [
        'https://careers.tencent.com/tencentcareer/api/post/Query?&pageIndex={}&keyword=%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE&pageSize=10&language=zh-cn&area=cn'.format(
            i) for i in range(5 + 1)]

    def start_requests(self):
        cookies = 'BIDUPSID=06A17A73F8F44DEC3E44B1EC84FD6302; PSTM=1627654483; __yjs_duid=1_7a84e79fa43f16459243d02e1d7e8b5c1627825360188; bdshare_firstime=1629703094461; H_WISE_SIDS=107317_110085_127969_179347_181126_181588_182246_182273_182530_183031_183328_184010_184441_185268_185635_185650_186317_186716_186840_186896_187346_187433_187819_187877_188182_188452_188844_188873_188997_189091_189422_189679_189715_189732_189755_190034_190114_190152_190474_190510_190680_190681_190756_190779_190804_190863_191051_191244_191359_191419_191475_191503_191598_191640_191809_192132_192264_192275_192408_192875_192905_192957_193010_193043_193179_193194_193283_193320_193492_193516_193701_193755_194122_194519_194670; BAIDUID=DEE38E821D1227538434B7B2EA6841DB:FG=1; MCITY=-131%3A; H_PS_PSSID=35104_35762_34584_35491_35872_35245_35541_35319_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=8-KOJeC62xCDv66DLwIVtWM5itn-wpTTH6aoz8VLlaqDYpQCBNvREG0PKM8g0KubRDmsogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=fRPD_Dt5f-5_jJ7kqtbSMttfqx6betJyaR3rblRvWJ5TMCoGylbEDh0vL4rv0b3UBRT0VnRVJMc8ShPC-tnGyMIpBPTi0bvdLDoehq6c3l02Vboae-t2yT3DebotqPRMW20jWl7mWPLWsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCKD5vQjHKHt6nQ26TOLRK8MnbtKROkep7H0M4pbt-qJj33220ebqbPBJ_hfM3EjtrqyPIDyGbnBT5Kab5gslbu2qciKtOF5t8M2tCkQN3TWRkO5bRiLRo2HxjtDn3oyT3VXp0n5G7ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJujVItatD_hbnRY5J7hbDCbbMDX5-CsQN5A2hcH0KLKMbncyTbCQMDNXHrJLMut2CTiBJ6FtMb1MRjveq-VQhIqyRALb-Tt5nn8Wq5TtUJYJKnTDMRh-R3D0fjyKMnitIj9-pnKfpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDT8Wj6O0jHusKbQKaDQ036rh-6rjDnCr055rXUI8LNDH2P7QLDcaKp4XQRRMSpCGMtov-qKiMRO7ttoyLaQB-DJGyUjMfR3RQjrNbML1Db0tKjvMtg3t2xQ-blToepvoD-cc3MkBe-jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbAj_IKXtDK3jt-kKRo_-4kyqlOybTPOHm39aJ5nJDoWEpbCj6jUXb-P3lOUW6Q0bI_LL-JmQpP-HJ7uehjdh-_LQbrjQxJGBjcNKl0MLpvYbb0xynoD0x0DKUnMBMPjamOnaPLy3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XjjbbjNoP; st_key_id=17; USER_JUMP=-1; video_bubble0=1; BDSFRCVID_BFESS=8-KOJeC62xCDv66DLwIVtWM5itn-wpTTH6aoz8VLlaqDYpQCBNvREG0PKM8g0KubRDmsogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=fRPD_Dt5f-5_jJ7kqtbSMttfqx6betJyaR3rblRvWJ5TMCoGylbEDh0vL4rv0b3UBRT0VnRVJMc8ShPC-tnGyMIpBPTi0bvdLDoehq6c3l02Vboae-t2yT3DebotqPRMW20jWl7mWPLWsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCKD5vQjHKHt6nQ26TOLRK8MnbtKROkep7H0M4pbt-qJj33220ebqbPBJ_hfM3EjtrqyPIDyGbnBT5Kab5gslbu2qciKtOF5t8M2tCkQN3TWRkO5bRiLRo2HxjtDn3oyT3VXp0n5G7ly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJPKtfJujVItatD_hbnRY5J7hbDCbbMDX5-CsQN5A2hcH0KLKMbncyTbCQMDNXHrJLMut2CTiBJ6FtMb1MRjveq-VQhIqyRALb-Tt5nn8Wq5TtUJYJKnTDMRh-R3D0fjyKMnitIj9-pnKfpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn02eCKuDT8Wj6O0jHusKbQKaDQ036rh-6rjDnCr055rXUI8LNDH2P7QLDcaKp4XQRRMSpCGMtov-qKiMRO7ttoyLaQB-DJGyUjMfR3RQjrNbML1Db0tKjvMtg3t2xQ-blToepvoD-cc3MkBe-jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbAj_IKXtDK3jt-kKRo_-4kyqlOybTPOHm39aJ5nJDoWEpbCj6jUXb-P3lOUW6Q0bI_LL-JmQpP-HJ7uehjdh-_LQbrjQxJGBjcNKl0MLpvYbb0xynoD0x0DKUnMBMPjamOnaPLy3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XjjbbjNoP; delPer=0; PSINO=2; ariaDefaultTheme=default; BAIDU_WISE_UID=wapp_1645426488214_567; ariaFixed=true; wise_device=0; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1645426580; ariaReadtype=1; ariaoldFixedStatus=false; ariaStatus=false; BAIDUID_BFESS=025D8EC593C9A75C8A0C6362CA800D33:FG=1; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1645432773; BA_HECTOR=al84al85a4aha52goq1h16kmo0r; tb_as_data=95b40d3a84d10b7bb08f974c85cd53b2b42e8c730ea563b9774287b01b4e2cd94c283762a6500f642b72f6578480335ed83afa35a5d1f3b7b5d6dc4bfdae184e6c1c7856d143b7ca591c0a1136c5e13e9d79e26abdea56884fe8323908116cb24918e7b197330d859635a0d6b5b552e8; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1645434546,1645434553,1645434682,1645434843; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1645434843; ab_sr=1.0.1_ZmQyMDBiYzMyMWI3ZDVlYjNkODcwZTA5ZmE5MTUxMmI1Njg0ZmY1MGVmNWNiM2JmNzQxMDE2Yjc1YWVjNDk2M2U1M2MzMmMzYzRhODNiYTM2MTBiZTFmZjQ1YzU1NGQzMTcyYjA4YTMxMWUzYmVhNWU4NTE1YTI5NWI2MDUxZTMxOTliMGQ2NDYwZjgwMzVkNGQzYzM2NGZmZWRiZjA0MA==; st_data=1bfc59fe3bcc810224228c458e5fd922e081727c907635cd04f15082bc2c4d1ff8fe40a686813bbf49f7e9a6d93cbc748ded226c2558c852cc90790170bd38e4f3a75dd9620ae0b5d2d4cd4b5702c46a83d1cb7f7d8288cdac2fdd781c145043; st_sign=139cc7ad'
        # 使用字典推导式
        cookies_dict = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookies.split("; ")}
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dict
        )

    def parse(self, response):
        rets = response.json()['Data']['Posts']
        for ret in rets:
            item = Text3Item()
            item["RecruitPostName"] = ret['RecruitPostName']
            item["CategoryName"] = ret['CategoryName']
            item["CountryName"] = ret['CountryName']
            item["LocationName"] = ret['LocationName']
            PostURL = ret['PostURL'].split("?")[-1]
            url_detail = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?&" + PostURL + "&language=zh-cn"
            item["PostURL"] = url_detail
            yield scrapy.Request(
                item['PostURL'],
                callback=self.parse_detail,
                meta={"item": item}
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["LastUpdateTime"] = response.json()['Data']['LastUpdateTime']
        yield item
