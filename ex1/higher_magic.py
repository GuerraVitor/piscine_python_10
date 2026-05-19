from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} fire damage"


def heal(target: str, power: int) -> str:
    return f"Heal restore {target} for {power} HP"


def freeze(target: str, power: int) -> str:
    return f"Freeze slows {target} for {power} seconds"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def wrapper(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return wrapper


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def wrapper(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return wrapper


#def conditional_caster(condition: Callable, spell: Callable) -> Callable:
#def spell_sequence(spells: list[Callable]) -> Callable:
