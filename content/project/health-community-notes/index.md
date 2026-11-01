---
title: 'LLM-Augmented Health Community Notes'
summary: 'We improve health Community Notes through evidence-grounded augmentation, automated generation, and agents that learn from prior correction episodes.'
tags: ['Health Misinformation', 'Community Notes', 'Large Language Models', 'Self-Evolving Agents']
year: 2026
# Project page creation date; each publication retains its own publication date.
date: '2026-11-01'
featured: true
# WING contributors; full author lists appear in the associated publications.
authors: ['zihang', 'fanxiao', 'jiaying', 'min']
image:
  alt_text: 'CrowdNotes+ Figure 3: the Community Notes workflow and two LLM-assisted modes, evidence-grounded note augmentation and utility-guided note automation.'
  focal_point: 'Smart'
  preview_only: false
links:
  - name: 'CrowdNotes+ Paper'
    url: 'https://aclanthology.org/2026.acl-long.233/'
  - name: 'CrowdNotes+ Code & Data'
    url: 'https://github.com/jiayingwu19/CrowdNotesPlus'
  - name: 'EvoNote Paper'
    url: 'https://aclanthology.org/2026.findings-emnlp.142/'
  - name: 'EvoNote Code & Data'
    url: 'https://github.com/Maekami/EvoNote'
---

Community Notes can provide context for misleading health posts, but useful corrections often arrive late. We study how large language models can support timely, evidence-grounded correction: first by augmenting and automating individual notes, and then by reusing experience from previous cases to improve future notes. The project connects two complementary studies of health misinformation governance on social platforms.

In [Beyond the Crowd: LLM-Augmented Community Notes for Governing Health Misinformation]({{< relref "/publication/wu-etal-2026-beyond-crowd" >}}) (ACL 2026), we analyze 30.8K health-related notes and find a median delay of 17.6 hours before notes receive a helpfulness status. We introduce **CrowdNotes+**, which combines evidence-grounded note augmentation with utility-guided note automation. Its hierarchical evaluation separates relevance, correctness, and helpfulness, addressing the tendency to mistake fluent writing for factual accuracy. **HealthNotes**, a benchmark of 1.2K health notes annotated for helpfulness, supports this study. The [CrowdNotes+ repository](https://github.com/jiayingwu19/CrowdNotesPlus) provides the code and data.

In [Better with Experience: Self-Evolving LLM Agents for Evidence-Grounded Health Community Notes]({{< relref "/publication/fu-etal-2026-better" >}}) (Findings of EMNLP 2026), we investigate how note generation can improve across correction episodes. **EvoNote** distills feedback from completed trajectories into an evolving experience memory that guides claim analysis, evidence acquisition, and note writing. We evaluate it on **MM-HealthCN**, a 1.2K-instance multimodal benchmark with human-written notes and crowd-derived helpfulness labels. This extends the project's focus from improving individual corrections to learning reusable correction strategies. The [EvoNote repository](https://github.com/Maekami/EvoNote) provides the implementation and MM-HealthCN data.
