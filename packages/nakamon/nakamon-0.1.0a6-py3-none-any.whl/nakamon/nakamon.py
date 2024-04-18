from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd

data_dir = Path(__file__).resolve().parent.parent / "data"
nakamon_status = pd.read_csv(data_dir / "nakamon_status.csv")
nakamon_resistance = pd.read_csv(data_dir / "resistance_status.csv", index_col="名前")
red_skill = pd.read_csv(data_dir / "red_skill.csv")
resistance_skill = pd.read_csv(data_dir / "resistance_skill.csv")
damage = [
    "メラ・斬体",
    "ギラ・斬体",
    "デイン・斬体",
    "イオ・斬体",
    "ヒャド・斬体",
    "バギ・斬体",
    "ドルマ・斬体",
    "ジバリア・斬体",
    "メラ・呪文",
    "ギラ・呪文",
    "デイン・呪文",
    "イオ・呪文",
    "ヒャド・呪文",
    "バギ・呪文",
    "ドルマ・呪文",
    "ジバリア・呪文",
    "メラ・ブレス",
    "ギラ・ブレス",
    "デイン・ブレス",
    "イオ・ブレス",
    "ヒャド・ブレス",
    "バギ・ブレス",
    "ドルマ・ブレス",
    "ジバリア・ブレス",
    "メラ・全",
    "ギラ・全",
    "デイン・全",
    "イオ・全",
    "ヒャド・全",
    "バギ・全",
    "ドルマ・全",
    "ジバリア・全",
    "撃・けもの系",
    "撃・鳥系",
    "撃・物質系",
    "撃・マシン系",
    "撃・水系",
    "撃・スライム系",
    "撃・ゾンビ系",
    "撃・悪魔系",
    "撃・ドラゴン系",
    "撃・怪人系",
    "撃・植物系",
    "撃・虫系",
    "撃・エレメント系",
    "撃・⁇⁇系",
]
probability_rates = [
    "会心率",
    "暴走率",
    "ガード率",
    "みかわし率",
    "全状態異常成功率",
    "麻痺成功率",
    "守備減成功率",
    "転び成功率",
    "魅了成功率",
    "混乱成功率",
    "眠り成功率",
    "怯え成功率",
]
resistance = list(
    resistance_skill.loc[:, "スキル"].str.split(":", expand=True).loc[:, 0].unique()
)
resistance.append("耐・⁇⁇系")


@dataclass
class Nakamon:
    name: str
    seikaku: str
    soshitsu: str
    skill: Optional[str|list] = None

    def __post_init__(self):
        self.status = (
            nakamon_status.groupby(["名前", "性格", "素質"])
            .get_group((self.name, self.seikaku, self.soshitsu))
            .iloc[0, :]
        )
        self.skills = []
        self.damage = pd.Series(index=damage).fillna(0)
        self.resistance = pd.Series(index=resistance).fillna(0)
        attribute_resistance = nakamon_resistance.loc[self.name]
        attribute_resistance.index = attribute_resistance.index.map(
            lambda x: f"耐・{x}"
        )
        self.resistance.loc[attribute_resistance.index] = attribute_resistance
        self.probability_rates = pd.Series(index=probability_rates).fillna(0)
        self.probability_rates["会心率"] = 0.01
        if self.skill:
            self.add_skill(self.skill)
        self.data = self.make_all_data()

    def add_red_skill(self, skill_name: str):
        status_change_map = {
            "さいだいHP": "HP",
            "さいだいMP": "MP",
            "こうげき力": "攻",
            "しゅび力": "守",
            "こうげき魔力": "攻魔",
            "きようさ": "器用",
            "すばやさ": "素早",
        }
        skill_category = skill_name.split(":")[0]
        status_change = status_change_map.get(skill_category)
        if status_change:
            diff = red_skill.set_index("スキル").loc[skill_name, :].iloc[0]
            self.status[status_change] = self.status[status_change] + diff
        elif skill_category in damage:
            diff = red_skill.set_index("スキル").loc[skill_name, :].iloc[0]
            self.damage[skill_category] = self.damage[skill_category] + diff
        elif skill_category in probability_rates:
            diff = red_skill.set_index("スキル").loc[skill_name, :].iloc[0]
            self.probability_rates[skill_category] = (
                self.probability_rates[skill_category] + diff
            )
        self.data = self.make_all_data()

    def add_resistance_skill(self, skill_name: str):
        skill_category = skill_name.split(":")[0]
        if skill_category in resistance:
            diff = resistance_skill.set_index("スキル").loc[skill_name, :].iloc[0]
            self.resistance[skill_category] = self.resistance[skill_category] + diff
        self.data = self.make_all_data()

    def _add_skill(self, skill_name: str):
        self.skills.append(skill_name)
        if skill_name in red_skill.loc[:, "スキル"].unique():
            self.add_red_skill(skill_name)
        elif skill_name in resistance_skill.loc[:, "スキル"].unique():
            self.add_resistance_skill(skill_name)
        self.data = self.make_all_data()

    def add_skill(self, skill: str | list):
        if isinstance(skill, str):
            self._add_skill(skill)
        elif hasattr(skill, "__iter__"):
            for skill_ in skill:
                self._add_skill(skill_)
        else:
            self._add_skill(skill)

    def make_all_data(self) -> pd.DataFrame:
        df = pd.DataFrame(pd.concat([self.status, self.damage, self.resistance])).T
        cast_columns = df.loc[:, "HP":].columns
        n = len(cast_columns)
        return df.astype(dict(zip(cast_columns, [float] * n)))
