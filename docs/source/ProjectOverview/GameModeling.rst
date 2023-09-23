战斗建模简介
============

简介
---------
.. Tip:: 强烈建议在继续阅读之前对游戏《崩坏:星穹铁道》有一定了解

《崩坏:星穹铁道》是一款回合制的战斗游戏, 玩家的目标是控制所用的角色击败所有敌方单位(使其血量值归零并且从战场上消失). 游戏开始后，可控角色和敌方单位会根据各自当前行动值依次行动，行动值最小的单位将执行动作.
玩家单位具有能量条，能量条充满以后可以执行在任意位置插入的终结技回合.

.. seealso:: `攻略和游戏机制 <https://bbs.nga.cn/read.php?tid=36048929&rand=892>`_

这部分内容将会介绍战斗建模部分的代码框架逻辑:
整个游戏由GameManager进行控制,游戏内的所有可互动对象将会由CombatEntity描述. 对于战斗部分的建模 我们主要关注以下两大部分

- 角色和角色之间,  角色和敌人之间, 敌人和敌人之间的互动. 主要有包括: 攻击, 施加状态, 治疗三大类
- 所有可互动对象的行动情况
- 角色和敌人的数值,状态管理

游戏主循环和行动管理
----------
- GameManager: GameManager由一个主循环驱动,在游戏开始后开始从一个最小堆里取出需要行动的Cycle. 每个Cycle在执行之前需要从决策空间里进行一次决策. 如果这个Cycle是由敌方行动,GameManager将使用EnemeyAgent和RLAgent进行共同决策(RLAgent会决定是否执行插入回合), 如果这个Cycle是己方行动,那么这个Cycle将会由RLAgent进行决策(普攻/战技和插入回合).GameManager同时进行战技点数的管理.

- Cycle: Cycle是一个Agent可以执行决策的最小单位. Agent需要在每个Cycle的起始执行决策, 并在Cycle结束以后获得feedback. 每个Cycle属于一个CombatEntity. Cycle包含一个行动值,由所对应的CombatEntity的内置Timer决定. 如果这个Cycle属于插入回合/额外回合, 则拥有最高优先级, 优先于正常Cycle执行 每个CombatEntity会给定一个决策空间

- Timer: 用于管理行动值计算

.. seealso:: 关于游戏的行动值机制:`NGA 行动值计算教学 <https://bbs.nga.cn/read.php?tid=36255036>`_
对象互动
----------
- CombatEntity: CombatEntity是最基本的战斗对象, 主要包括角色和敌人两类. 神君,回合计数器等特殊单位也由CombatEntity实现.ComBatEntity会储存这个实体当前的状态和基础状态.
    - Enemy Enemy是CombatEntity的一个子类, Enemy的基础属性由敌人类型, 敌人等级共同决定
    - Character Character是CombatEntity的一个子类,Character的基础属性由角色本身,角色等级,角色光锥共同决定
        - LightCone. 光锥是一个会给Character提升基础属性的装备, 不同的光锥有不同的属性,由LightCone类进行解析. 由光锥的名字和等级决定属性

- StateAdjust: 游戏内的大多数特殊效果都由StatesAdjust实现. 尽管一些特殊效果在实际游戏中并不以可见buff形式出现，但是在本项目的框架中，这是最有效的实现方式 包括以下部分
    - 遗器效果
    - 光锥的特效
    - 普攻,战技的特效
    - 持续伤害
    - buff和debuff
    StateAdjust有以下几个基本类型
        - 开发中
- Event: StateAdjust拥有一个触发器列表, 会监听CombatEntity/GameManager内的触发器. 当CombatEntity或者GameManager执行特定动作的时候 会触发StatesAdjust的函数 执行相应动作.
- 主要事件包括以下部分
    - Entity事件
        - 攻击事件
            - 普通攻击
            - 战技攻击
            - 追加攻击
            - 终结技攻击
        - 受击事件
        - 生命值变化
        - 能量值变化
        - BUFF/DEBUFF变化
        - 角色Cycle开始
        - 角色Cycle结束
    - 世界事件
        - 游戏开始
        - 游戏结束
        - 战技点变化


数据管理
----------
- DataManager: 单例对象，用于储存各种表格数据以供解析 目前数据来源为666bj的解包数据.包括角色和敌人属性 目前需要开发技能倍率部分的解析



