from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional


from ssb_altinn3_util.constants.enums import UtsendingEnhetType, UtsendingFormat, MottakerType


class PeriodeResponseModel(BaseModel):
    id: int
    skjema_id: int
    periode_type: Optional[str] = None
    periode_nr: Optional[int] = None
    periode_aar: Optional[int] = None
    periode_dato: Optional[date] = None
    delreg_nr: Optional[int] = None
    enhet_type: Optional[str] = None
    vis_oppgavebyrde: str
    vis_brukeropplevelse: str
    har_skjemadata: str
    journalnummer: Optional[str] = None
    endret_dato: datetime
    endret_av: str


class UtsendingResponseModel(BaseModel):
    id: int
    periode_id: int
    utsendingstype_id: Optional[int] = None
    utsendingstype_navn: Optional[str] = None
    pulje: Optional[int] = None
    trigger: str
    test: bool
    altinn_uts_tidspunkt: Optional[datetime] = None
    altinn_tilgjengelig: Optional[datetime] = None
    altinn_svarfrist: Optional[date] = None
    endret_dato: datetime
    endret_av: str


class SkjemaResponseModel(BaseModel):
    id: int
    ra_nummer: str
    versjon: int
    undersokelse_nr: str
    datamodell: Optional[str] = None
    beskrivelse: Optional[str] = None
    navn_nb: Optional[str] = None
    navn_nn: Optional[str] = None
    navn_en: Optional[str] = None
    infoside: Optional[str] = None
    eier: Optional[str] = None
    kun_sky: str
    gyldig_fra: date
    gyldig_til: Optional[date] = None
    endret_dato: datetime
    endret_av: str

    # perioder: Optional[List[PeriodeResponseModel]]


class SkjemaPrefillMetaResponseModel(BaseModel):
    id: int
    skjema_id: int
    navn: str
    sti: Optional[str] = None
    rekkefolge: int
    type: str
    antall: Optional[int] = None
    kontroll: Optional[str] = None
    stat_navn: Optional[str] = None
    kommentar: Optional[str] = None
    endret_dato: datetime
    endret_av: str


class UtsendingstypeResponseModel(BaseModel):
    id: int
    navn: str
    enhet_type: UtsendingEnhetType
    utsendingsformat: UtsendingFormat
    mottakere: MottakerType

    endret_dato: datetime
    endret_av: str


class UtsendingsmalResponseModel(BaseModel):
    id: int
    skjema_id: int
    utsendingstype_id: int
    utsendingstype_navn: Optional[str] = None
    malnavn: str
    malversjon: int
    gyldig_fra: date
    gyldig_til: Optional[date] = None
    endret_dato: datetime
    endret_av: str
