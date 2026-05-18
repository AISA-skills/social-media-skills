# Skill 去重合并分析

生成时间：2026-05-18

## 最新结论

- `targetSkills` 原始来源：54 个 skill
- AIsa 原仓库：10 个 skill
- 第一轮补齐后：54 个 skill
- 当前按“只删功能完全一致，保留子集入口”策略去重后：39 个 skill
- 当前删除同功能别名/重包：15 个 skill
- 从上一轮恢复的子集/垂直入口：14 个 skill

## 当前去重原则

- 只删除功能完全一致、同能力别名、OpenClaw 专属重包、或同一能力的替代包装。
- 即使某个 skill 是更大 skill 的子集，也保留为独立入口，用于搜索、分发和引流。
- 单一搜索模式、单一社媒动作、中文模型入口、YouTube search 等子集包均保留。
- reviewer 如需进一步压缩，可基于业务流量价值再决定。

## 删除的同功能重复 skills

- openclaw-media-gen: OpenClaw-specific repack of media-gen; same image/video generation capability and identical media_gen_client.py
- youtube: alias of youtube-serp with the same YouTube SERP capability and identical youtube_client.py
- openclaw-youtube: OpenClaw-specific repack of the YouTube SERP workflow
- aisa-youtube-serp-scout: alias of youtube-serp with the same YouTube SERP capability and identical youtube_client.py
- openclaw-aisa-youtube-aisa: OpenClaw-specific repack of the YouTube SERP workflow
- twitter: alias of twitter-autopilot with the same read/post/engagement surface
- twitter-command-center-search-post-interact: long-name alias of twitter-autopilot with the same read/post/engagement surface
- aisa-twitter-engagement-suite: same capability and same auxiliary files as aisa-twitter-post-engage; kept aisa-twitter-post-engage as the clearer action-oriented entry
- openclaw-twitter: OpenClaw-specific repack of Twitter read/post workflow
- openclaw-twitter-post-engage: OpenClaw-specific repack of Twitter read/post/engagement workflow
- aisa-multi-search-engine: broad multi-search alias overlapping multi-source-search/multi-search rather than a distinct subset entry
- search: generic command-center alias overlapping multi-source-search rather than a distinct subset entry
- openclaw-search: OpenClaw-specific repack of multi-source search
- prediction-market: alternate packaging of prediction-market-data with the same prediction-market data surface
- prediction-market-arbitrage-api: alternate packaging of prediction-market-arbitrage with the same arbitrage surface

## 已恢复/保留的子集入口

- aisa-twitter-api
- aisa-twitter-command-center
- aisa-twitter-post-engage
- cn-llm
- multi-search
- perplexity-research
- scholar-search
- smart-search
- tavily-extract
- tavily-search
- twitter-command-center-search-post
- web-search
- x-intelligence-automation
- youtube-search

## 最终保留 skills

- aisa-provider
- aisa-tavily
- aisa-twitter-api
- aisa-twitter-command-center
- aisa-twitter-post-engage
- aisa-youtube-search
- cn-llm
- crypto-market-data
- last30days
- last30days-zh
- llm-router
- market
- marketpulse
- media-gen
- multi-search
- multi-source-search
- perplexity-research
- perplexity-search
- prediction-market-arbitrage
- prediction-market-arbitrage-zh
- prediction-market-data
- prediction-market-data-zh
- scholar-search
- smart-search
- stock-analysis
- stock-dividend
- stock-hot
- stock-portfolio
- stock-rumors
- stock-watchlist
- tavily-extract
- tavily-search
- twitter-autopilot
- twitter-command-center-search-post
- us-stock-analyst
- web-search
- x-intelligence-automation
- youtube-search
- youtube-serp
