from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	def get_pc_index(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:PRACh:PCINdex \n
		Snippet: value: int = driver.configure.nrSubMeas.network.prach.get_pc_index() \n
		No command help available \n
			:return: prach_conf_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:NETWork:PRACh:PCINdex?')
		return Conversions.str_to_int(response)

	def set_pc_index(self, prach_conf_index: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:NETWork:PRACh:PCINdex \n
		Snippet: driver.configure.nrSubMeas.network.prach.set_pc_index(prach_conf_index = 1) \n
		No command help available \n
			:param prach_conf_index: No help available
		"""
		param = Conversions.decimal_value_to_str(prach_conf_index)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:NETWork:PRACh:PCINdex {param}')
