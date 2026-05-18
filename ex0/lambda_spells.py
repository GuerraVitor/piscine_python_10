def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


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


def main():
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'scrying'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'combat'},
        {'name': 'Old Wand', 'power': 15, 'type': 'training'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
          "power) comes before {sorted_artifacts[1]['name']}"
          "({sorted_artifacts[1]['power']} power)")

    spells = ["fireball", "heal", "shield"]
    transformed_spells = spell_transformer(spells)
    print("\nTesting spell transformer...")
    print(" ".join(transformed_spells))


if __name__ == "__main__":
    main()
