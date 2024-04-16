HUMAN_UNITS = ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]
SPEED_UNITS = ["bps", "Kbps", "Mbps", "Gbps", "Tbps"]


def convert_to_human(value: float) -> tuple:
    """
    Convert number to human readable format
    """
    for unit in HUMAN_UNITS:
        if unit == HUMAN_UNITS[-1]:
            break
        if float(value) < 1024.0:
            break
        value /= 1024.0
    return value, unit
