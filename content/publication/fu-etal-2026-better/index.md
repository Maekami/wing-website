---
title: 'Better with Experience: Self-Evolving LLM Agents for Evidence-Grounded Health Community Notes'
authors:
  - zihang
  - fanxiao
  - Jianyang Gu
  - Haonan Wang
  - Preslav Nakov
  - Bryan Hooi
  - min
  - jiaying
# Anthology specifies October only; day defaults to the first of the month.
date: '2026-10-01'
publishDate: '2026-11-01T00:00:00Z'
doi: '10.18653/2026.findings-emnlp.142'
publication_types: ['paper-conference']
publication: 'In *Findings of the Association for Computational Linguistics: EMNLP 2026*'
abstract: >-
  Large Language Model (LLM)-augmented Community Notes offer a scalable path for timely, evidence-grounded correction of health misinformation on social platforms. However, they still reset at every post, leaving useful correction experience from prior cases unused. We introduce EvoNote, an agentic framework that enables health Community Notes generation to self-evolve through an evolving experience memory of prior misinformation correction episodes.
  Its core is fine-grained credit assignment: EvoNote grounds trajectory-level feedback in health-specific note qualities and distills it into action-level memory for claim analysis, evidence acquisition, and note writing. We evaluate EvoNote on MM-HealthCN, a 1.2K-instance multimodal benchmark of user-flagged health posts with human-written Community Notes and crowd-derived helpfulness labels.
  Under a human-validated hierarchical utility judge, EvoNote-generated notes are preferred over corresponding human-written notes in 89.6% of cases; on a separate set of Needs More Ratings posts without a crowd helpfulness verdict, EvoNote produces helpful notes for 82.0% of cases. It also reduces time to an available candidate correction from multi-hour post-to-note delays to under 2 minutes on average.
  Analyses link these quality gains to stronger evidence use and reusable correction strategies, positioning self-evolving note generation as a promising paradigm for scalable health misinformation governance.
summary: 'EvoNote improves evidence-grounded health Community Notes by distilling prior correction episodes into reusable experience for claim analysis, evidence acquisition, and note writing.'
tags: ['Health Misinformation', 'Community Notes', 'Large Language Models', 'Self-Evolving Agents']
featured: false
links:
  - name: ACL Anthology
    url: 'https://aclanthology.org/2026.findings-emnlp.142/'
url_pdf: 'https://aclanthology.org/2026.findings-emnlp.142.pdf'
url_code: 'https://github.com/Maekami/EvoNote'
image:
  alt_text: 'One-pass note generation and EvoNote: an evolving experience memory distills and reuses prior correction episodes to improve evidence-grounded health Community Notes.'
  focal_point: 'Smart'
  preview_only: false
projects: []
---
