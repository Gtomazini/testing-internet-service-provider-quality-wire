
WRITING_UX = {
    'FIRST_MODULE': {
        'PT_BR' : "SUA CONEXÃO",
        'EN_US' : "YOUR CONNECTION"
    },
    'SECOND_MODULE' : {
    'PT_BR' : 'PING',
    'EN_US' : 'PING'
    },
    'THIRD_MODULE' : {
    'PT_BR' : 'PERDA DE PACOTES',
    'EN_US' : 'PACKAGE LOSS'
    },
    'CONECTION_LEVEL_QUALITY_GOOD' : {
        'PT_BR' : 'BOM',
        'EN_US' : 'GOOD'
    },
    'CONECTION_LEVEL_QUALITY_MEDIUM' : {
    'PT_BR' : 'MÉDIO',
    'EN_US' : 'MEDIUM'
    },
    'CONECTION_LEVEL_QUALITY_LOW' : {
    'PT_BR' : 'LENTO',
    'EN_US' : 'SLOW'
    },
    'BASIC_ERROR_VALIDATION': {
        'PT_BR' : 'NADA',
        'EN_US' : 'NONE'
    }
    }

def get_terms_lang(type_term: str, lang: str):
    return WRITING_UX[type_term][lang]