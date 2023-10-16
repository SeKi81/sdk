# automatically generated by the FlatBuffers compiler, do not modify

# namespace: openmeteo_sdk

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from openmeteo_sdk.MarineCurrent import MarineCurrent
from openmeteo_sdk.MarineDaily import MarineDaily
from openmeteo_sdk.MarineHourly import MarineHourly
from typing import Optional
np = import_numpy()

class MarineApiResponse(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MarineApiResponse()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMarineApiResponse(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MarineApiResponse
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MarineApiResponse
    def Latitude(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MarineApiResponse
    def Longitude(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MarineApiResponse
    def Elevation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MarineApiResponse
    def Model(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # MarineApiResponse
    def GenerationtimeMs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MarineApiResponse
    def UtcOffsetSeconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # MarineApiResponse
    def Timezone(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MarineApiResponse
    def TimezoneAbbreviation(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MarineApiResponse
    def Daily(self) -> Optional[MarineDaily]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = MarineDaily()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MarineApiResponse
    def Hourly(self) -> Optional[MarineHourly]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = MarineHourly()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MarineApiResponse
    def Current(self) -> Optional[MarineCurrent]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = MarineCurrent()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def MarineApiResponseStart(builder: flatbuffers.Builder):
    builder.StartObject(11)

def Start(builder: flatbuffers.Builder):
    MarineApiResponseStart(builder)

def MarineApiResponseAddLatitude(builder: flatbuffers.Builder, latitude: float):
    builder.PrependFloat32Slot(0, latitude, 0.0)

def AddLatitude(builder: flatbuffers.Builder, latitude: float):
    MarineApiResponseAddLatitude(builder, latitude)

def MarineApiResponseAddLongitude(builder: flatbuffers.Builder, longitude: float):
    builder.PrependFloat32Slot(1, longitude, 0.0)

def AddLongitude(builder: flatbuffers.Builder, longitude: float):
    MarineApiResponseAddLongitude(builder, longitude)

def MarineApiResponseAddElevation(builder: flatbuffers.Builder, elevation: float):
    builder.PrependFloat32Slot(2, elevation, 0.0)

def AddElevation(builder: flatbuffers.Builder, elevation: float):
    MarineApiResponseAddElevation(builder, elevation)

def MarineApiResponseAddModel(builder: flatbuffers.Builder, model: int):
    builder.PrependInt8Slot(3, model, 0)

def AddModel(builder: flatbuffers.Builder, model: int):
    MarineApiResponseAddModel(builder, model)

def MarineApiResponseAddGenerationtimeMs(builder: flatbuffers.Builder, generationtimeMs: float):
    builder.PrependFloat32Slot(4, generationtimeMs, 0.0)

def AddGenerationtimeMs(builder: flatbuffers.Builder, generationtimeMs: float):
    MarineApiResponseAddGenerationtimeMs(builder, generationtimeMs)

def MarineApiResponseAddUtcOffsetSeconds(builder: flatbuffers.Builder, utcOffsetSeconds: int):
    builder.PrependInt32Slot(5, utcOffsetSeconds, 0)

def AddUtcOffsetSeconds(builder: flatbuffers.Builder, utcOffsetSeconds: int):
    MarineApiResponseAddUtcOffsetSeconds(builder, utcOffsetSeconds)

def MarineApiResponseAddTimezone(builder: flatbuffers.Builder, timezone: int):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(timezone), 0)

def AddTimezone(builder: flatbuffers.Builder, timezone: int):
    MarineApiResponseAddTimezone(builder, timezone)

def MarineApiResponseAddTimezoneAbbreviation(builder: flatbuffers.Builder, timezoneAbbreviation: int):
    builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(timezoneAbbreviation), 0)

def AddTimezoneAbbreviation(builder: flatbuffers.Builder, timezoneAbbreviation: int):
    MarineApiResponseAddTimezoneAbbreviation(builder, timezoneAbbreviation)

def MarineApiResponseAddDaily(builder: flatbuffers.Builder, daily: int):
    builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(daily), 0)

def AddDaily(builder: flatbuffers.Builder, daily: int):
    MarineApiResponseAddDaily(builder, daily)

def MarineApiResponseAddHourly(builder: flatbuffers.Builder, hourly: int):
    builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(hourly), 0)

def AddHourly(builder: flatbuffers.Builder, hourly: int):
    MarineApiResponseAddHourly(builder, hourly)

def MarineApiResponseAddCurrent(builder: flatbuffers.Builder, current: int):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(current), 0)

def AddCurrent(builder: flatbuffers.Builder, current: int):
    MarineApiResponseAddCurrent(builder, current)

def MarineApiResponseEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return MarineApiResponseEnd(builder)