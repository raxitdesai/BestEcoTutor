def calculate_footprint(electricity_kwh, water_liters, transport_km, region="global_average"):
    factors = {
        "global_average": {"electricity": 0.45, "water": 0.0003, "transport": 0.15}
    }

    elec = electricity_kwh * factors[region]["electricity"]
    water = water_liters * factors[region]["water"]
    transp = transport_km * factors[region]["transport"]

    total = elec + water + transp

    return {
        "electricity_kg": elec,
        "water_kg": water,
        "transport_kg": transp,
        "total_kg": total,
        "total_tonnes": round(total / 1000, 3),
    }


def simulate_reduction(baseline_total_kg, target_reduction_percent=10.0):
    target_kg = baseline_total_kg * (1 - target_reduction_percent / 100)
    return {
        "baseline_kg": baseline_total_kg,
        "target_percent": target_reduction_percent,
        "target_kg": target_kg,
        "reduction_kg": baseline_total_kg - target_kg,
    }
