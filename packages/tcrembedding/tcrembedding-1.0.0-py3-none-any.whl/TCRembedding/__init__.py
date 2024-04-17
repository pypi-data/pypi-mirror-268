# TCRembedding/__init__.py
from .version import __version__

def get_embedding_instance(embedding_name):
    """
    Dynamically import and return an instance of the requested embedding class based on the method name.
    
    :param embedding_name: The name of the embedding class for which to create an instance.
    :return: An instance of the requested embedding class.
    """
    if embedding_name == "EmbeddingATMTCR":
        from .ATMTCR.embedding import EmbeddingATMTCR
        return EmbeddingATMTCR()
    elif embedding_name == "EmbeddingcatELMo":
        from .catELMo.embedding import EmbeddingcatELMo
        return EmbeddingcatELMo()
    elif embedding_name == "EmbeddingclusTCR":
        from .clusTCR.embedding import EmbeddingclusTCR
        return EmbeddingclusTCR()
    elif embedding_name == "EmbeddingDeepRC":
        from .DeepRC.embedding import EmbeddingDeepRC
        return EmbeddingDeepRC()
    elif embedding_name == "EmbeddingDeepTCR":
        from .DeepTCR.embedding import EmbeddingDeepTCR
        return EmbeddingDeepTCR()
    elif embedding_name == "EmbeddingERGO":
        from .ERGOII.embedding import EmbeddingERGO
        return EmbeddingERGO()
    elif embedding_name == "EmbeddingESM":
        from .ESM.embedding import EmbeddingESM
        return EmbeddingESM()
    elif embedding_name == "EmbeddingGIANA":
        from .GIANA.embedding import EmbeddingGIANA
        return EmbeddingGIANA()
    elif embedding_name == "EmbeddingImRex":
        from .ImRex.embedding import EmbeddingImRex
        return EmbeddingImRex()
    elif embedding_name == "EmbeddingiSMART":
        from .iSMART.embedding import EmbeddingiSMART
        return EmbeddingiSMART()
    elif embedding_name == "EmbeddingLuuEtAl":
        from .LuuEtAl.embedding import EmbeddingLuuEtAl
        return EmbeddingLuuEtAl()
    elif embedding_name == "EmbeddingNetTCR2":
        from .NetTCR2_0.embedding import EmbeddingNetTCR2
        return EmbeddingNetTCR2()
    elif embedding_name == "EmbeddingpMTnet":
        from .pMTnet.embedding import EmbeddingpMTnet
        return EmbeddingpMTnet()
    elif embedding_name == "EmbeddingSETE":
        from .SETE.embedding import EmbeddingSETE
        return EmbeddingSETE()
    elif embedding_name == "EmbeddingTCRanno":
        from .TCRanno.embedding import EmbeddingTCRanno
        return EmbeddingTCRanno()
    elif embedding_name == "EmbeddingTCRGP":
        from .TCRGP.embedding import EmbeddingTCRGP
        return EmbeddingTCRGP()
    elif embedding_name == "EmbeddingTITAN":
        from .TITAN.embedding import EmbeddingTITAN
        return EmbeddingTITAN()
    elif embedding_name == "EmbeddingWord2Vec":
        from .Word2Vec.embedding import EmbeddingWord2Vec
        return EmbeddingWord2Vec()
    elif embedding_name == "EmbeddingTCRpeg":
        from .TCRpeg.embedding import EmbeddingTCRpeg
        return EmbeddingTCRpeg()
    else:
        raise ValueError(f"Unknown embedding method: {embedding_name}")

__all__ = ['get_embedding_instance', '__version__']
