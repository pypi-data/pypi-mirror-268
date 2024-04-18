from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnitCls:
	"""Unit commands group definition. 13 total commands, 0 Subgroups, 13 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	# noinspection PyTypeChecker
	def get_conductance(self) -> enums.DefaultUnitConductance:
		"""SCPI: UNIT:CONDuctance \n
		Snippet: value: enums.DefaultUnitConductance = driver.unit.get_conductance() \n
		No command help available \n
			:return: default_unit_conductance: No help available
		"""
		response = self._core.io.query_str('UNIT:CONDuctance?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitConductance)

	def set_conductance(self, default_unit_conductance: enums.DefaultUnitConductance) -> None:
		"""SCPI: UNIT:CONDuctance \n
		Snippet: driver.unit.set_conductance(default_unit_conductance = enums.DefaultUnitConductance.ASIE) \n
		No command help available \n
			:param default_unit_conductance: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_conductance, enums.DefaultUnitConductance)
		self._core.io.write(f'UNIT:CONDuctance {param}')

	# noinspection PyTypeChecker
	def get_charge(self) -> enums.DefaultUnitCharge:
		"""SCPI: UNIT:CHARge \n
		Snippet: value: enums.DefaultUnitCharge = driver.unit.get_charge() \n
		No command help available \n
			:return: default_unit_charge: No help available
		"""
		response = self._core.io.query_str('UNIT:CHARge?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitCharge)

	def set_charge(self, default_unit_charge: enums.DefaultUnitCharge) -> None:
		"""SCPI: UNIT:CHARge \n
		Snippet: driver.unit.set_charge(default_unit_charge = enums.DefaultUnitCharge.AC) \n
		No command help available \n
			:param default_unit_charge: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_charge, enums.DefaultUnitCharge)
		self._core.io.write(f'UNIT:CHARge {param}')

	# noinspection PyTypeChecker
	def get_capacity(self) -> enums.DefaultUnitCapacity:
		"""SCPI: UNIT:CAPacity \n
		Snippet: value: enums.DefaultUnitCapacity = driver.unit.get_capacity() \n
		No command help available \n
			:return: default_unit_capacity: No help available
		"""
		response = self._core.io.query_str('UNIT:CAPacity?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitCapacity)

	def set_capacity(self, default_unit_capacity: enums.DefaultUnitCapacity) -> None:
		"""SCPI: UNIT:CAPacity \n
		Snippet: driver.unit.set_capacity(default_unit_capacity = enums.DefaultUnitCapacity.AF) \n
		No command help available \n
			:param default_unit_capacity: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_capacity, enums.DefaultUnitCapacity)
		self._core.io.write(f'UNIT:CAPacity {param}')

	# noinspection PyTypeChecker
	def get_energy(self) -> enums.DefaultUnitEnergy:
		"""SCPI: UNIT:ENERgy \n
		Snippet: value: enums.DefaultUnitEnergy = driver.unit.get_energy() \n
		No command help available \n
			:return: default_unit_energy: No help available
		"""
		response = self._core.io.query_str('UNIT:ENERgy?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitEnergy)

	def set_energy(self, default_unit_energy: enums.DefaultUnitEnergy) -> None:
		"""SCPI: UNIT:ENERgy \n
		Snippet: driver.unit.set_energy(default_unit_energy = enums.DefaultUnitEnergy.AJ) \n
		No command help available \n
			:param default_unit_energy: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_energy, enums.DefaultUnitEnergy)
		self._core.io.write(f'UNIT:ENERgy {param}')

	# noinspection PyTypeChecker
	def get_frequency(self) -> enums.DefaultUnitFrequency:
		"""SCPI: UNIT:FREQuency \n
		Snippet: value: enums.DefaultUnitFrequency = driver.unit.get_frequency() \n
		No command help available \n
			:return: default_unit_frequency: No help available
		"""
		response = self._core.io.query_str('UNIT:FREQuency?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitFrequency)

	def set_frequency(self, default_unit_frequency: enums.DefaultUnitFrequency) -> None:
		"""SCPI: UNIT:FREQuency \n
		Snippet: driver.unit.set_frequency(default_unit_frequency = enums.DefaultUnitFrequency.AHZ) \n
		No command help available \n
			:param default_unit_frequency: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_frequency, enums.DefaultUnitFrequency)
		self._core.io.write(f'UNIT:FREQuency {param}')

	# noinspection PyTypeChecker
	def get_resistor(self) -> enums.DefaultUnitResistor:
		"""SCPI: UNIT:RESistor \n
		Snippet: value: enums.DefaultUnitResistor = driver.unit.get_resistor() \n
		No command help available \n
			:return: default_unit_resistor: No help available
		"""
		response = self._core.io.query_str('UNIT:RESistor?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitResistor)

	def set_resistor(self, default_unit_resistor: enums.DefaultUnitResistor) -> None:
		"""SCPI: UNIT:RESistor \n
		Snippet: driver.unit.set_resistor(default_unit_resistor = enums.DefaultUnitResistor.AOHM) \n
		No command help available \n
			:param default_unit_resistor: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_resistor, enums.DefaultUnitResistor)
		self._core.io.write(f'UNIT:RESistor {param}')

	# noinspection PyTypeChecker
	def get_voltage(self) -> enums.DefaultUnitVoltage:
		"""SCPI: UNIT:VOLTage \n
		Snippet: value: enums.DefaultUnitVoltage = driver.unit.get_voltage() \n
		No command help available \n
			:return: default_unit_voltage: No help available
		"""
		response = self._core.io.query_str('UNIT:VOLTage?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitVoltage)

	def set_voltage(self, default_unit_voltage: enums.DefaultUnitVoltage) -> None:
		"""SCPI: UNIT:VOLTage \n
		Snippet: driver.unit.set_voltage(default_unit_voltage = enums.DefaultUnitVoltage.AV) \n
		No command help available \n
			:param default_unit_voltage: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_voltage, enums.DefaultUnitVoltage)
		self._core.io.write(f'UNIT:VOLTage {param}')

	# noinspection PyTypeChecker
	def get_angle(self) -> enums.DefaultUnitAngle:
		"""SCPI: UNIT:ANGLe \n
		Snippet: value: enums.DefaultUnitAngle = driver.unit.get_angle() \n
		No command help available \n
			:return: default_unit_angle: No help available
		"""
		response = self._core.io.query_str('UNIT:ANGLe?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitAngle)

	def set_angle(self, default_unit_angle: enums.DefaultUnitAngle) -> None:
		"""SCPI: UNIT:ANGLe \n
		Snippet: driver.unit.set_angle(default_unit_angle = enums.DefaultUnitAngle.DEG) \n
		No command help available \n
			:param default_unit_angle: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_angle, enums.DefaultUnitAngle)
		self._core.io.write(f'UNIT:ANGLe {param}')

	# noinspection PyTypeChecker
	def get_length(self) -> enums.DefaultUnitLenght:
		"""SCPI: UNIT:LENGth \n
		Snippet: value: enums.DefaultUnitLenght = driver.unit.get_length() \n
		No command help available \n
			:return: default_unit_lenght: No help available
		"""
		response = self._core.io.query_str('UNIT:LENGth?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitLenght)

	def set_length(self, default_unit_lenght: enums.DefaultUnitLenght) -> None:
		"""SCPI: UNIT:LENGth \n
		Snippet: driver.unit.set_length(default_unit_lenght = enums.DefaultUnitLenght.AM) \n
		No command help available \n
			:param default_unit_lenght: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_lenght, enums.DefaultUnitLenght)
		self._core.io.write(f'UNIT:LENGth {param}')

	# noinspection PyTypeChecker
	def get_current(self) -> enums.DefaultUnitCurrent:
		"""SCPI: UNIT:CURRent \n
		Snippet: value: enums.DefaultUnitCurrent = driver.unit.get_current() \n
		No command help available \n
			:return: default_unit_current: No help available
		"""
		response = self._core.io.query_str('UNIT:CURRent?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitCurrent)

	def set_current(self, default_unit_current: enums.DefaultUnitCurrent) -> None:
		"""SCPI: UNIT:CURRent \n
		Snippet: driver.unit.set_current(default_unit_current = enums.DefaultUnitCurrent.A) \n
		No command help available \n
			:param default_unit_current: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_current, enums.DefaultUnitCurrent)
		self._core.io.write(f'UNIT:CURRent {param}')

	# noinspection PyTypeChecker
	def get_power(self) -> enums.DefaultUnitPower:
		"""SCPI: UNIT:POWer \n
		Snippet: value: enums.DefaultUnitPower = driver.unit.get_power() \n
		No command help available \n
			:return: default_unit_power: No help available
		"""
		response = self._core.io.query_str('UNIT:POWer?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitPower)

	def set_power(self, default_unit_power: enums.DefaultUnitPower) -> None:
		"""SCPI: UNIT:POWer \n
		Snippet: driver.unit.set_power(default_unit_power = enums.DefaultUnitPower.AW) \n
		No command help available \n
			:param default_unit_power: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_power, enums.DefaultUnitPower)
		self._core.io.write(f'UNIT:POWer {param}')

	# noinspection PyTypeChecker
	def get_temperature(self) -> enums.DefaultUnitTemperature:
		"""SCPI: UNIT:TEMPerature \n
		Snippet: value: enums.DefaultUnitTemperature = driver.unit.get_temperature() \n
		No command help available \n
			:return: default_unit_temperature: No help available
		"""
		response = self._core.io.query_str('UNIT:TEMPerature?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitTemperature)

	def set_temperature(self, default_unit_temperature: enums.DefaultUnitTemperature) -> None:
		"""SCPI: UNIT:TEMPerature \n
		Snippet: driver.unit.set_temperature(default_unit_temperature = enums.DefaultUnitTemperature.C) \n
		No command help available \n
			:param default_unit_temperature: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_temperature, enums.DefaultUnitTemperature)
		self._core.io.write(f'UNIT:TEMPerature {param}')

	# noinspection PyTypeChecker
	def get_time(self) -> enums.DefaultUnitTime:
		"""SCPI: UNIT:TIME \n
		Snippet: value: enums.DefaultUnitTime = driver.unit.get_time() \n
		No command help available \n
			:return: default_unit_time: No help available
		"""
		response = self._core.io.query_str('UNIT:TIME?')
		return Conversions.str_to_scalar_enum(response, enums.DefaultUnitTime)

	def set_time(self, default_unit_time: enums.DefaultUnitTime) -> None:
		"""SCPI: UNIT:TIME \n
		Snippet: driver.unit.set_time(default_unit_time = enums.DefaultUnitTime.AS) \n
		No command help available \n
			:param default_unit_time: No help available
		"""
		param = Conversions.enum_scalar_to_str(default_unit_time, enums.DefaultUnitTime)
		self._core.io.write(f'UNIT:TIME {param}')
