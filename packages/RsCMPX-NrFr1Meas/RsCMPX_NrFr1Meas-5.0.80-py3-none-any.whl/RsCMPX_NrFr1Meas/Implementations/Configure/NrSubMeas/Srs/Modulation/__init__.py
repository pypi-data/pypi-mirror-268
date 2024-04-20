from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModulationCls:
	"""Modulation commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	@property
	def ewLength(self):
		"""ewLength commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ewLength'):
			from .EwLength import EwLengthCls
			self._ewLength = EwLengthCls(self._core, self._cmd_group)
		return self._ewLength

	def get_ssymbol(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:SSYMbol \n
		Snippet: value: int = driver.configure.nrSubMeas.srs.modulation.get_ssymbol() \n
		No command help available \n
			:return: selected_symbol: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:SSYMbol?')
		return Conversions.str_to_int(response)

	def set_ssymbol(self, selected_symbol: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:SSYMbol \n
		Snippet: driver.configure.nrSubMeas.srs.modulation.set_ssymbol(selected_symbol = 1) \n
		No command help available \n
			:param selected_symbol: No help available
		"""
		param = Conversions.decimal_value_to_str(selected_symbol)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:SSYMbol {param}')

	# noinspection PyTypeChecker
	def get_ew_position(self) -> enums.LowHigh:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:EWPosition \n
		Snippet: value: enums.LowHigh = driver.configure.nrSubMeas.srs.modulation.get_ew_position() \n
		No command help available \n
			:return: evm_window_pos: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:EWPosition?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)

	def set_ew_position(self, evm_window_pos: enums.LowHigh) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:EWPosition \n
		Snippet: driver.configure.nrSubMeas.srs.modulation.set_ew_position(evm_window_pos = enums.LowHigh.HIGH) \n
		No command help available \n
			:param evm_window_pos: No help available
		"""
		param = Conversions.enum_scalar_to_str(evm_window_pos, enums.LowHigh)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:MODulation:EWPosition {param}')

	def clone(self) -> 'ModulationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModulationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
