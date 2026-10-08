# 角色声线推演 · Character Voice Simulation

> 让某个角色**以第一人称开口**——想知道「她／他此刻还会说什么」、或需要贴着角色声线的素材（同人补完 / 对白 / 文案）。
> 反着用，它就是**指纹**：一堆没署名的碎碎念，认它出自谁的嘴。

## 什么时候用它

| 需求 | 走哪条 |
|:--|:--|
| 一次性：她此刻会说的一句/一段、同人补完、对白素材 | **分队声线推演**（本文） |
| 给无名文本（游戏彩蛋碎碎念 / 旧稿残句 / 台词摘录）认说话人 | **反用锚点表**（口癖 / 物件 / 场景 / 称呼四条反查） |
| 持续多轮、有记忆、要跟人来回聊下去 | 角色卡（见 `sillytavern-cards`）——分队做不到 |
| 官方设定 / 考据 | 走「角色建档」那套，勿混 |

**边界（先记住，别答窄）**：分队**演不了「多人」**——一次性、无共享频道、无记忆、上下文隔离，跑不成来回对话；
但**演得了「一个人」**，而这正是它的独门价值：起来的那份人格只装着档案，**声音里不带主会话的味**。

## 产出是什么

- **给得了**：隔离的声音（只装档案）／同档案多角度并行问话（今天·过去·对某人）／可验收（每句带出处）
- **给不了**：多轮来回、记忆、跨轮一致性、真正的「在场」——产的是**基于档案的推演**，不是她说过的话

## 配方（五步）

1. **先自备档案**：把该角色可用材料列成**绝对路径**喂进 context——官方设定档、故事正文（末章优先）、剧情整理、名场面金句集、概念词典、关系网络、暗线总账。分队不会自己找，路径给死。
2. **官方原文原样贴进 context**——它是声线锚。锚料＝角色的一手原话，不限体裁（互动台词／语音文本／信件／节日台词）。**官方旁白（第三人称叙述）只作语境，不当锚。**
3. **一队一问，并行跑**：每队 3~6 句，别贪多。
4. **四条硬约束写进 context**：① 语气贴官方声线；② 每个意象必须能在档案里找到出处，不得发明新设定／新角色／新事件；③ 输出分三段——正文 ／ 逐句依据 ／ 自陈「哪些是档案没有、我填的」；④ **只读官方层，不写文件**——把「严禁读创作层」明写进去（不写它会自己去翻）。
5. **收尾**：产物归创作区并标「基于官方档案推演（非官方）」；**依据段就是验收标准**——对不上档案的句子要么删要么改。

## 声线锚点表怎么提

只统计**角色的一手原话**（官方旁白与第三人称叙述不计），每角色一份，三步：

1. **统计**：自称 · 第二人称 · 句尾字频与感叹号 · 语气词与起手词 · 句式型 · 分场景差异——**每条结论都带条号**，可逐条回查（没条号就无法验收）。
2. **分层读**：常态称谓 ／ **引号内的引用与表演台词**（她在复述别人的话，不算口癖）／ **情绪松开的瞬间**——三层分开数才敢下结论。混成一个总数写进「硬锚」，推演就会把某个变体撒得满篇。
3. **抓「缺席词」**：同一作品里别的角色高频、这份语料里为 0 的语气词，是最省事的**区分器**——反向认人时也靠它。

数字走脚本，不靠眼看：

```bash
python3 scripts/voice_anchor_stats.py <作品库/台词/角色目录> \
    [--self <自称>] [--you <第二人称候选>] [--extra <信件.md>] [--json]
```

一次跑出条数／平均字数／自称与第二人称计数（附命中条号）／标点／句尾字频／语气词／起手词，**并按每档分列**。非场景锚料（信件、贺图引号原话）用 `--extra` **单独统计，别混算**。

## 反用：给无名文本认说话人

四条反查，按硬度排：**口癖／自称**（最硬，签名式用词直接锁人）→ **物件**（句中的具体道具去数据里搜，官方描述常与句子近乎逐字对应）→ **场景**（地点先把候选缩到「在场的人」）→ **称呼**（敬称与转述腔是签名）。

**先判代际、再认说话人**——前作与续作角色池不同，判错整池全错（两代共用的词——食物、道具、公司名——不算代际证据）。

**输出分级，别硬凑**：已定（依据写成可复核的引用）／倾向·日常（日常碎碎念归「日常」即可，不必定死到人）／待考（留空 ＋ 写清卡在哪）。

## 怎么用

把它放进你的 skills 目录（目录名用 `character-voice-simulation`）：

```bash
git clone https://github.com/feverZHONG/liya-character-voice-simulation.git <你的数据根>/skills/character-voice-simulation
```

零第三方依赖（脚本只用标准库）。**锚点表与产物都放你自己的作品库**，本仓只留方法。

## 许可

- `scripts/` 下的代码：**MIT**（全文见 `LICENSE`）
- 文档（`SKILL.md`、`references/`、本 README 正文）：**CC BY 4.0**（全文见 `LICENSE-DOCS`）

## 姊妹仓库

**同一族（把角色写对、写像）**

- [liya-sillytavern-cards](https://github.com/feverZHONG/liya-sillytavern-cards) —— 酒馆角色卡写法：V2 格式 / PList+Ali:Chat / 三个 Python 工具
- [liya-tavern-card-refinement](https://github.com/feverZHONG/liya-tavern-card-refinement) —— 酒馆角色卡精修：7 字段清单 / 槽位归位 / 6 类断言 / 可用性验收

**莉娅名下其他**

- [liya-subtraction-skill](https://github.com/feverZHONG/liya-subtraction-skill) —— 技能库做减法：冗余检测 / 拆薄 / 合并 / 归档判断
- [liya-persona-authoring](https://github.com/feverZHONG/liya-persona-authoring) —— 给 AI agent 写身份文件（SOUL.md 类）：创作流程 / 砍装饰留行为 / 减法与漂移对照
- [liya-sillytavern-worldbook](https://github.com/feverZHONG/liya-sillytavern-worldbook) —— 酒馆世界书（Lorebook）：触发链源码实证 + 体检 / 模拟 / 生成工具
- [liya-vision-recognition-traps](https://github.com/feverZHONG/liya-vision-recognition-traps) —— 视觉模型识图陷阱：22 条实测与对策（附真 OCR 通道、生图物理体检、两图差分）
- [liya-chat-game-referee](https://github.com/feverZHONG/liya-chat-game-referee) —— 群聊小游戏裁判：扫雷 / 五子棋 / 大话骰 / 骗子牌 / 掷骰决斗，一位裁判带六个引擎
- [liya-spy-game](https://github.com/feverZHONG/liya-spy-game) —— 谁是卧底：黑板规则 / 出题方法论 / 词库验证 / 身份分配器
- [liya-sea-turtle-soup](https://github.com/feverZHONG/liya-sea-turtle-soup) —— 海龟汤：推理方法论 + 档案流水线（turtle CLI）
- [liya-delegation-and-verification](https://github.com/feverZHONG/liya-delegation-and-verification) —— 委派与验收：任务书写法 / 并行隔离 / 把「自报」验成事实
- [liya-prose-quality-metrics](https://github.com/feverZHONG/liya-prose-quality-metrics) —— 稿子读起来「平」怎么办：先量再改（对话占比·句长σ·标点谱）＋ 7 个工具
- [liya-ruozhiba-wordbank](https://github.com/feverZHONG/liya-ruozhiba-wordbank) —— 弱智吧题防御手册：160 道逐题拆解 + 三连防御法（拆前提→指谬误→反杀）
- [liya-subtitle-proofreading](https://github.com/feverZHONG/liya-subtitle-proofreading) —— 字幕校对 / 重建 / 外挂 SRT（5 个纯标准库工具）
- [liya-corpus-line-mining](https://github.com/feverZHONG/liya-corpus-line-mining) —— 从语料 / 会话库挖可复用原句：候选池筛选 + 人审落库（零依赖）
- [liya-story-revision-plan](https://github.com/feverZHONG/liya-story-revision-plan) —— 小说全稿修订方案：评估 / 缺口清单 / 逐章大纲 / 信息融合 / 优先级
- [liya-dev-workflow](https://github.com/feverZHONG/liya-dev-workflow) —— 开发全流程方法论：环境侦查 / 计划 / spike / TDD / 调试 / 推送排障 / 同步验收
- [liya-news-verification](https://github.com/feverZHONG/liya-news-verification) —— 验证伞：轻量核查 / 交付前多源验证 / 链接危险识别 / 厂商官宣核实 / 链接考古
- [liya-knowledge-persistence](https://github.com/feverZHONG/liya-knowledge-persistence) —— 知识持久化：信息该放记忆层 / 文件 / 技能库的分层规范
- [liya-incident-review](https://github.com/feverZHONG/liya-incident-review) —— 社群事件复盘：素材收集 → 时间线重构 → 交叉验证 → 矛盾管理（输出理解不输出建议）
- [liya-document-translation](https://github.com/feverZHONG/liya-document-translation) —— 论文与长文档翻译：提取全文 → 术语表 → 并行分章 → 质量抽查 → 归档
- [liya-source-code-investigation](https://github.com/feverZHONG/liya-source-code-investigation) —— 外部项目调查：源码审计 / 拆包分层 / 数据实测 / 身份链（结论导向，非取用）
- [liya-dialogue-system-builder](https://github.com/feverZHONG/liya-dialogue-system-builder) —— 台词系统脚手架：触发维度画格子 / 模板+变量兜底 / 覆盖率验证（含 17 子命令工作台与示例角色）

---

*莉娅（[@feverZHONG](https://github.com/feverZHONG)）· 宇宙美好记录官*
