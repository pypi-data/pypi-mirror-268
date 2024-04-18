from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.Utilities import trim_str_response
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DescriptionCls:
	"""Description commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("description", core, parent)

	def get(self, product_type: enums.ProductType = None, validity: enums.ValidityScope = None, scope: enums.ValidityScopeB = None, instrument_no: float = None) -> str:
		"""SCPI: SYSTem:BASE:OPTion:DESCription \n
		Snippet: value: str = driver.system.base.option.description.get(product_type = enums.ProductType.ALL, validity = enums.ValidityScope.ALL, scope = enums.ValidityScopeB.INSTrument, instrument_no = 1.0) \n
		No command help available \n
			:param product_type: No help available
			:param validity: No help available
			:param scope: No help available
			:param instrument_no: No help available
			:return: option_list: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('product_type', product_type, DataType.Enum, enums.ProductType, is_optional=True), ArgSingle('validity', validity, DataType.Enum, enums.ValidityScope, is_optional=True), ArgSingle('scope', scope, DataType.Enum, enums.ValidityScopeB, is_optional=True), ArgSingle('instrument_no', instrument_no, DataType.Float, None, is_optional=True))
		response = self._core.io.query_str(f'SYSTem:BASE:OPTion:DESCription? {param}'.rstrip())
		return trim_str_response(response)
