# Not used by any item
type = "passive"
runTime = "early"


def handler(fit, src, context):
    fit.ship.multiplyItemAttr("structureFullPowerStateHitpointMultiplier", src.getModifiedItemAttr("serviceModuleFullPowerStateHitpointMultiplier"))
