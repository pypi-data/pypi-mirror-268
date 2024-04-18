from pathlib import Path

import pandas as pd

from nakamon import Nakamon

data_dir = Path(__file__).resolve().parent.parent / "data"
orange_skill = pd.read_csv(data_dir / "orange_skill.csv").set_index("スキル")


def get_parameters(skill_name: str, player: Nakamon, enemy: Nakamon) -> dict:
    player_ = player.data.iloc[0]
    enemy_ = enemy.data.iloc[0]
    parameters = {}

    parameters["自_系統"] = player_.loc["系統"]
    parameters["他_系統"] = enemy_.loc["系統"]

    parameters["スキル_属性"] = orange_skill.loc[skill_name, "属性"]
    if pd.isna(parameters["スキル_属性"]):
        parameters["スキル_属性"] = ""
    parameters["スキル_種別"] = orange_skill.loc[skill_name, "種別"]
    parameters["スキル_系統"] = orange_skill.loc[skill_name, "系統"]
    if parameters["スキル_系統"] and parameters["他_系統"] == parameters["スキル_系統"]:
        parameters["スキル_威力"] = orange_skill.loc[skill_name, "威力_系統"] * 0.01
    else:
        parameters["スキル_威力"] = orange_skill.loc[skill_name, "威力"] * 0.01
    parameters["攻撃回数"] = orange_skill.loc[skill_name, "攻撃回数"]

    parameters["自_攻"] = player_.loc["攻"]
    parameters["自_器用"] = player_.loc["器用"]
    parameters["自_攻魔"] = player_.loc["攻魔"]
    if parameters["スキル_属性"]:
        parameters["自_属性"] = player_.loc[f'{parameters["スキル_属性"]}・全']
    else:
        parameters["自_属性"] = 0
    if parameters["スキル_属性"]:
        if parameters["スキル_種別"] in ("斬撃", "体技"):
            attribute = player_.loc[f'{parameters["スキル_属性"]}・斬体']
        elif parameters["スキル_種別"] == "呪文":
            attribute = player_.loc[f'{parameters["スキル_属性"]}・呪文']
        elif parameters["スキル_種別"] == "ブレス":
            attribute = player_.loc[f'{parameters["スキル_属性"]}・ブレス']
        parameters["自_撃_属性"] = (
            attribute + player_.loc[f'{parameters["スキル_属性"]}・全']
        )
    else:
        parameters["自_撃_属性"] = 0
    parameters["自_撃_系統"] = player_.loc[f'撃・{parameters["他_系統"]}']

    parameters["他_守"] = enemy_.loc["守"]
    if parameters["スキル_種別"] == "斬撃":
        parameters["他_耐_スキル"] = enemy_.loc["耐・斬撃"]
    elif parameters["スキル_種別"] == "体技":
        parameters["他_耐_スキル"] = enemy_.loc["耐・体技"]
    elif parameters["スキル_種別"] == "呪文":
        parameters["他_耐_スキル"] = enemy_.loc["耐・じゅもん"]
    elif parameters["スキル_種別"] == "ブレス":
        parameters["他_耐_スキル"] = enemy_.loc["耐・ブレス"]
    parameters["他_耐_系統"] = enemy_.loc[f'耐・{parameters["自_系統"]}']
    if parameters["スキル_属性"]:
        parameters["他_耐_属性"] = enemy_.loc[f'耐・{parameters["スキル_属性"]}']
    else:
        parameters["他_耐_属性"] = 0
    return parameters


def calculate_physical_damage(
    skill_name: str, player: pd.Series, enemy: pd.Series
) -> float:
    parameters = get_parameters(skill_name, player, enemy)
    return (
        (parameters["自_攻"] * 0.5 - parameters["他_守"] * 0.25)
        * parameters["スキル_威力"]
        * (1 + parameters["自_撃_属性"])
        * (1 + parameters["自_撃_系統"])
        * (1 - parameters["他_耐_属性"])
        * (1 - parameters["他_耐_スキル"])
        * (1 - parameters["他_耐_系統"])
        * parameters["攻撃回数"]
    )


def calculate_magic_damage(
    skill_name: str, player: pd.Series, enemy: pd.Series
) -> float:
    parameters = get_parameters(skill_name, player, enemy)
    magic_power = parameters["自_攻魔"]

    damage_map = (
        pd.DataFrame(
            {
                "対象": {0: "1体", 1: "1体", 2: "1体", 3: "全体", 4: "全体", 5: "全体"},
                "ランク": {0: "A", 1: "B", 2: "C", 3: "A", 4: "B", 5: "C"},
                "最小魔力": {0: 15, 1: 15, 2: 15, 3: 15, 4: 15, 5: 15},
                "最大魔力": {0: 1200, 1: 1200, 2: 1200, 3: 1200, 4: 1200, 5: 1200},
                "最小威力": {0: 50, 1: 40, 2: 30, 3: 30, 4: 25, 5: 20},
                "最大威力": {0: 940, 1: 740, 2: 610, 3: 460, 4: 360, 5: 290},
            },
        )
        .astype({"最小威力": float})
        .set_index(["対象", "ランク"])
    )

    target = orange_skill.loc[skill_name, "対象"]
    rank = orange_skill.loc[skill_name, "ランク"]
    skill_parameters = damage_map.loc[(target, rank)]

    min_damage = skill_parameters["最小威力"]
    max_damage = skill_parameters["最大威力"]
    min_magic_power = skill_parameters["最小魔力"]
    max_magic_power = skill_parameters["最大魔力"]

    return (
        (
            (max_damage - min_damage)
            * (magic_power - min_magic_power)
            // (max_magic_power - min_magic_power)
            + min_damage
        )
        * (1 + parameters["自_撃_属性"])
        * (1 + parameters["自_撃_系統"])
        * (1 - parameters["他_耐_属性"])
        * (1 - parameters["他_耐_スキル"])
        * (1 - parameters["他_耐_系統"])
    )


def calculate_bless_damage(
    skill_name: str, player: pd.Series, enemy: pd.Series
) -> float:
    parameters = get_parameters(skill_name, player, enemy)
    bless_attack = parameters["自_攻"] + parameters["自_器用"]

    damage_map = (
        pd.DataFrame(
            {
                "対象": {0: "1体", 1: "1体", 2: "1体", 3: "全体", 4: "全体", 5: "全体"},
                "ランク": {0: "A", 1: "B", 2: "C", 3: "A", 4: "B", 5: "C"},
                "最小攻撃力": {0: 15, 1: 15, 2: 15, 3: 15, 4: 15, 5: 15},
                "最大攻撃力": {0: 2400, 1: 2400, 2: 2400, 3: 2400, 4: 2400, 5: 2400},
                "最小威力": {0: 50, 1: 40, 2: 30, 3: 30, 4: 25, 5: 20},
                "最大威力": {0: 940, 1: 740, 2: 610, 3: 460, 4: 360, 5: 290},
            },
        )
        .astype({"最小威力": float})
        .set_index(["対象", "ランク"])
    )
    if skill_name == "こうねつのガス":
        min_damage = 30
        max_damage = 400
        min_attack = 30
        max_attack = 2400
    else:
        target = orange_skill.loc[skill_name, "対象"]
        rank = orange_skill.loc[skill_name, "ランク"]
        skill_parameters = damage_map.loc[(target, rank)]
        min_damage = skill_parameters["最小威力"]
        max_damage = skill_parameters["最大威力"]
        min_attack = skill_parameters["最小攻撃力"]
        max_attack = skill_parameters["最大攻撃力"]

    return (
        (
            (max_damage - min_damage)
            * (bless_attack - min_damage)
            // (max_attack - min_attack)
            + min_damage
        )
        * (1 + parameters["自_撃_属性"])
        * (1 + parameters["自_撃_系統"])
        * (1 - parameters["他_耐_属性"])
        * (1 - parameters["他_耐_スキル"])
        * (1 - parameters["他_耐_系統"])
    )


def calculate_damage(skill_name: str, player: pd.Series, enemy: pd.Series) -> float:
    skill_data = orange_skill.loc[skill_name]
    shubetu = skill_data.loc["種別"]
    if shubetu in ("斬撃", "体技"):
        return calculate_physical_damage(skill_name, player, enemy)
    elif shubetu == "呪文":
        return calculate_magic_damage(skill_name, player, enemy)
    elif shubetu == "ブレス":
        return calculate_bless_damage(skill_name, player, enemy)
