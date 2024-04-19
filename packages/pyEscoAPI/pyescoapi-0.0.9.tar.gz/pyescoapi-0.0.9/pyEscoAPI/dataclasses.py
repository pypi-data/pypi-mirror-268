from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class ComitenteData:
    numComitente: Optional[int]
    fechaApertura: datetime
    denominacion: str
    emailsInfo: Optional[str]
    esFisico: bool
    patrimonioEstim: Optional[int]
    patrimonioEstimMoneda: Optional[str]
    esInversorCalificado: bool
    actividad: Optional[int]
    expBrokerCta: bool
    expBrokerCtaNombre: Optional[str]
    expInversion: bool
    experienciaEnInversiones: Optional[str]
    especulativoOportunista: int
    montoEstimCta: Optional[int]
    montoEstimCtaMoneda: Optional[str]
    fechaDesdeCodTpContribIVA: datetime
    codTpContribIVA: str
    tpRiesgoCmt: Optional[str]
    tpManejoCart: Optional[str]
    tpCmtTrading: Optional[int]
    codCuotapartista: Optional[str]
    requiereFirmaConjunta: bool
    referenciaFirmaConjunta: Optional[str]
    codGrupoArOperBurs: Optional[int]
    codTpComitente: Optional[int]
    codCategoriaUIF: Optional[int]
    codGrupoArAcreencias: Optional[int]
    codGrupoArCustodia: Optional[int]
    noPresencial: bool
    firmoCondFechaDesde: Optional[datetime]
    terceroNoIntermediario: bool
    intermediario: bool
    oficialCuenta: Optional[int]
    administrador: Optional[int]
    productor: Optional[int]
    codTpBilleteraVirtual: Optional[str]
    pmtComsinCustodia: Optional[bool]
    pmtComRecepdeInf: Optional[bool]
    pmtDerechoenMonOpe: Optional[bool]
    pmtEsClienteEspecial: Optional[bool]
    pmtEsComPromotor: Optional[bool]
    pmtGeneraAvisosAlertasUIF: Optional[bool]
    pmtivAenMondeOpeMov: Optional[bool]
    pmtOperabajoAcuerdoLibreAdm: Optional[bool]
    pmtPermiteSuscribirCtaBancariaEnVBHome: Optional[bool]
    pmtRecibeMailCambioEstadoOrdenes: Optional[bool]
    pmtExcluyeCalculoRetencionPercepcionIVABoletosCheques: Optional[bool]
    pmtExcluyeCalculoResultadoOpContinuo: Optional[bool]
    pmtIncluyeGenracionCreditosParaOperar: Optional[bool]
    pmtInformaInterfazGTR: Optional[bool]
    pmtBonificaGastoCustodiaCV: Optional[bool]
    pmtSeCobraCustodia: Optional[bool]
    pmtSeCobranArancelesGestionBancaria: Optional[bool]
    pmtSeCobranCargosPorDescubierto: Optional[bool]
    pmtSeEnviaValuacion: Optional[bool]
    pmtSeFacturanCargosPorDescubierto: Optional[bool]
    pmtSeleimimenboletos: Optional[bool]
    pmtSeleImimenetiquetas: Optional[bool]
    juridicos: Optional[Juridicos]
    titulares: List[Persona]
    instrucciones: Optional[List[Instrucciones]]
    entMailing: List[EntMailing]
    codTpRiesgo: Optional[str]
    fechaVencimientoPerfil: Optional[datetime]
    tpContribRetencion: Optional[str]
    codCanalVta: Optional[int]
    codCategoria: Optional[int]
    codPRI: Optional[int]
    codPerfilCmt: Optional[int]
    numSucursal: Optional[str]


@dataclass
class Juridicos:
    numInscripcion: str
    lugarConstitucion: str
    folio: str
    libro: str
    tomo: str
    codPais: int
    tpContribIngBrutos: str
    cuit: str
    ruc: str
    rut: str
    esSociedadHecho: bool
    tpRegisJuridica: int
    esExtranjero: bool
    actividad: int
    numInscripcionIIBB: str
    codTpIdFatca: int
    idFatca: str
    actividadUIF: int
    giin: str
    esInversorCalificado: bool
    obsFatca: str
    cie: str
    fechaConstitucion: datetime
    

@dataclass
class Persona:
    apellido: Optional[str]
    nombre: Optional[str]
    tpDoc: Optional[int]
    numDoc: Optional[str]
    nacionalidad: Optional[int]
    fechaNacimiento: Optional[datetime]
    lugarNacimiento: Optional[str]
    sexo: Optional[int]
    estadoCivil: Optional[int]
    esPEP: Optional[bool]
    esSujetoObligado: Optional[bool]
    cuit: Optional[str]
    cuil: Optional[str]
    cdi: Optional[str]
    emailsInfo: Optional[str]
    noPresencial: Optional[bool]
    esInversorCalificado: Optional[bool]
    esBeneficiario: Optional[bool]
    esCliente: Optional[bool]
    esClienteEspecial: Optional[bool]
    esExtranjero: Optional[bool]
    codInterfaz: Optional[str]
    perteneceLUT: Optional[bool]
    giin: Optional[str]
    ruc: Optional[str]
    rut: Optional[str]
    idFatca: Optional[str]
    obsFatca: Optional[str]
    codTpIdFatca: Optional[int]
    codActividad: Optional[int]
    codActividadUIF: Optional[int]
    codTpContribIVA: Optional[str]
    tpPersona: Optional[bool]
    numImpositivo: Optional[str]
    persEmpresa: Optional[str]
    persCargo: Optional[str]
    persTpContribRetencion: Optional[str]
    persAgRecaudador: Optional[bool]
    persAgNroInscrip: Optional[str]
    persSSN: Optional[str]
    posicionCondominio: Optional[int]
    condTpCondominio: Optional[str]
    requiereFirma: Optional[bool]
    condEsAccionista: Optional[bool]
    condPorcParticipacion: Optional[int]
    condBeneficiario: Optional[int]
    patrimonioEstim: Optional[int]
    patrimonioEstimMoneda: Optional[str]
    tpRiesgoTitular: Optional[str]
    domicilioParticular: Optional[Domicilio]
    domicilioComercial: Optional[Domicilio]
    

@dataclass
class Domicilio:
    codPais: Optional[int]
    codProvincia: int
    altura: Optional[str]
    calle: Optional[str]
    piso: Optional[str]
    departamento: Optional[str]
    localidad: Optional[str]
    codigoPostal: Optional[str]
    telefono: Optional[str]
    fax: Optional[str]
    recibeInfoFax: Optional[bool]
    

@dataclass
class Instrucciones:
    banco: Optional[int]
    tpCuenta: Optional[int]
    moneda: str
    numSucursal: Optional[int]
    numeroCuenta: Optional[str]
    cbu: Optional[str]
    cuit: Optional[str]
    ctaAlias: Optional[str]


@dataclass
class EntMailing:
    codEntMailing: int
