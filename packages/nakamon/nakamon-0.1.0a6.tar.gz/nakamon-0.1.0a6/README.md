# なかモンダメージシミュレータ

## インストール

```
pip install nakamon
```

## 使い方

### `Nakamon` クラス

`Nakamon` クラスは仲間モンスターのステータスを格納するクラスです。

- name: モンスタ名
- seikaku: 性格
- soshitsu: 素質
- skill: 成長、継承玉（省略可）


```python
from nakamon import Nakamon

player = Nakamon("スライム", "いっぴきおおかみ", "極")
```

`status` 属性にアクセスすると、HPなどのステータスが参照できます


```python
player.status
```




    図鑑No           4
    名前          スライム
    系統         スライム系
    紫卵         5000歩
    特性          電光石火
    性格      いっぴきおおかみ
    素質             極
    HP           861
    MP           283
    攻            612
    守            431
    素早           630
    攻魔           152
    回魔           112
    器用           548
    Name: 2985, dtype: object



`damage` 属性にアクセスすると、与ダメージの補正値を参照できます


```python
player.damage
```




    メラ・斬体       0.0
    ギラ・斬体       0.0
    デイン・斬体      0.0
    イオ・斬体       0.0
    ヒャド・斬体      0.0
    バギ・斬体       0.0
    ドルマ・斬体      0.0
    ジバリア・斬体     0.0
    メラ・呪文       0.0
    ギラ・呪文       0.0
    デイン・呪文      0.0
    イオ・呪文       0.0
    ヒャド・呪文      0.0
    バギ・呪文       0.0
    ドルマ・呪文      0.0
    ジバリア・呪文     0.0
    メラ・ブレス      0.0
    ギラ・ブレス      0.0
    デイン・ブレス     0.0
    イオ・ブレス      0.0
    ヒャド・ブレス     0.0
    バギ・ブレス      0.0
    ドルマ・ブレス     0.0
    ジバリア・ブレス    0.0
    メラ・全        0.0
    ギラ・全        0.0
    デイン・全       0.0
    イオ・全        0.0
    ヒャド・全       0.0
    バギ・全        0.0
    ドルマ・全       0.0
    ジバリア・全      0.0
    撃・けもの系      0.0
    撃・鳥系        0.0
    撃・物質系       0.0
    撃・マシン系      0.0
    撃・水系        0.0
    撃・スライム系     0.0
    撃・ゾンビ系      0.0
    撃・悪魔系       0.0
    撃・ドラゴン系     0.0
    撃・怪人系       0.0
    撃・植物系       0.0
    撃・虫系        0.0
    撃・⁇⁇系       0.0
    dtype: float64



`resistance` 属性にアクセスすると、耐性の補正値を参照できます


```python
player.resistance
```




    耐・メラ       -0.50
    耐・ギラ        0.00
    耐・デイン       0.50
    耐・イオ        0.25
    耐・ヒャド      -0.25
    耐・バギ        0.25
    耐・ドルマ      -0.25
    耐・ジバリア      0.00
    耐・斬撃        0.00
    耐・ブレス       0.00
    耐・けもの系      0.00
    耐・鳥系        0.00
    耐・植物系       0.00
    耐・虫系        0.00
    耐・マシン系      0.00
    耐・エレメント系    0.00
    耐・スライム系     0.00
    耐・悪魔系       0.00
    耐・眠り        0.00
    耐・麻痺        0.00
    耐・混乱        0.00
    耐・幻惑        0.00
    耐・毒         0.00
    耐・即死        0.00
    耐・呪い        0.00
    耐・休み        0.00
    耐・魅了        0.00
    耐・攻撃減       0.00
    耐・守備減       0.00
    耐・封印        0.00
    耐・水系        0.00
    耐・すばやさ減     0.00
    耐・じゅもん      0.00
    耐・怪人系       0.00
    耐・踊り        0.00
    耐・怯え        0.00
    耐・吸収        0.00
    耐・ゾンビ系      0.00
    耐・ドラゴン系     0.00
    耐・物質系       0.00
    耐・体技        0.00
    耐・⁇⁇系       0.00
    dtype: float64



`data` 属性にアクセスすると、すべてのステータスを参照できます


```python
player.data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>図鑑No</th>
      <th>名前</th>
      <th>系統</th>
      <th>紫卵</th>
      <th>特性</th>
      <th>性格</th>
      <th>素質</th>
      <th>HP</th>
      <th>MP</th>
      <th>攻</th>
      <th>...</th>
      <th>耐・じゅもん</th>
      <th>耐・怪人系</th>
      <th>耐・踊り</th>
      <th>耐・怯え</th>
      <th>耐・吸収</th>
      <th>耐・ゾンビ系</th>
      <th>耐・ドラゴン系</th>
      <th>耐・物質系</th>
      <th>耐・体技</th>
      <th>耐・⁇⁇系</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>スライム</td>
      <td>スライム系</td>
      <td>5000歩</td>
      <td>電光石火</td>
      <td>いっぴきおおかみ</td>
      <td>極</td>
      <td>861.0</td>
      <td>283.0</td>
      <td>612.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 102 columns</p>
</div>



### 成長・継承玉（スキル）

成長や継承玉（スキル）を追加する場合は、 `Nakamon` クラスの引数 `skill` にリストで渡します。追加できるスキルは赤（ステータス）または水色（耐性）の2つです。追加するスキル数の上限はありません。


```python
player = Nakamon("スライム", "いっぴきおおかみ", "極", ["さいだいHP:S", "しゅび力:S"])
```

`skills` 属性にアクセスすると、追加したスキルを確認できます。


```python
player.skills
```




    ['さいだいHP:S', 'しゅび力:S']



スキルを追加するとステータスが変化します。


```python
player.status
```




    図鑑No           4
    名前          スライム
    系統         スライム系
    紫卵         5000歩
    特性          電光石火
    性格      いっぴきおおかみ
    素質             極
    HP         931.0
    MP           283
    攻            612
    守          481.0
    素早           630
    攻魔           152
    回魔           112
    器用           548
    Name: 2985, dtype: object



スキルを追加する場合は `add_skill` メソッドを実行します。


```python
player = Nakamon("スライム", "いっぴきおおかみ", "極")
```


```python
player.add_skill(["さいだいHP:S", "しゅび力"])
player.skills
```




    ['さいだいHP:S', 'しゅび力']




```python
player.status
```




    図鑑No           4
    名前          スライム
    系統         スライム系
    紫卵         5000歩
    特性          電光石火
    性格      いっぴきおおかみ
    素質             極
    HP         931.0
    MP           283
    攻            612
    守            431
    素早           630
    攻魔           152
    回魔           112
    器用           548
    Name: 2985, dtype: object



## ダメージ計算

`calculate_damage` 関数を実行するとスキルの与ダメージを計算します。

- skill_name: スキル名
- player: 攻撃を与える側の `Nakamon` インスタンス
- enemy: 攻撃を受ける側の `Nakamon` インスタンス


```python
from nakamon.damage import calculate_damage

enemy = Nakamon("ドラキー", "ぬけめがない", "優")
calculate_damage("セイントインパクト", player, enemy)
```




    324.0


