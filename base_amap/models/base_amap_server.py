# -*- coding: utf-8 -*-
# Copyright(c): 2019 Freshoo (<www.freshoo.cn>)

import requests
import logging

from odoo import fields, models, api, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class AmapService(models.AbstractModel):
    """ Abstract class used to call Amap Service. """
    _name = "base.amap.server"
    _description = "Amap Service"

    @api.model
    def _get_api_key(self):
        return self.env['ir.config_parameter'].sudo().get_param('base_amap.amap_api_key', '')

    def _call_amap_district(self, keyword, subdistrict='3'):
        key = self._get_api_key()
        url = "https://restapi.amap.com/v3/config/district?keywords=%s&subdistrict=%s&key=%s" % (keyword, subdistrict, key)
        try:
            result = requests.get(url).json()
            _logger.info('amap district service called: ' + str(keyword))
            if result.get('infocode') != '10000':
                _logger.warning('amap district service: ' + str(result.get('info', 'Error!')))
            return result
        except requests.exceptions.ConnectionError as e:
            _logger.warning("Connection Error: " + str(e))
        except requests.exceptions.Timeout as e:
            _logger.warning("Timeout: " + str(e))
        except Exception as e:
            _logger.warning("amap district service request failed: " + str(e))
        return {}

    def _call_amap_geocode(self, addr, city=None):
        """
        :param addr: Address string passed to API
        :param city: city name or city adcode
        :return: (latitude, longitude) or None if not found
        """
        # TODO
        # # 地理编码
        # url = "https://restapi.amap.com/v3/geocode/geo?address=%s&city=%s&output=JSON&key=%s"
        # # 逆地理编码
        # url = "https://restapi.amap.com/v3/geocode/regeo?output=JSON&location=%s&key=%s&radius=1000&extensions=all"
        return None

    def _call_amap_ip(self, ip):
        """
        :param ip: ip address string passed to API
        :return: (latitude, longitude) or None if not found
        """
        # TODO
        # # 将IP信息转换为地理位置信息
        # url = "https://restapi.amap.com/v3/ip?ip=%s&output=JSON&key=%s" % (ip, key)
        return None

    def _call_amap_weather(self):
        # TODO
        # # 天气查询
        # url = "https://restapi.amap.com/v3/weather/weatherInfo?city=%s&key=%s" % (city_key, key)
        return None

    def _call_amap_coordinate(self):
        # TODO
        # # 将非高德坐标转换为高德坐标
        # coordsys = 'gps'
        # url = "https://restapi.amap.com/v3/assistant/coordinate/convert?locations=%s&coordsys=%s&output=JSON&key=%s"
        return None

    def _call_amap_inputtips(self):
        # TODO
        # #  输入提示
        # url = "https://restapi.amap.com/v3/assistant/inputtips?output=JSON&city=%s&keywords=%s&key=%s"
        return None

    def _call_amap_poi_place(self):
        # TODO
        # # text: 关键字搜索
        # url = "https://restapi.amap.com/v3/place/text?keywords=北京大学&city=beijing&output=JSON&offset=20&page=1&key=%s&extensions=all"
        # # around: 周边搜索
        # url = "https://restapi.amap.com/v3/place/around?key=%s&location=116.473168,39.993015&radius=10000&types=011100"
        # # polygon: 多边形搜索
        # url = "https://restapi.amap.com/v3/place/polygon?polygon=116.460988,40.006919|116.48231,40.007381|116.47516,39.99713|116.472596,39.985227|116.45669,39.984989|116.460988,40.006919&keywords=kfc&output=JSON&key=%s"
        # # detail: 兴趣点ID查询
        # url = "https://restapi.amap.com/v3/place/detail?id=B0FFFAB6J2&output=JSON&key=%s"
        return None
