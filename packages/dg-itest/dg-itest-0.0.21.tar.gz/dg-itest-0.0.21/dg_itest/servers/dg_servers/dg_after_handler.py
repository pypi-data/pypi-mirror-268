#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/11 11:29
# @Author  : 杨智杰
# @Email   : yangzhijie@datagrand.com
import json
import jsonpath
from dg_itest.utils.logger import log_attach
from dg_itest.utils.diff_helper import DiffHelper
from dg_itest.utils.cache import local_cache

class DgAfterHandler:
	def __init__(self):
		pass

	# todo 断言类型需要增加，目前只支持eq(相等), co(包含), sa(存储)。
	def after(self, in_params, response):
		'''
		对接口返回值进行各种后处理操作：断言，提取值，判断包含
		in_params: 传入的参数，格式为json
		response: 接口返回的http响应
		'''
		validate = in_params.get("validate")
		expect = in_params.get('expect')
		for item in validate:
			if "sa" in item.keys():  # save临时存储，后面用例可用
				self._save(item, response)
			if "eq" in item.keys():
				self._equal(item, response, expect)
			if "co" in item.keys():
				self._contains(item, response, expect)


	def _equal(self, item, response, expect):
		'''
		item: 单个用例的入参
		response: 接口返回的http响应
		expect：用例执行的期望值
		'''
		validate_rule = item.get("eq")
		actual_result = jsonpath.jsonpath(response.json(), validate_rule)
		expect_result = jsonpath.jsonpath(expect.get('json'), validate_rule)

		if isinstance(actual_result, list) and isinstance(expect_result, list):
			actual_result = sorted(actual_result)
			expect_result = sorted(expect_result)
		log_attach(f'equal check --> validate_rule: {validate_rule} ,\nactual_result: {actual_result}\nexpect_result: {expect_result}', name='equal assert')
		assert actual_result == expect_result, '\n' + DiffHelper.diff(str(actual_result), str(expect_result))


	def _contains(self, item, response, expect):
		'''
		item: 单个用例的入参
		response: 接口返回的http响应
		expect：用例执行的期望值
		'''
		contains_rule = item.get('co')
		actual_result = jsonpath.jsonpath(response.json(), contains_rule)
		expect_result = expect.get('contains')
		log_attach(
			f'contains check --> validate_rule: {contains_rule} ,\nactual_result: {actual_result}\nexpect_result: {expect_result}',
			name='contains assert')
		assert expect_result in json.dumps(actual_result, ensure_ascii=False), f'{expect_result} not in {actual_result}'

	def _save(self, item, response):
		'''
		item: 单个用例的入参
		response: 接口返回的http响应
		'''
		sa_value = item.get("sa")
		for sa_item_key in sa_value.keys():
			sa_item_value = jsonpath.jsonpath(response.json(), sa_value.get(sa_item_key))
			assert type(sa_item_value) is list and len(sa_item_value) > 0, '\n' + '未获取到值'
			sa_item_keep_value = eval(f'{item.get("convert")}({sa_item_value[0]})') if item.get("convert") else sa_item_value[0]
			log_attach(f'local cache --> ${sa_item_key}$:{sa_item_keep_value} , cache type: {str(type(sa_item_keep_value))}', name='save local cache')
			local_cache.put(f"${sa_item_key}$", sa_item_keep_value)


	def check_status(self, in_params):
		"""
        校验接口返回状态
        由于接口存在异步执行，返回对应状态耗时较长，通过其状态校验，多次循环执行得到正确实际状态
        :return: 返回状态
        """
		status = True
		for item in in_params.get("validate"):
			if 'cs' in item.keys():
				cs_value = item.get('cs')
				for cs_item_key in cs_value.keys():
					status = status and local_cache[f"${cs_item_key}$"] == cs_value.get(cs_item_key)
		return status
