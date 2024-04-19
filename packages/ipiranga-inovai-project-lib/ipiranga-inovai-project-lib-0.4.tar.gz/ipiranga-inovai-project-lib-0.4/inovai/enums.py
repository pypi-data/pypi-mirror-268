from enum import Enum


class DocumentStatus(Enum):
    INTEGRATED = 'INTEGRADO'
    PENDING_INTEGRATION = 'PENDENTE_INTEGRACAO'


class DocumentMovementType(Enum):
    INPUT = 'E',
    OUTPUT = 'S'


class ResponsibleMovement(Enum):
    ISSUER = 'EMITENTE'
    RECIPIENT = 'DESTINATARIO'
