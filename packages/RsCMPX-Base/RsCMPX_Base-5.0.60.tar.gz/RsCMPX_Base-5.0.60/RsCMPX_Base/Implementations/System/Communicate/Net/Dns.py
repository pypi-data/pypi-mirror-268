from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DnsCls:
	"""Dns commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dns", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:NET:DNS:ENABle \n
		Snippet: value: bool = driver.system.communicate.net.dns.get_enable() \n
		No command help available \n
			:return: dns_enable: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NET:DNS:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, dns_enable: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:NET:DNS:ENABle \n
		Snippet: driver.system.communicate.net.dns.set_enable(dns_enable = False) \n
		No command help available \n
			:param dns_enable: No help available
		"""
		param = Conversions.bool_to_str(dns_enable)
		self._core.io.write(f'SYSTem:COMMunicate:NET:DNS:ENABle {param}')

	def get_value(self) -> List[str]:
		"""SCPI: SYSTem:COMMunicate:NET:DNS \n
		Snippet: value: List[str] = driver.system.communicate.net.dns.get_value() \n
		Manually defines the DNS server IPv4 addresses to be used. A query returns the defined DNS addresses, irrespective of
		whether they have been specified manually or via DHCP. \n
			:return: ip_addresses: No help available
		"""
		response = self._core.io.query_str('SYSTem:COMMunicate:NET:DNS?')
		return Conversions.str_to_str_list(response)

	def set_value(self, ip_addresses: List[str]) -> None:
		"""SCPI: SYSTem:COMMunicate:NET:DNS \n
		Snippet: driver.system.communicate.net.dns.set_value(ip_addresses = ['abc1', 'abc2', 'abc3']) \n
		Manually defines the DNS server IPv4 addresses to be used. A query returns the defined DNS addresses, irrespective of
		whether they have been specified manually or via DHCP. \n
			:param ip_addresses: DNS server IPv4 addresses consisting of four blocks separated by dots. Several strings separated by commas can be entered or several addresses separated by commas can be included in one string.
		"""
		param = Conversions.list_to_csv_quoted_str(ip_addresses)
		self._core.io.write(f'SYSTem:COMMunicate:NET:DNS {param}')
