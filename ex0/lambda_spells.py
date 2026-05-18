def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_mage = max(mages, key=lambda mage: mage['power'])
    min_mage = min(mages, key=lambda mage: mage['power'])

    total_power = sum(map(lambda mage: mage['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        'max_power': max_mage['power'],
        'min_power': min_mage['power'],
        'avg_power': avg_power
    }
