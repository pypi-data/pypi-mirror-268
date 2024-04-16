import proto.dtx.messages.common.threat_pb2 as threat_pb2

def get_threat_category_name(tid):
    """
    Get threat category name from PB threat category ID
    """
    return threat_pb2.ThreatCategory.DESCRIPTOR.values_by_number[tid].name

def get_threat_class_name(tid):
    """
    Get threat class name from PB threat class ID
    """
    return threat_pb2.ThreatClass.DESCRIPTOR.values_by_number[tid].name

def get_threat_category_human_name(threat_category_id) -> str:
    """
    Return a humanized name for threat category
    """
    return get_threat_category_name(threat_category_id) \
            .replace("THREAT_CATEGORY_", "") \
            .replace("_", " ").title()

def get_threat_class_human_name(threat_class_id) -> str:
    """
    Return a humanized name for threat class
    """
    return get_threat_class_name(threat_class_id) \
            .replace("THREAT_CLASS_", "") \
            .replace("_", " ").title()
