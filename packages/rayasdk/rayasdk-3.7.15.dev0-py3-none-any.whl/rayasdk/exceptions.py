class SDKException(Exception): pass


# Connect Errors
# Init Errors
# Kill Errors
# Run Errors
# Scanner Errors
# Simulator Errors
# Skills Errors
class SkillException(SDKException): pass
class SkillDependency(SkillException): pass
class SkillManifestNotFound(SkillDependency): pass
class SkillCircularDependency(SkillDependency): pass
class SkillVersionNotCompatible(SkillDependency): pass
# Ssh Errros
# Tools Errors
# VCS Errors

