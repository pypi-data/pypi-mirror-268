import bpkio_api.helpers.profile_generator as PG
from bpkio_api.helpers.handlers import ContentHandler, DASHHandler, HLSHandler


def make_transcoding_profile(handler: ContentHandler, schema_version: str):
    analyser = None
    if isinstance(handler, HLSHandler):
        analyser = PG.HlsAnalyser(handler)
    elif isinstance(handler, DASHHandler):
        analyser = PG.DashAnalyser(handler)
    else:
        raise Exception("Unsupported handler type")

    renditions = analyser.analyze_renditions()
    packaging = analyser.analyze_packaging()

    generator = PG.TranscodingProfileGenerator(schema=schema_version)
    profile = generator.generate(renditions, packaging)

    return (profile, analyser.messages + generator.messages)
