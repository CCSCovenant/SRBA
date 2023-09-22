战斗建模简介
============

简介
---------
这部分内容将会介绍战斗建模部分的代码框架逻辑:
整个游戏由GameManager进行控制,游戏内的所有可互动对象将会由CombatEntity描述.


- GameManager: GameManager由一个主循环驱动,在游戏开始后开始从一个最小堆里取出需要行动的Cycle. 每个Cycle在执行之前需要从决策空间里进行一次决策. 如果这个Cycle是由敌方行动,
GameManager将使用EnemeyAgent和RLAgent进行共同决策(RLAgent会决定是否执行插入回合), 如果这个Cycle是己方行动,那么这个Cycle将会由RLAgent进行决策(普攻/战技和插入回合).GameManager同时进行战技点数的管理.

- Cycle: Cycle是一个Agent可以执行决策的最小单位. Agent需要在每个Cycle的起始执行决策, 并在Cycle结束以后获得feedback. 每个Cycle属于一个CombatEntity. 每个CombatEntity会给定一个决策空间

- CombatEntity: CombatEntity是最基本的战斗对象, 主要包括角色和敌人两类. 神君,回合计数器等特殊单位也由CombatEntity实现.ComBatEntity会储存这个实体当前的状态和基础状态.
    -Enemy Enemy是CombatEntity的一个子类, Enemy的基础属性由敌人类型, 敌人等级共同决定
    -Character Character是CombatEntity的一个子类,Character的基础属性由角色等级,角色光锥共同决定

- StateAdjust: 游戏内的大多数特殊效果都由StatesAdjust实现. 包括以下部分
    - 遗器效果
    - 光锥的特效
    - 普攻,战技的特效
    
