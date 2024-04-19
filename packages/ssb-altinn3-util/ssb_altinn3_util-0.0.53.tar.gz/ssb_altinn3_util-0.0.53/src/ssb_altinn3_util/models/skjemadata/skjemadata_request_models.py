from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional

from ssb_altinn3_util.constants.enums import UtsendingEnhetType, UtsendingFormat, MottakerType


class PeriodeRequestModel(BaseModel):
    id: Optional[int] = None
    skjema_id: int
    periode_type: Optional[str] = None
    periode_nr: Optional[int] = None
    periode_aar: Optional[int] = None
    periode_dato: Optional[date] = None
    delreg_nr: Optional[int] = None
    enhet_type: Optional[str] = None
    vis_oppgavebyrde: Optional[str] = "N"
    vis_brukeropplevelse: Optional[str] = "N"
    har_skjemadata: Optional[str] = "N"
    journalnummer: Optional[str] = None
    endret_av: str


class UtsendingRequestModel(BaseModel):
    id: Optional[int] = None
    periode_id: int
    utsendingstype_id: Optional[int] = None
    utsendingstype_navn: Optional[str] = None
    pulje: Optional[int] = None
    trigger: Optional[str] = "Manuell"
    test: Optional[bool] = False
    altinn_uts_tidspunkt: Optional[datetime] = None
    altinn_tilgjengelig: Optional[datetime] = None
    altinn_svarfrist: Optional[date] = None
    endret_av: str


class SkjemaRequestModel(BaseModel):
    id: Optional[int] = None
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
    kun_sky: Optional[str] = "N"
    gyldig_fra: date
    gyldig_til: Optional[date] = None
    endret_av: str


class SkjemaPrefillMetaRequestModel(BaseModel):
    id: Optional[int] = None
    skjema_id: int
    navn: str
    sti: Optional[str] = None
    rekkefolge: int
    type: Optional[str] = "ORDINAR"
    antall: Optional[int] = None
    kontroll: Optional[str] = "INGEN"
    stat_navn: Optional[str] = None
    kommentar: Optional[str] = None
    endret_av: str


class UtsendingstypeRequestModel(BaseModel):
    id: Optional[int] = None
    navn: str
    enhet_type: UtsendingEnhetType
    utsendingsformat: UtsendingFormat
    mottakere: MottakerType
    endret_av: str


class UtsendingsmalRequestModel(BaseModel):
    id: Optional[int] = None
    skjema_id: int
    utsendingstype_id: Optional[int] = None
    utsendingstype_navn: Optional[str] = None
    malnavn: str
    malversjon: int
    gyldig_fra: date
    gyldig_til: Optional[date] = None
    endret_av: str

