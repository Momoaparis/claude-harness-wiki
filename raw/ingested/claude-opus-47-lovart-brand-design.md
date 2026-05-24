---
title: "Claude Opus 4.7 配 Lovart：全套品牌设计只需点击 2 次，设计师可能不太需要了"
source: "https://mp.weixin.qq.com/s/WuLLXz-_XS0VsyAOgYp69g"
author:
  - "[[J0hn]]"
published:
created: 2026-05-23
description: "从 PDF 解析到海报、字体、Skill、PSD 再到 5 秒动态片，动嘴即可完成"
tags:
  - "clippings"
---
J0hn *2026年4月17日 09:01*

昨晚，Anthropic 发布了 Claude Opus 4.7，见前文： [Claude Opus 4.7 发布！留给人类的时间，不多了](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ==&mid=2453482866&idx=1&sn=785a8ccf063a484013f44f94a7cc11cd&scene=21#wechat_redirect) 。

![Image](https://mmbiz.qpic.cn/mmbiz_png/ZKqVLiaIpzFmZtNx8icDZeKzxQvQHP24ianNKJyH7eUyzdVcCyhialNuLLTrGHuwsNFtgZHvIsPmgLjCA6oWFBr1E7FQAQDmTYHNjnxykywUyOA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

我一边读发布稿，一边想起一件拖了很久的事。

我有一位认识了十年的老朋友，是北京一家手工美术馆的馆长，从去年春节前开始就在搞一个公益项目，叫「 **国宝回家** 」，要给那些流失海外的中国文物建一份数字化的「归途护照」。

他春节前后找过我多次，问我能不能顺手帮忙做一个小程序，最好还要有不错的品牌视觉，大白话说就是：逼格要高一点。

隔行如隔山，对于对国宝的尊敬且拥有一众 AI 的我当然是满口答应了。然后……一拖就拖到现在。

倒不是我偷懒，想法和实现我自认为都很擅长，但品牌视觉这玩意……程序员出身的我显然，并不擅长。

这就是所谓的视觉 taste 的重要性了，AI 没准已经杀死了前端，但要说杀死设计师，可能还需要不少时间。

所以每次有新模型发布，或者哪个 AI 设计工具更新，我都会用早就准备好 context 和指令的这个 case 试一把。结果一直都干不好：要么 AI 出图能看但毫无品牌感；要么品牌感勉强对了，主标题里的中文又扭成了奇怪的偏旁部首；要么海报本身还行，但根本没法交付，专业设计师连改都没法改。

而较劲的我则也不想找个人来帮忙，也是我确实太忙，也没空再找个人进行人与人之前的 context 传递。

懂的都懂，和 AI 传递 context 很方便随意，和人有时，还真挺费劲的。

![拖了两个月，第七次还是没过60分](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

拖了两个月，第七次还是没过60分

拖了两个月，第七次还是没过60分

每次失败，我都把这个 case 又往后塞了一次。

但今天的尝试，让我觉得，好像可以了。

01

## 两个问题

对我来说这事儿没办成，是有两个问题的叠加：

**一是 AI 设计工具不够好。**

大多数文生图工具只是「出图」，没有品牌资产管理、没有可编辑的图层导出、没有工作流沉淀。

设计师拿到一张拍平的 PNG，根本没法接着干活。我的想法是先快递给他弄个还行的 demo，然后就他自己找他圈里的人们路演，成了就自己找设计师去吧，我也就不用想再操心了。

**二是模型本身不够强。**

这个事儿，我当然不想去操作各种网页的界面，那多费劲啊。习惯偷懒的我想要的是用 CLI 或 MPC 让 AI 去直接操作网页。

之前有用过 Opus 4.6 的浏览器扩展、Computer Use 和浏览器 MCP，没有一次能干得很好的。

![两根线终于在中央撞上](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

两根线终于在中央撞上

两根线终于在中央撞上

一是 Lovart 刚好上线了 Brand Kit、Font Generator、Create Skill、Export PSD 四个新功能，把品牌设计的工程化链路，一次全打通了。

二是模型这边，Opus 4.7 加了「自我验证」机制，视觉感知基准从 4.6 的 54.5% 跳到了 98.5%，长任务连续工具调用的出错率下降约三分之一。

于是我决定，让它俩搭档来上一把。

02

## 让 Opus 4.7 上浏览器

Claude Code 有个功能叫 `--chrome` ，可以通过 MCP 把 Opus 4.7 接进我本地的 Chrome 浏览器，让模型直接在我已经登录的 Lovart 网页上自己一顿点点点。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

懒人如我，当然不会自己手动操作 Lovart。

我只是把整个「国宝回家」项目的文件夹一坨直接喂给了 Claude Code，告诉它：

> “ 你去 Lovart 上，从 Brand Kit 开始，造字、出海报、保存 Skill、导出 PSD，整套跑完。

然后我就跑茶去了。

![机械臂帮你点，茶水你来喝](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

机械臂帮你点，茶水你来喝

当我喝完回来，对话框里已经在跑 Lovart 的画布操作了，虽然速度比人慢，但非常的，不需要人。

03

## 先喂个品牌

第一步，Brand Kit。

这是个很程序员的逻辑：把一个品牌的 Logo、配色、字体、设计哲学，统一存进一个「资产库」，之后每次创作直接挂到项目级，让整个项目默认遵守这套规范。

听起来就像是给品牌做一份 schema 文件，类型化、可复用、一处定义多处生效。

但「国宝回家」是个全新项目，没有现成的品牌手册。Lovart 给的另一种玩法是：直接上传一份 **知名品牌** 的 PDF，让 AI 自己解析。

Opus 4.7 在我提供的品牌样例里翻出了一份《 **黑神话：悟空** 》IP 介绍手册，47MB。

![Image](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

它从众多品牌中做出这个选择的判断是：文化母题对得上，配色（墨黑、印章红、宣纸白）对得上，「东方史诗」的视觉哲学跟「国宝回家」的叙事简直是同一根线上长出来的。

然后，Claude Code 把 47MB 的 PDF 拖进了 Lovart，然后 Lovart 慢悠悠地跑了大约一分钟，完成。

弹出的解析面板里，则可以说是，把整本手册拆解了个稀碎透彻：

• **设计指南** （自动总结成一段精炼的英文哲学陈述：「视觉风格 = Oriental Epic，UE5 写实质感 + 书法 + 佛道符号」）

• **Logo** ：主标、文字版、Game Science 子品牌 Logo，分门别类提取

• **颜色** ：自动命名为 Brand Deep Black、Calligraphy White、 **Stamp Red**

• **图像素材** ：Environment Mood、Character Key Visual、Combat Action Shot

![Brand Kit 面板：黑神话悟空被解析成结构化资产](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Brand Kit 面板：黑神话悟空被解析成结构化资产

注意这个颜色名字，英文不好或者不仔细看，差点没看出来：「Stamp Red」直译就是「印章红」。

AI 看了几张悟空海报里出现的朱印，自己给这个红色取的名字。

我看着这个名字时，还愣了一下。

**这已经不是提取了，是真的在「理解」。**

![47MB PDF 被 reverse 成结构化资产](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

47MB PDF 被 reverse 成结构化资产

从我的视角看，等于是把一份散乱的 PDF reverse 出了一份结构化的 brand-config schema。

04

## 一句话出主视觉

Brand Kit 解析完，Opus 4.7 在 Lovart 里点了「使用此套件创建项目」。

新项目自动把 Brand Kit 挂到了项目级。

然后它给 Lovart 发了这么一段提示词（我一字未参与，Opus 4.7 自己来的）：

> “ 为「国宝回家」公益项目设计一张主视觉海报，竖版 3:4。
> 
> 主体：一件流失海外的中国古代青铜器从远方雾气中走来，背景是淡墨山水与故土剪影。
> 
> 主标题：国宝回家（毛笔书法）；副标题：让流失海外的中华文物，踏上归途。
> 
> 右下角留一枚朱红方印，「归」字。

并且 **完全没提** 「悟空」「中式建筑」「暖金光」这些细节词。

Lovart 用 Nano Banana Pro 跑了大约一分钟。

然后屏幕上的海报，就一寸一寸地长了出来：

![国宝回家海报第一稿](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

国宝回家海报第一稿

「 **国宝回家** 」四个毛笔大字，墨白色，置于画面顶端。一枚朱红方印贴在标题旁边。

中央是一位铠甲守护者形象（像悟空，也更像是被概括过的「文化武将」原型）。

背景是中式古建廊柱，灯笼悬挂，暖金光从顶部洒下。

底部摆着一组青铜礼器、玉龙、白瓷瓶。

我自然也没有动手指定其中任何一项。

这一切，都是 Brand Kit 里 Character Key Visual + Environment Mood + Stamp Red + Calligraphy White 在那个「世界观」里的自然延伸。

有个细节是：朱印还被它放到了右上角，而不是 Opus 4.7 在指令里说的右下角。

这其实更符合书法落款的传统，也算是触及 Opus 4.7 的文化短板了。

**Lovart 自己做了这个判断。**

到这一步，我心里默默给了上了不少分。

05

## 造个青铜字

接下来这个功能，对我这种「不太懂字体」的程序员来说，是真正的小惊喜。

Lovart 画布底部最右边有个不起眼的图标，叫 **Font Generator（字体生成器）** 。

逻辑非常简单：

上传一张参考图，或者用一段文字描述，约 3 分钟造一套西文字体出来，自动存进「My Fonts」字体库。

Opus 4.7 在风格描述里写了这么一段：

> “ A serif typeface with subtle brush-stroke texture. Heavy weight, with elegant tapered serifs that hint at Chinese stone-rubbing calligraphy. Like inscriptions on bronze ware or stone steles. Inspired by Black Myth: Wukong — oriental epic, dignified, weighty.

大致意思是：粗衬线 + 笔触感 + 碑帖味，像青铜器铭文，要厚重感。

按了生成。

约两分半之后，字体出来了，名字叫 **Bronze Calligraphy** （青铜书法）。

![字体生成器 Beta 面板](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

字体生成器 Beta 面板

注意这个字体的名字。

提示词里出现过 bronze ware 和 stone steles。Lovart 把 Bronze 拎了出来，组合了 Calligraphy，给字体落了个名。

比我自己起名要专业太多了，我最怕的就是起名这事了……有经验的都懂。

然后只需要字形直接扔进画布里，「LOVART」的文字就会展示出来。粗壮的衬线，深棕近黑的色调（不是纯黑，带一点暖意，就是提示词里写的「ink black with a hint of warmth」），收尾的衬线带一点微微的不规则锈蚀感。

跟我想象中刻在青铜礼器上的铭文，已经差不多对得上了。但当然，还是差一点，毕竟我连手都没上过，嘴也没开过。

我顺手拉了一份完整的字符样张出来：

![Bronze Calligraphy 字符样张：国宝回家 LOVART 公益项目](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Bronze Calligraphy 字符样张：国宝回家 LOVART 公益项目

而且这套字体已经自动存进「My Fonts」，下次在任何一个新项目里，都能直接使用。

不过好像， **字体生成器目前只支持西文，中文还没出** 。对国际化项目够用，但要造一套中文字体，那估计还得再等等。

06

## 设计 Skill

还有一个功能叫 **Create Skill** 。

Lovart 的逻辑是：你跟 Agent 跑了一轮满意的对话之后，可以一键把这次对话「提炼」成一个可复用的 Skill，下次新项目调出来直接用。

Opus 4.7 于是自己点了「基于此对话创建 Skill」。Lovart 自动总结了刚才整个对话的过程，给 Skill 起了个名字：

> “ **Game IP Charity Campaign Design** （游戏 IP 公益活动设计）

「Game IP」是因为用的 Brand Kit 是黑神话，「Charity Campaign」是因为说了公益项目，「Design」是因为做的是设计任务。

把这次对话的语义维度，精准地缩到了三个词。

![Skill Book：保存为 My Skill](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Skill Book：保存为 My Skill

到这里我想多说两句，关于 Skill 这个词。

它是去年 11 月以来，Agent 逐渐通用化的一个抽象，本质上在解决的问题是：

> “ 我上次怎么做的来着？

Skill 化的意义，是把「prompt-as-craft」（每次重新想一遍提示词，靠手感）升级成「prompt-as-asset」（成功的对话路径，作为资产被持久化、被版本化、被复用）。

![换个圈子，同一个抽象](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

换个圈子，同一个抽象

设计师对这个抽象可能还在适应，但作为一个习惯了把 best practice 沉淀成可执行模板的程序员， **我反而觉得这个功能的逻辑出奇地熟悉** 。

下次馆长又来找我聊什么项目，我可以直接打开 Skill Book 调出这个 Skill，预填的 Prompt 直接给我（不对，是给 AI）一个可复用的技能。

从而能省下许多「重新摸索」的 token 和时间成本。

当然，这个 Skill 我也没详细查看和打磨，毕竟本次目的是先交个差……

07

## PSD 导出

另外还有一个功能，对我来说还是蛮有用的，叫 **Export PSD** 。

之前 AI 出图基本是「死图」：一张平面 PNG/JPG 扔到你面前，想改文案得回去重写提示词再跑一遍。

设计师拿到这种图，几乎没法接着干活。

Lovart 这次非常直接且好用：在画布上选中海报，点工具栏下载按钮旁边的下拉箭头，选「 **导出 PSD** 」。

![导出 PSD 下拉菜单](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

导出 PSD 下拉菜单

然后，PSD 文件就会下载到本地了。

然后 Claude Code 自己用 Python 的 `psd-tools` 库扒了一下文件结构（也是本能动作了，我就不期望它能打开 PS 看这文件了）：

```
●●●PSD signature: 8BPS, version 1
Dimensions: 1276x1200, RGB 8-bit
Layers: 2
  [0] '国宝回家公益海报' - kind: pixel
  [1] 'Text: LOVART' - kind: type
└
```

注意这个 `kind: type` 。

这是一个 **可编辑文字图层** ，在 Photoshop 里打开后，可以直接双击改文案、换字号、改字体。

不是一张合并拍平的位图。

而且图层命名带语义，「国宝回家公益海报」「Text: LOVART」，不是 Layer 1 / Layer 2 这种垃圾命名。只是这次，好像整的不够复杂，应该来上几百上千层才够重磅……

**这就是 AI Design Agent 跟「随便一个文生图工具」的本质差异。**

AI 出 80 分初稿，专业设计师在 PS 里精修到 95 分，源文件能复用、能改、能交付、能带人。

08

## 再用 Seedance 2.0 让它动起来

到这里，海报、字体、Skill、PSD 都齐了。

但我还想到一件事：馆长之前提过，国宝回家的小程序启动页上，希望能有一段约 5 秒的氛围视频，让用户一打开就能感受到「文物归来」的庄重。

刚好 Lovart 这一波也把 **Seedance 2.0** 加了上来，新购或升级 Pro 会员，限时送最高 **150 次免费视频生成** 。

我额度还剩着不少，那就顺手用掉。

我让 Opus 4.7 直接用纯文本 prompt 喂给 Seedance（先别拿海报里的悟空形象去，那个会触发素材库的角色审核）：

> “ 一组中国古代青铜礼器（鼎、簋、爵）静静伫立在水墨山水的画面中央，背景是淡淡的远山剪影和缓缓升腾的雾气。镜头从俯视角度极缓慢地推进，金色暖光从画面顶部斜射而下，打在青铜器表面。地面有薄雾缓慢流动，空气中飘着几片缓慢飘落的花瓣。色调：墨黑、暖金、宣纸白、印章红点缀。

期间画布上一直挂着「Generating」。

提示词被 Lovart 自动翻译成英文喂给 Seedance 2.0，约 5 分钟之后（中间也跳出来一句「模型资源紧张，生成较慢」），第一版视频跑完了。

![Tibo 点评](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Tibo 点评

期间，Opus 4.7 的确是如 OpenAI 员工 Tibo 所说，很有点 codexy：

![非常的 Codexy](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

非常的 Codexy

Claude 自己下载视频，抽帧分析，并打开看了一眼：

![第一版：古庙宫殿场景](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

第一版：古庙宫殿场景

然后分析道：中式古庙的廊柱深邃，几尊青铜鼎摆在画面中前景，烛光从两侧打过来，中央那只大鼎里腾起一束温润的金光，雾气从顶部缓慢流下，玉璧、玉龙散落在前方。

怎么讲，倒是没毛病，质感也很到位，但……怎么感觉地点有点奇怪呢……

所幸 Opus 4.7 看完后，又自言自语回了一段话：

> “ 这一版偏「古庙宫殿」的实景感了，戏剧性强但不够清雅，跟「国宝回家」庄重悠远的公益气质有点错位。建议再来一版，把场景换成水墨山水留白意境，让青铜礼器作为唯一主体浮现，更符合东方文化叙事的疏朗感。

这也算是 Opus 4.7 这一代加的「 **自我验证** 」机制：跑完任务先自己审一遍，发现不对就直接再要一遍，不等我开口。

我当然也是，随它去吧……

有意思的是，Opus 4.7 还吸收了上一次的交互教训，给来了句：不要再问我选项！

![不要再问我选项](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

不要再问我选项

第二版又跑了五分钟左右出来：

![第二版：水墨山水里的青铜礼器](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

第二版：水墨山水里的青铜礼器

水墨晕染的远山剪影在两侧展开， **中央一只饕餮纹青铜大鼎伫立在米色宣纸般的留白里** ，小鼎、簋、爵围绕在旁。金色的光柱从画面上方斜照下来，打在鼎的口沿上，折射出温润的反光。画面四角各盖着一枚若隐若现的朱红印章。一两片红色的花瓣缓缓飘落。

整段 5 秒的镜头，是非常缓慢的俯视推进，水墨的山从侧面往中央汇聚，金光在雾气里微微浮动。

![Seedance 视频片段（第二版）](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Seedance 视频片段（第二版）

这一版，气质显然就，对上了。

就这一段 5 秒的氛围视频， **也是「我动嘴 → AI 干活」的一句话产物** 。

放在过去，这种古风氛围片，要找拍摄团队搭场景、布灯、调色、剪辑，几万块都打不住。哪怕找模板剪个特效片，也得耗一个下午。

现在，AI 会自行基于 context 描述一段话，等上 5 分钟，即可。

至此，从一份品牌手册 PDF，到品牌资产库、主视觉海报、专属字体、可复用 Skill、可编辑 PSD、再到一段动态宣传片， **整套品牌视觉的工程化链路，全部跑通了** 。

09

## 80 分够不够

整个过程，我没自己完全点过 Lovart 一下，除了登录、付款。

然后所有的动作，Brand Kit 上传、海报提示词、字体描述、Skill 保存、PSD 导出、Seedance 视频生成，都是 Opus 4.7 通过 Chrome MCP 自己在网页上完成的。

我其他做的事情就两件：

第一件，告诉它任务大概是什么；第二件，在它问我「这版海报你要不要改」的时候，回了一句「就这样吧」。

整套跑完，海报、字体、Skill、PSD、5 秒动态宣传片，都齐了。

老实说， **这版还不算能直接交付** 。

朱印里那个「归」字看上去像是 AI 糊成的乱码，主标题的英文副标位置可以再调一调，文物在画面里的占比相对小了一点，悟空那张脸有些太喧宾夺主了，需要再概括化一些才能更适合公益项目。

不过这些细节，我想扔给馆长朋友自己手动微调去吧，调完了扔回来，我再让 AI 用一晚上把小程序完成 coding + 上架，这事对我来说，就可以结束了。

**整套品牌世界观、主视觉构图、字体资产、可编辑源文件、宣传视频** ，已经一次性都到位了。

距离能让人来验收，可能就差那 15 到 20 分的精修，用时也就 15 到 20 分钟吧。

10

## 收多少钱合适

写到这里，我突然想到个问题：

我朋友本来是想找我帮个小忙，还说可以有些设计师费用的预算。

现在我动嘴让 AI 们给搞定了一套以前要花一周的活儿。

那……我应该收他多少钱合适呢？

按 token 收太亏，按设计师市价收又怪不好意思的，按「兄弟价」收……那不得免费了吗……

**先稳一稳，看他会不会看到这篇文章，再议。**

◇ ◆ ◇

相关链接：

• Lovart 官网：https://www.lovart.ai/

• Claude Opus 4.7 发布：https://www.anthropic.com/news/claude-opus-4-7

**微信扫一扫赞赏作者**

继续滑动看下一个

AGI Hunt

向上滑动看下一个